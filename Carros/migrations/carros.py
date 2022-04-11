from database import Database

class Carros():

    def __init__(self):
        self.database = Database()
        self.conn = self.database.getConn()
        self.cursor = self.conn.cursor()

    def createTable(self):
        print("Criando tabela carros.\n")

        self.cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS carros (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                marca VARCHAR(50) NOT NULL,
                modelo VARCHAR(50) NOT NULL,
                ano INT NOT NULL,
                valor FLOAT NOT NULL 
            );
        """)

        print("Tabela criado com sucesso!\n")


    def getAll(self):
        print("Buscando todos carros:")

        self.cursor.execute(
            """
                SELECT * FROM carros;
            """
        )

        return self.cursor.fetchall()

    def getOne(self, id):

        print("Buscando pelo carro: "+ id)

        self.cursor.execute(
            """
                SELECT * FROM carros WHERE id = ?
            """, (id)
        )

        return self.cursor.fetchall()

    def criar(self):

        print("Criando um novo carro!")

        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        valor = input("Valor: ")

        self.cursor.execute(
            """
                INSERT INTO carros (marca, modelo, ano, valor)
                VALUES (?,?,?,?)
            """, (marca, modelo, ano, valor)
        )

        self.conn.commit()

    def atualizar(self):

        print("Atualizando algum carro")

        id = input("ID para modificar:")

        print("/********************/")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        valor = input("Valor: ")

        self.cursor.execute(
            """
                UPDATE carros SET marca = ?,  modelo = ?, ano = ? , valor = ?
                WHERE id = ?
            """, (marca, modelo, ano, valor, id)
        )

        self.conn.commit()

        print('Dados atualizados com sucesso.')

    def delete(self):
        print("Apagar um carro")

        id = input("ID: ")

        self.cursor.execute(
            """
                DELETE FROM carros where id = ?
            """, (id)
        )

        conn.commit()

        print('Registro excluido com sucesso.')

    def closeConn(self):
        print("\nDesligando conexão!")
        self.database.closeConn()