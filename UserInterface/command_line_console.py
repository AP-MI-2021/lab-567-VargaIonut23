from Domain.rezervare import toString
from Logic.CRUD import adaugarezervare, stergerezervare


def printDescriere():
    print("Lista de comenzi va fi separat prin ; ")
    print("Comenzile pot fi: add, showall, delete, exit ")
    print("Parametri dintr-o comanda vor fi separati prin ,")

def command_line_console(lista):
    print (printDescriere())
    lista = []
    listainput = []
    while True:
        listainput = input("Dati lista de comenzi: ")
        listacomenzi = []
        listacomenzi = listainput.split(",")
        i = 1
        for i in range(len(listacomenzi)):
            if listacomenzi[i] == "add":
                lista = adaugarezervare(listacomenzi[i+1], listacomenzi[i+2], listacomenzi[i+3], listacomenzi[i+4], listacomenzi[i+5], lista)
                i = i + 6
            elif listacomenzi[i] == "delete":
                lista = stergerezervare(listacomenzi[i+1], lista)
                i = i + 2
            elif listacomenzi[i] == "showall":
                for rezervare in lista:
                    print(toString(rezervare))
                i = i + 1
            elif listacomenzi[i] == "exit":
                break

