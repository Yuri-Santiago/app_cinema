import mysql.connector


class Diretor:
    conexao = mysql.connector.connect(
        host="localhost",
        user="yuri",
        password="12345678",
        database="cinema")

    @classmethod
    def fecha_conexao(cls):
        cls.conexao.close()

    @classmethod
    def select_diretor(cls, diretor):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = f"SELECT idDiretores FROM diretores WHERE Nome = \"{diretor.title()}\""
        cursor.execute(sql)

        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return cls.insert(diretor)

    @classmethod
    def insert(cls, diretor):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "INSERT INTO diretores (Nome) " \
              "VALUES (%s)"
        val = (diretor.title(),)
        cursor.execute(sql, val)

        banco.commit()

        return cursor.lastrowid
