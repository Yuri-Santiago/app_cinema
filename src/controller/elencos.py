import json

from flask import Response, request

from src import app
from src.model.elenco import Elenco


# CREATE
@app.route("/elenco", methods=["POST"])
def insere_elenco():
    body = request.get_json()
    try:
        elenco = Elenco.insert(body)

        if elenco:
            return response(201, elenco, "Ator criado no elenco")
        else:
            return response(400, elenco, "Erro ao cadastrar")
    except Exception as e:
        print(e)
        return response(400, {}, "Erro ao cadastrar")


# READ
@app.route("/elenco/<id_filme>", methods=["GET"])
def seleciona_elenco(id_filme):
    elenco = Elenco.select(id_filme)
    if elenco:
        return response(200, elenco, 'Request Válido')
    else:
        return response(400, elenco, 'ID de filme inválido')


# UPDATE
@app.route("/elenco", methods=["PUT"])
def atualiza_elenco():
    body = request.get_json()
    elenco = Elenco.update(body)

    if elenco:
        return response(200, elenco, "Ator atualizado no elenco com sucesso")
    else:
        return response(400, elenco, 'Erro ao Atualizar')


# DELETE
@app.route("/elenco", methods=["DELETE"])
def deleta_elenco():
    body = request.get_json()
    elenco = Elenco.delete(body)
    if elenco:
        return response(200, elenco, "Ator deletado no elenco com sucesso")
    else:
        return response(400, elenco, "Erro ao deletar")


def response(status, elenco, mensagem=''):
    body = {"elenco": elenco}

    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="cinema/json")
