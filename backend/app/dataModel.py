from app import *
from model import DockerComands

# Inserindo de dados (carregando seus dados de seus arquivos)

data = [
    {"id": "1", "usable": "Listar Imagens:", "script": "$ docker images"},
    {"id": "2", "usable": "remover imagens", "script": "$ docker rmi <nomeImagem>"},
    {"id":"3", "usable": "remover imagens forçando-as", "script": "$ docker rmi -f <nomeImagem>"}
]

# For para inserção dos dados no banco de dados
with app.app_context():
    
    for item in data:
    
        dockercomands = DockerComands(**item)
        db.session.add(dockercomands)

    db.session.commit()
