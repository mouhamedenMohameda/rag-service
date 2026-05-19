# Déploiement rag-service

## Pré-requis

- Python 3.10+ sur le VPS
- Clé OpenAI : https://platform.openai.com/api-keys
- Les PDFs sources doivent être présents sur le VPS (rsync depuis ton Mac, ou git LFS, ou un autre mécanisme).

## 1. Setup local du service sur le VPS

```bash
# Cloner le repo (à pousser sur GitHub d'abord)
ssh root@5.189.153.144
cd /opt
git clone https://github.com/mouhamedenMohameda/rag-service.git
cd rag-service

# Venv + deps
python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

# Configurer .env
cp .env.example .env
# Édite .env :
#   OPENAI_API_KEY=sk-proj-...
#   RAG_S2S_KEY=<générer>   (python -c "import secrets; print(secrets.token_urlsafe(32))")
#   RAG_CHROMA_DIR=/opt/rag-service/data/chroma
#   RAG_PDF_ROOT=/opt/rag-service/pdfs
chmod 600 .env

# Préparer le dossier PDFs (copier depuis ton Mac)
mkdir -p /opt/rag-service/pdfs
# Sur ton Mac :
#   rsync -avh --include='*.pdf' --include='*/' --exclude='*' \
#     '/Users/mohameda/Documents/Bac/drive_archive/' \
#     root@5.189.153.144:/opt/rag-service/pdfs/
```

## 2. Indexation initiale (one-shot, ~5-15 min selon volume)

```bash
cd /opt/rag-service
source .venv/bin/activate
python ingest.py            # toutes les matières
# ou
python ingest.py --subject svt
# ou
python ingest.py --dry-run  # vérifie sans appel API
```

Vérifie le résultat :
```bash
.venv/bin/python -c "
import chromadb
c = chromadb.PersistentClient(path='./data/chroma').get_collection('bac_corpus')
print('Total chunks:', c.count())
for s in ['math','physique','chimie','svt']:
    r = c.get(where={'subject': s}, limit=1)
    print(f'  {s}:', len(c.get(where={\"subject\": s}).get(\"ids\", [])))
"
```

## 3. Service systemd

```bash
cp /opt/rag-service/rag-service.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable rag-service
systemctl start rag-service
systemctl status rag-service --no-pager | head -8

# Tester l'endpoint health
curl -s http://127.0.0.1:8001/health
# Attendu : {"ok":true,"chunks":<N>}

# Tester /search avec la clé S2S
RAG_KEY=$(grep RAG_S2S_KEY /opt/rag-service/.env | cut -d= -f2-)
curl -s -X POST http://127.0.0.1:8001/search \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: $RAG_KEY" \
  -d '{"subject":"svt","query":"qu est-ce que le linkage partiel","top_k":3}' | python3 -m json.tool
```

## 4. Configurer Débloque-moi pour appeler le RAG

Dans `/opt/debloquemoi/.env.local` ajouter :
```
RAG_SERVICE_URL=http://127.0.0.1:8001
RAG_S2S_KEY=<la même clé que dans /opt/rag-service/.env>
```

Puis :
```bash
cd /opt/debloquemoi
systemctl restart debloquemoi
journalctl -u debloquemoi -n 30 --no-pager
```

## 5. Mise à jour d'un PDF / réindexation

- Ajouter un nouveau PDF sous `/opt/rag-service/pdfs/` (au bon emplacement par matière)
- `cd /opt/rag-service && source .venv/bin/activate && python ingest.py`
  - Les PDFs déjà indexés sont sautés (fingerprint taille+mtime)
  - Un PDF modifié est ré-indexé (upsert)
- `systemctl restart rag-service` (recharge le compte de chunks)

Pour repartir de zéro : `python ingest.py --reset`.
