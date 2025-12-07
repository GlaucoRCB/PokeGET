# PokeGET

Uma API construída com FastAPI para buscar dados de Pokémon utilizando a PokeAPI.

# Tecnologias Utilizadas
- Python 3.13
- FastAPI
- Uvicorn
- Docker & Docker Compose

# Como rodar localmente (sem Docker)
- Criar e ativar venv
no bash
python -m venv .venv
.\.venv\Scripts\activate  no Windows

- Instalar as dependencias
pip install -r requirements.txt

- rodar servidor 
uvicorn basicRequests:app --reload


# Como Rodar com Docker 
no bash
- docker-compose up --build


