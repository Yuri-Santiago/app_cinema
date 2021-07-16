from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_object('config')

from src.controller import filmes
from src.controller import elencos
from src.controller import programacoes
