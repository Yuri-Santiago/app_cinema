import mysql.connector


class Distribuidora:
    conexao = mysql.connector.connect(
        host="localhost",
        user="yuri",
        password="12345678",
        database="cinema")

    @classmethod
    def fecha_conexao(cls):
        cls.conexao.close()

    @classmethod
    def select_distribuidora(cls, distribuidora):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = f"SELECT idDistribuidoras FROM distribuidoras WHERE Distribuidora = \"{distribuidora.title()}\""
        cursor.execute(sql)

        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return cls.insert(distribuidora)

    @classmethod
    def insert(cls, distribuidora):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "INSERT INTO distribuidoras (Distribuidora) " \
              "VALUES (%s)"
        val = (distribuidora.title(),)
        cursor.execute(sql, val)

        banco.commit()

        return cursor.lastrowid
