from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Configuração do banco de dados
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql://root:my_password@db/banco_de_dados_projeto"
db = SQLAlchemy(app)

# Defina seus modelos SQLAlchemy aqui
try:
    # Tenta inicializar o SQLAlchemy com as configurações
    db = SQLAlchemy(app)
    print(
        "Configuração do SQLAlchemy bem-sucedida. Conexão ao banco de dados bem-sucedida."
    )
except Exception as e:
    print(f"Erro ao configurar o SQLAlchemy: {e}")

if __name__ == "__main__":
    app.run()
