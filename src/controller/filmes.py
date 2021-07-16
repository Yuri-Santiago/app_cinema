import json

from flask import Response, request

from src import app
from src.model.elenco import Elenco
from src.model.filme import Filme
from src.model.programacao import Programacao


# READ ALL
@app.route("/filmes", methods=["GET"])
def seleciona_filmes():
    filmes = Filme.select_all()

    return response(200, filmes, 'Request Válido')


@app.route("/filmes/<genero>", methods=["GET"])
def seleciona_filmes_genero(genero):
    filmes = Filme.select_genero(genero)

    return response(200, filmes[0], 'Request Válido', numero=filmes[1])


# CREATE
@app.route("/filme", methods=["POST"])
def insere_filme():
    body = request.get_json()
    try:
        filme = Filme.insert(body)

        if filme:
            return response(201, filme, "Filme criado com sucesso")
        else:
            return response(400, filme, "Erro ao cadastrar")
    except Exception as e:
        print(e)
        return response(400, {}, "Erro ao cadastrar")


# READ
@app.route("/filme/<id_filme>", methods=["GET"])
def seleciona_filme(id_filme):
    filme = Filme.select_id(id_filme)
    elenco = Elenco.select(id_filme)
    programacao = Programacao.select_id(id_filme)
    if filme:
        return response(200, filme, 'Request Válido', elenco, programacao)
    else:
        return response(400, filme, 'ID de filme inválido')


# UPDATE
@app.route("/filme/<id_filme>", methods=["PUT"])
def atualiza_filme(id_filme):
    body = request.get_json()
    filme = Filme.update(body, id_filme)
    if filme:
        return response(200, filme, "Filme atualizado com sucesso")
    else:
        return response(400, filme, 'Erro ao Atualizar')


# DELETE
@app.route("/filme", methods=["DELETE"])
def deleta_filme():
    body = request.get_json()
    filme = Filme.delete(body)
    if filme:
        return response(200, filme, "Filme deletado com sucesso")
    else:
        return response(400, filme, "Erro ao deletar")


def response(status, filme, mensagem='', elenco=None, programacao=None, numero=None):
    body = {"filme": filme}

    if elenco:
        body["elenco"] = elenco
    if programacao:
        body["programacao"] = programacao
    if numero:
        body["numero"] = numero
    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="cinema/json")
