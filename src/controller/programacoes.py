import json

from flask import Response, request

from src import app
from src.model.programacao import Programacao


# CREATE
@app.route("/programacao", methods=["POST"])
def insere_programacao():
    body = request.get_json()
    try:
        programacao = Programacao.insert(body)

        if programacao:
            return response(201, programacao, "Programacao do filme criada com sucesso")
        else:
            return response(400, programacao, "Erro ao cadastrar")
    except Exception as e:
        print(e)
        return response(400, {}, "Erro ao cadastrar")


# READ
@app.route("/programacao/<id_filme>", methods=["GET"])
def seleciona_programacao(id_filme):
    programacao = Programacao.select_id(id_filme)
    if programacao:
        return response(200, programacao, 'Request Válido')
    else:
        return response(400, programacao, 'ID de filme inválido')


# UPDATE
@app.route("/programacao/<id_sala>", methods=["PUT"])
def atualiza_programacao(id_sala):
    body = request.get_json()
    programacao = Programacao.update(body, id_sala)
    if programacao:
        return response(200, programacao, "Programacao do filme atualizada com sucesso")
    else:
        return response(400, programacao, 'Erro ao Atualizar')


# DELETE
@app.route("/programacao", methods=["DELETE"])
def deleta_programacao():
    body = request.get_json()
    programacao = Programacao.delete(body)
    if programacao:
        return response(200, programacao, "Programacao do filme deletada com sucesso")
    else:
        return response(400, programacao, "Erro ao deletar")


def response(status, programacao, mensagem=''):
    body = {"programacao": programacao}

    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="cinema/json")
