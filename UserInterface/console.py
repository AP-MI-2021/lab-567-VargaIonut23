from Domain.rezervare import toString
from Logic.CRUD import adaugarezervare, stergerezervare, modificarezervare
from Logic.cerinte import cerinta4, cerinta5, cerinta6economyplus, cerinta6economy, cerinta6business, cerinta7, cerinta8


def printmenu():
    print('1. Adauga rezervare')
    print('2. Sterge rezervare')
    print('3. Modifica rezervare')
    print('4. Trecerea tuturor rezervarilor la o clasa superioara')
    print('5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit')
    print('6. Determina prețul maxim pentru fiecare clasă')
    print('7. Odoneaza rezervarile in ordine descrescatoare dupa pret')
    print('8. Afișarea sumelor prețurilor pentru fiecare nume.')
    print('a. Afiseaza toate rezervarile')
    print('x. Iesire')

def UIadaugarezervare(lista):
    try:
        id = input('Dati id-ul: ')
        nume = input('Dati un nume: ')
        clasa = input('Dati clasa: ')
        pret = float(input('Dati pretul: '))
        checkin = input('Dati checkin: ')
        return adaugarezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def UIstergerezervare(lista):
    try:
        id = input('Dati id-ul rezervarii pe care vreti sa o stergeti: ')
        return stergerezervare(id , lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def UImodificarezervare(lista):
    try:
        id = input('Dati id-ul rezervarii de modificat: ')
        nume = input('Dati numele rezervarii de modificat: ')
        clasa = input('Dati clasa rezervarii de modificat: ')
        pret = float(input('Dati pretul rezervarii de modificat: '))
        checkin = input('Dati checkin-ul rezervarii de modificat: ')
        return modificarezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def showall(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uicerinta5(lista):
    try:
        procentaj = int(input('Dati un procentaj cu care sa se reduca preturile celor care au checkin ul facut: '))
        lista = cerinta5(lista, procentaj)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uicerinta6(lista):
    print('Pretul maxim de la economy este: {}'.format(cerinta6economy(lista)))
    print('Pretul maxim de la economy plus este: {} '.format(cerinta6economyplus(lista)))
    print('Pretul maxim de la business este: {} '.format(cerinta6business(lista)))


def uicerinta8(lista):
    print(cerinta8(lista))


def runmenu(lista):
    while True:
        printmenu()
        optiune = input('Dati optiunea: ')
        if optiune == '1':
            lista = UIadaugarezervare(lista)
        elif optiune == '2':
            lista = UIstergerezervare(lista)
        elif optiune == '3':
            lista = UImodificarezervare(lista)
        elif optiune == '4':
            lista = cerinta4(lista)
        elif optiune == '5':
            lista=uicerinta5(lista)
        elif optiune == '6':
            uicerinta6(lista)
        elif optiune == '7':
            lista = cerinta7(lista)
        elif optiune == '8':
            uicerinta8(lista)
        elif optiune == 'a':
            showall(lista)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita!. Reincercati')
