from flask_sqlalchemy import SQLAlchemy
from app import *

class DockerComands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usable = db.Column(db.String(255))
    script = db.Column(db.String(255))


"""

data = [
    {"id": "1", "usable": "Listar Imagens:", "script": "$ docker images"},
    {"id": "2", "usable": "remover imagens", "script": "$ docker rmi <nomeImagem>"},
    {"id":"3", "usable": "remover imagens forçando-as", "script": "$ docker rmi -f <nomeImagem>"}
]

with app.app_context():
    
    for item in data:
        db.create_all()
        dockercomands = DockerComands(**item)
        db.session.add(dockercomands)

    db.session.commit()
"""