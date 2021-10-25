from Domain.rezervare import toString
from Logic.CRUD import adaugarezervare, stergerezervare, modificarezervare
from Logic.cerinte import cerinta4, cerinta5, cerinta6economyplus, cerinta6economy, cerinta6business


def printmenu():
    print('1. Adauga rezervare')
    print('2. Sterge rezervare')
    print('3. Modifica rezervare')
    print('4. Trecerea tuturor rezervarilor la o clasa superioara')
    print('5. Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit')
    print('6. Determina prețul maxim pentru fiecare clasă')
    print('a. Afiseaza toate rezervarile')
    print('x. Iesire')

def UIadaugarezervare(lista):
    id = input('Dati id-ul: ')
    nume = input('Dati un nume: ')
    clasa = input('Dati clasa: ')
    pret = float(input('Dati pretul: '))
    checkin = input('Dati checkin: ')
    return adaugarezervare(id, nume, clasa, pret, checkin, lista)

def UIstergerezervare(lista):
    id = input('Dati id-ul rezervarii pe care vreti sa o stergeti: ')
    return stergerezervare(id , lista)

def UImodificarezervare(lista):
    id = input('Dati id-ul rezervarii de modificat: ')
    nume = input('Dati numele rezervarii de modificat: ')
    clasa = input('Dati clasa rezervarii de modificat: ')
    pret = float(input('Dati pretul rezervarii de modificat: '))
    checkin = input('Dati checkin-ul rezervarii de modificat: ')
    return modificarezervare(id, nume, clasa, pret, checkin, lista)

def showall(lista):
    for rezervare in lista:
        print(toString(rezervare))

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
            procentaj = int(input('Dati un procentaj cu care sa se reduca preturile celor care au checkin ul facut: '))
            lista = cerinta5(lista ,procentaj)
        elif optiune == '6':
            print('Pretul maxim de la economy este:')
            print(cerinta6economy(lista))
            print('Pretul maxim de la economy plus este: ')
            print(cerinta6economyplus(lista))
            print('Pretul maxim de la business este: ')
            print(cerinta6business(lista))
        elif optiune == 'a':
            showall(lista)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita!. Reincercati')
