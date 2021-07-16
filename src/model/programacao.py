import mysql.connector

from src.model.horario import Horario
from src.model.filme import Filme


class Programacao:
    conexao = mysql.connector.connect(
        host="localhost",
        user="yuri",
        password="12345678",
        database="cinema")

    @classmethod
    def fecha_conexao(cls):
        cls.conexao.close()

    @classmethod
    def select_id(cls, id_filme):
        try:
            banco = cls.conexao
            cursor = banco.cursor()

            sql = "SELECT horarios.DiaHora, DiaDaSemana, salas.idSalas, Capacidade, Formato, Idioma, Preco, " \
                  "QuantidadeAtual FROM programacao, horarios, salas WHERE programacao.DiaHora = horarios.DiaHora and" \
                  " programacao.idSalas = salas.idSalas " \
                  f"and idFilmes = {id_filme} ORDER BY DiaHora"

            cursor.execute(sql)
            programacoes = cursor.fetchall()
            return cls.programacoes_json(programacoes)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def insert(cls, body):
        try:
            dia_hora = Horario.select_horario(body['diaHora'], body['diaSemana'])
            id_filme = Filme.select_nome(body['filme'])

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "INSERT INTO programacao (DiaHora, idSalas, idFilmes, Formato, Idioma, Preco, QuantidadeAtual) " \
                  "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (dia_hora, body['sala'], id_filme, body['formato'], body['idioma'], float(body['preco']),
                   body['quantidade'])

            cursor.execute(sql, val)
            banco.commit()

            return cls.select_id(id_filme)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def update(cls, body, id_sala):
        try:
            id_filme = Filme.select_nome(body['filme'])

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "UPDATE programacao SET idFilmes = %s, Formato = %s, Idioma = %s, Preco = %s, QuantidadeAtual = %s " \
                  "WHERE (DiaHora = %s) and (idSalas = %s)"
            val = (id_filme, body['formato'], body['idioma'], body['preco'], body['quantidade'],
                   body['diaHora'], id_sala)

            cursor.execute(sql, val)
            banco.commit()

            return cls.select_id(id_filme)
        except Exception as e:
            print(e)
            return {}

    @classmethod
    def delete(cls, body):
        try:
            id_filme = Filme.select_nome(body['filme'])

            banco = cls.conexao
            cursor = banco.cursor()

            sql = "DELETE FROM programacao WHERE (DiaHora = %s) and (idSalas = %s)"
            val = (body['diaHora'], body['sala'])

            cursor.execute(sql, val)
            banco.commit()

            return cls.select_id(id_filme)
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def programacoes_json(programacoes):
        programacoes_json = []
        for programacao in programacoes:
            programacao_json = Programacao.programacao_json(programacao)
            programacoes_json.append(programacao_json)
        return programacoes_json

    @staticmethod
    def programacao_json(programacao):
        programacao_json = {
            'diaHora': ':'.join(str(programacao[0]).split()[1].split(':')[:2]),
            'diaSemana': programacao[1],
            'sala': programacao[2],
            'capacidade': programacao[3],
            'formato': programacao[4],
            'idioma': programacao[5],
            'preco': programacao[6],
            'quantidade': programacao[7]
        }
        return programacao_json
