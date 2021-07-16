import mysql.connector

from src.model.ator import Ator
from src.model.filme import Filme


class Elenco:
    conexao = mysql.connector.connect(
        host="localhost",
        user="yuri",
        password="12345678",
        database="cinema")

    @classmethod
    def fecha_conexao(cls):
        cls.conexao.close()

    @classmethod
    def select(cls, id_filme):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "SELECT atores.idAtores, atores.Nome, Personagem " \
              "FROM atores, filmes, elenco " \
              "WHERE elenco.idFilmes = filmes.idFilmes and elenco.idAtores = atores.idAtores " \
              f"and (filmes.idFilmes = {id_filme}) " \
              f"ORDER BY Nome"
        try:
            cursor.execute(sql)
            elenco = cursor.fetchall()
            return cls.elenco_json(elenco)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def insert(cls, body):
        try:
            id_ator = cls.get_id_ator(body['nome'])
            id_filme = Filme.select_nome(body['filme'])

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "INSERT INTO elenco (idFilmes, idAtores, Personagem) VALUES (%s, %s, %s)"
            val = (id_filme, id_ator, body['personagem'])

            cursor.execute(sql, val)
            banco.commit()

            return cls.select(id_filme)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def update(cls, body):
        try:
            id_ator = cls.get_id_ator(body['nome'])
            id_filme = Filme.select_nome(body['filme'])

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "UPDATE elenco SET Personagem = %s WHERE (idFilmes = %s) and (idAtores = %s)"
            val = (body['personagem'], id_filme, id_ator)

            cursor.execute(sql, val)
            banco.commit()

            return cls.select(id_filme)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def delete(cls, body):
        try:
            id_ator = cls.get_id_ator(body['nome'])
            id_filme = Filme.select_nome(body['filme'])

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "DELETE FROM elenco WHERE (idFilmes = %s) and (idAtores = %s)"
            val = (id_filme, id_ator)

            cursor.execute(sql, val)
            banco.commit()

            return cls.select(id_filme)
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def elenco_json(elenco):
        elenco_json = []
        for ator in elenco:
            ator_json = Elenco.ator_json(ator)
            elenco_json.append(ator_json)
        return elenco_json

    @staticmethod
    def ator_json(ator):
        ator_json = {
            'id': ator[0],
            'nome': ator[1],
            'personagem': ator[2]
        }
        return ator_json

    @staticmethod
    def get_id_ator(nome):
        id_ator = Ator.select_ator(nome)
        return id_ator
