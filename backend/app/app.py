from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import urllib.parse

app = Flask(__name__)

password = "my_password"
encoded_password = urllib.parse.quote_plus(password)

# Configuração do banco de dados
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = (f"mysql://root:{encoded_password}@mysql-container:3306/banco_de_dados_projeto")
db = SQLAlchemy(app)


if __name__ == "__main__":
    app.run(host='192.168.15.9', debug=True)
