import mysql.connector


class Ator:
    conexao = mysql.connector.connect(
        host="localhost",
        user="yuri",
        password="12345678",
        database="cinema")

    @classmethod
    def fecha_conexao(cls):
        cls.conexao.close()

    @classmethod
    def select_ator(cls, ator):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = f"SELECT idAtores FROM atores WHERE Nome = \"{ator.title()}\""
        cursor.execute(sql)

        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return cls.insert(ator)

    @classmethod
    def insert(cls, ator):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "INSERT INTO atores (Nome) " \
              "VALUES (%s)"
        val = (ator.title(),)
        cursor.execute(sql, val)

        banco.commit()

        return cursor.lastrowid
