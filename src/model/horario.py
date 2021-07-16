import mysql.connector


class Horario:
    conexao = mysql.connector.connect(
        host="localhost",
        user="yuri",
        password="12345678",
        database="cinema")

    @classmethod
    def fecha_conexao(cls):
        cls.conexao.close()

    @classmethod
    def select_horario(cls, horario, dia):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = f"SELECT DiaHora FROM horarios WHERE DiaHora = \"{horario}\""
        cursor.execute(sql)

        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return cls.insert(horario, dia)

    @classmethod
    def insert(cls, horario, dia):
        banco = cls.conexao
        cursor = banco.cursor()

        sql = "INSERT INTO horarios (DiaHora, DiaDaSemana) " \
              "VALUES (%s, %s)"
        val = (horario, dia)
        cursor.execute(sql, val)

        banco.commit()

        return cls.select_horario(horario, dia)
