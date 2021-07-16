import mysql.connector


class Genero:
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

        sql = f"SELECT idGeneros FROM generos WHERE Genero = \"{genero.title()}\""
        cursor.execute(sql)

        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return cls.insert(genero)

    @classmethod
    def insert(cls, genero):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "INSERT INTO generos (Genero) " \
              "VALUES (%s)"
        val = (genero.title(),)
        cursor.execute(sql, val)

        banco.commit()

        return cursor.lastrowid
