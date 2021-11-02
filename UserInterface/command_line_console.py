from Domain.rezervare import toString
from Logic.CRUD import modificarezervare, stergerezervare, adaugarezervare
from Logic.cerinte import cerinta7, cerinta5


def printmenu1():
    print("1)Add:")
    print("2)Showall: ")
    print("3)Delete: ")
    print("4)Stop: ")

def add_rezervare(lista):
    try:
        id = input("Dati ID: ")
        titlu = input("Titlu: ")
        pret = input("Pret: ")
        gen = input("Genul: ")
        reducere = input("Reducere(Silver/Gold): ")
        return adaugarezervare(id,titlu,gen,pret,reducere,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def sterg_rezervare(lista):
    try:
        id = input("Dati id ul unei comenzi: ")
        return stergerezervare(id,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def modif_rezervare(lista):
    try:
        id = input("Dati ID ul comenzii de modificat: ")
        titlu = input("Titlu nou: ")
        pret = input("Pret nou: ")
        gen = input("Genul nou: ")
        reducere = input("Reducere noua (Silver/Gold): ")
        return modificarezervare(id,titlu,gen,pret,reducere,lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def arata(lista):
    for comanda in lista:
        print(toString(comanda))

def ord_descresc(lista):
    return cerinta7(lista)

def aplic_discount(lista):
    return cerinta5(lista)


def command_line_console(lista):
    while True:
        printmenu1()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = add_rezervare(lista)
        elif optiune =="2":
            print(lista)
        elif optiune =="3":
            lista = sterg_rezervare(lista)
        elif optiune =="4":
            break
        else:
            print("Optiune incorecta! Reincercati: ")