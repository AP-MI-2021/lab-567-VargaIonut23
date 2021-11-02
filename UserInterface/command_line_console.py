from Domain.rezervare import toString
from Logic.CRUD import adaugarezervare, stergerezervare, modificarezervare


def printMenuconsole():
    print("C. Comenzi.")
    print("b. Afisare")
    print("x. Iesire")

def uireadCommandLine(lista):
    stringCommandLine = input("Dati comenzile separate prin virgula:")
    return readCommandLine(stringCommandLine,lista)


def command_line_console(lista):
    while True:
        printMenuconsole()
        optiune = input("Dati optiunea: ")
        if optiune == "C":
            lista = uireadCommandLine(lista)
        elif optiune == "b":
            showAllCommand(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita!Reincercati!")


def readCommandLine(stringCommandLine, lista):
    list = stringCommandLine.split(",")
    for i in range(len(list)):
        if list[i] == "add":
            try:
                id = int(list[i + 1])
                nume = float(list[i + 2])
                clasa = list[i + 3]
                pret = list[i + 4]
                checkin = list[i + 5]
                lista = adaugarezervare(id, nume, clasa, pret, checkin, lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            print("Adaugarea s a realizat cu succes")
            i = i + 5
        elif list[i] == "delete":
            try:
               rezervare = int(list[i + 1])
               lista = stergerezervare(rezervare, lista)
            except ValueError as ve:
              print("Eroare: {}".format(ve))
            print("Stergerea s a realizat cu succes")
            i = i + 2
        elif list[i] == "update":
            try:
                id = int(list[i + 1])
                nume = str(list[i + 2])
                clasa = str(list[i + 3])
                pret = float(list[i + 4])
                checkin = str(list[i + 5])
                lista = modificarezervare(id, nume, clasa, pret, checkin, lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            print("Modificarea s a realizat cu succes")
            i = i + 5
        elif lista[i] == "showall":
            lista = showAllCommand(lista)
            i = i + 1
    return lista


def showAllCommand(lista):
    for rezervare in lista:
        print(toString(rezervare))