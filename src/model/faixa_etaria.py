import mysql.connector


class FaixaEtaria:
    conexao = mysql.connector.connect(
        host="localhost",
        user="yuri",
        password="12345678",
        database="cinema")

    @classmethod
    def fecha_conexao(cls):
        cls.conexao.close()

    @classmethod
    def select_faixa_etaria(cls, faixa_etaria):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = f"SELECT idFaixasEtarias FROM faixasetarias WHERE FaixaEtaria = \"{faixa_etaria}\""
        cursor.execute(sql)

        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return cls.insert(faixa_etaria)

    @classmethod
    def insert(cls, faixa_etaria):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "INSERT INTO faixasetarias (FaixaEtaria) " \
              "VALUES (%s)"
        val = (faixa_etaria,)
        cursor.execute(sql, val)

        banco.commit()

        return cursor.lastrowid
