from migrations.carros import Carros

if __name__ == "__main__":
    print("Iniciando Projeto!\n")

    carros = Carros()
    # carros.createTable()
    # carros.criar()
    # carros.atualizar()

    allCarros = carros.getAll()
    for row in allCarros:
        print(row)

    carros.closeConn()