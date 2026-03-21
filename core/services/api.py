import requests

BASE_URL = "https://hp-api.onrender.com/api"

def listar_personagens():
    response = requests.get(f"{BASE_URL}/characters")
    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def buscar_personagem_por_nome(nome):
    personagens = listar_personagens()

    personagem = next(
        (p for p in personagens if p['name'] == nome),
        None
    )

    return personagem