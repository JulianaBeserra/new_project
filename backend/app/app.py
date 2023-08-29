from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:my_password@db/banco_de_dados_projeto'
db = SQLAlchemy(app)

# Defina seus modelos SQLAlchemy aqui

if __name__ == '__main__':
    app.run(host='0.0.0.0')
