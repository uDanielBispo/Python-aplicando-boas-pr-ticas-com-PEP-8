from typing import Dict
from fastapi import FastAPI

from app.routers import routers_produtos, routers_usuarios

CONSTANTE_MENSAGEM_HOME: str = "Bem-vindo à API de Recomendação de Produtos"

# Criando o App
app = FastAPI()

app.include_router(routers_usuarios.router)
app.include_router(routers_produtos.router)


# Iniciando o servidor
@app.get("/")
def home() -> Dict[str, str]:
    global CONSTANTE_MENSAGEM_HOME
    return {"msg": CONSTANTE_MENSAGEM_HOME}
