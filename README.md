# CloudOps API

API REST em Python (FastAPI) usada como base para um pipeline completo de CI/CD
com GitHub Actions — testes automatizados, análise estática de segurança (SAST),
build de imagem Docker e publicação no Docker Hub.

> Projeto em construção. A documentação do pipeline entra junto com os workflows.

## Endpoints

| Método | Rota      | Resposta                                                            |
| ------ | --------- | ------------------------------------------------------------------- |
| `GET`  | `/`       | `{"mensagem": "...", "status": "online", "versao": "1.0.0"}`        |
| `GET`  | `/health` | `{"status": "healthy"}`                                             |

## Executar localmente

Requisitos: Python 3.12+

```bash
# 1. Ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 2. Dependências
pip install -r requirements.txt

# 3. Subir a API (a partir da raiz do projeto)
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

A API sobe em <http://localhost:8000>. A documentação interativa gerada pelo
FastAPI fica em <http://localhost:8000/docs>.

## Executar os testes

```bash
pytest tests/ -v
```

## Estrutura

```
.
├── app/
│   ├── __init__.py       # marca a pasta como módulo Python
│   └── main.py           # código da API
├── tests/
│   └── test_main.py      # testes unitários dos endpoints
├── requirements.txt
└── README.md
```

## Fluxo de trabalho

O projeto segue **GitFlow**:

- `main` — código de produção (branch protegida)
- `develop` — integração de features
- `feature/*` — desenvolvimento de funcionalidades
