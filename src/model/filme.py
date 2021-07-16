import mysql.connector

from src.model.diretor import Diretor
from src.model.distribuidora import Distribuidora
from src.model.faixa_etaria import FaixaEtaria
from src.model.genero import Genero


class Filme:
    conexao = mysql.connector.connect(
        host="localhost",
        user="yuri",
        password="12345678",
        database="cinema")

    @classmethod
    def fecha_conexao(cls):
        cls.conexao.close()

    @classmethod
    def select_genero(cls, genero):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "SELECT idFilmes,filmes.Nome, Sinopse, Duracao, Genero, FaixaEtaria, Distribuidora, diretores.Nome as " \
              "NomeDiretor, Cartaz, Capa FROM filmes, generos, faixasetarias, distribuidoras, diretores WHERE " \
              "filmes.idGeneros = generos.idGeneros and filmes.idFaixasEtarias = faixasetarias.idFaixasEtarias and " \
              "filmes.idDistribuidoras = distribuidoras.idDistribuidoras and filmes.idDiretores = diretores.idDiretores" \
              f" and generos.Genero = '{genero}' ORDER BY idFilmes"

        cursor.execute(sql)
        filmes = cls.filmes_json(cursor.fetchall())

        sql2 = "SELECT COUNT(idFilmes) as NumeroDeFilmes FROM " \
               "(SELECT idFilmes FROM filmes, generos WHERE filmes.idGeneros = generos.idGeneros " \
               f"and generos.Genero = '{genero}') as tabela"

        cursor.execute(sql2)
        numero = cursor.fetchone()[0]
        return filmes, numero

    @classmethod
    def select_all(cls):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "SELECT idFilmes,filmes.Nome, Sinopse, Duracao, Genero, FaixaEtaria, Distribuidora, diretores.Nome, " \
              "Cartaz, Capa FROM filmes, generos, faixasetarias, distribuidoras, diretores " \
              "WHERE filmes.idGeneros = generos.idGeneros and filmes.idFaixasEtarias = faixasetarias.idFaixasEtarias " \
              "and filmes.idDistribuidoras = distribuidoras.idDistribuidoras and filmes.idDiretores = " \
              "diretores.idDiretores " \
              "ORDER BY idFilmes"

        cursor.execute(sql)
        filmes = cursor.fetchall()
        return cls.filmes_json(filmes)

    @classmethod
    def select_id(cls, id_filme):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "SELECT idFilmes,filmes.Nome, Sinopse, Duracao, Genero, FaixaEtaria, Distribuidora, diretores.Nome, " \
              "Cartaz, Capa FROM filmes, generos, faixasetarias, distribuidoras, diretores " \
              "WHERE filmes.idGeneros = generos.idGeneros and filmes.idFaixasEtarias = faixasetarias.idFaixasEtarias " \
              "and filmes.idDistribuidoras = distribuidoras.idDistribuidoras and filmes.idDiretores = " \
              f"diretores.idDiretores and idFilmes = {id_filme} " \
              f"ORDER BY idFilmes"

        try:
            cursor.execute(sql)
            filme = cursor.fetchone()
            return cls.filme_json(filme)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def select_nome(cls, nome):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = f"SELECT idFilmes FROM filmes WHERE Nome = \"{nome}\""

        try:
            cursor.execute(sql)
            filme = cursor.fetchone()

            return filme[0]
        except Exception as e:
            print(e)
            return None

    @classmethod
    def insert(cls, body):
        try:
            ids = cls.get_ids(body['genero'], body['faixaEtaria'], body['distribuidora'], body['diretor'])

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "INSERT INTO filmes (idGeneros, idFaixasEtarias, idDistribuidoras, idDiretores, Nome, Sinopse, " \
                  "Duracao, Cartaz, Capa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (ids[0], ids[1], ids[2], ids[3], body['nome'], body['sinopse'], body['duracao'], body['cartaz'],
                   body['capa'])

            cursor.execute(sql, val)
            banco.commit()

            id_filme = cursor.lastrowid
            return cls.select_id(id_filme)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def update(cls, body, id_filme):
        try:
            ids = cls.get_ids(body['genero'], body['faixaEtaria'], body['distribuidora'], body['diretor'])

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "UPDATE filmes SET idGeneros = %s, idFaixasEtarias = %s, idDistribuidoras = %s, idDiretores = %s, " \
                  "Nome = %s, Sinopse = %s, Duracao = %s, Cartaz = %s, Capa = %s WHERE (idFilmes = %s)"
            val = (ids[0], ids[1], ids[2], ids[3], body['nome'], body['sinopse'], body['duracao'], body['cartaz'],
                   body['capa'], id_filme)

            cursor.execute(sql, val)
            banco.commit()

            return cls.select_id(id_filme)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def delete(cls, body):
        try:
            id_filme = cls.select_nome(body['nome'])
            filme = cls.select_id(id_filme)

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "DELETE FROM filmes WHERE (idFilmes = %s)"
            val = (int(id_filme),)

            cursor.execute(sql, val)
            banco.commit()

            return filme
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def filmes_json(filmes):
        filmes_json = []
        for filme in filmes:
            filme_json = Filme.filme_json(filme)
            filmes_json.append(filme_json)
        return filmes_json

    @staticmethod
    def filme_json(filme):
        filme_json = {
            'id': filme[0],
            'nome': filme[1],
            'sinopse': filme[2],
            'duracao': filme[3],
            'genero': filme[4],
            'faixaEtaria': filme[5],
            'distribuidora': filme[6],
            'diretor': filme[7],
            'cartaz': str(filme[8]).replace("b'", "").replace("'", ""),
            'capa': str(filme[9]).replace("b'", "").replace("'", "")
        }
        return filme_json

    @staticmethod
    def get_ids(genero, faixa_etaria, distribuidora, diretor):
        id_genero = Genero.select_genero(genero)
        id_faixa_etaria = FaixaEtaria.select_faixa_etaria(faixa_etaria)
        id_distribuidora = Distribuidora.select_distribuidora(distribuidora)
        id_diretor = Diretor.select_diretor(diretor)

        return id_genero, id_faixa_etaria, id_distribuidora, id_diretor
