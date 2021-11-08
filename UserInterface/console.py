from Domain.rezervare import toString, getnume, getclasa, getpret, getcheckin
from Logic.CRUD import adaugarezervare, stergerezervare, modificarezervare, getbyid
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
    print('u. Undo')
    #print('r. Redo')
    print('a. Afiseaza toate rezervarile')
    print('x. Iesire')

def UIadaugarezervare(lista ,undooperations):
    try:
        id = input('Dati id-ul: ')
        nume = input('Dati un nume: ')
        clasa = input('Dati clasa: ')
        pret = float(input('Dati pretul: '))
        checkin = input('Dati checkin: ')
        rezultat = adaugarezervare(id, nume, clasa, pret, checkin, lista)
        undooperations.append(lambda: stergerezervare(id, rezultat))
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def UIstergerezervare(lista, undooperations):
    try:
        id = input('Dati id-ul rezervarii pe care vreti sa o stergeti: ')

        rezultat = stergerezervare(id , lista)
        rezervaredesters = getbyid(id, lista)
        undooperations.append(
            lambda: adaugarezervare(
            id,
            getnume(rezervaredesters),
            getclasa(rezervaredesters),
            getpret(rezervaredesters),
            getcheckin(rezervaredesters),
            rezultat))
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def UImodificarezervare(lista, undooperations):
    try:
        id = input('Dati id-ul rezervarii de modificat: ')
        nume = input('Dati numele rezervarii de modificat: ')
        clasa = input('Dati clasa rezervarii de modificat: ')
        pret = float(input('Dati pretul rezervarii de modificat: '))
        checkin = input('Dati checkin-ul rezervarii de modificat: ')
        rezultat =  modificarezervare(id, nume, clasa, pret, checkin, lista)
        rezervaredemodificat = getbyid(id, lista)
        undooperations.append(lambda: modificarezervare(
                id,
                getnume(rezervaredemodificat),
                getclasa(rezervaredemodificat),
                getpret(rezervaredemodificat),
                getcheckin(rezervaredemodificat),
                rezultat) )
        return rezultat
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
    undooperations = []
    while True:
        printmenu()
        optiune = input('Dati optiunea: ')
        if optiune == '1':
            lista = UIadaugarezervare(lista, undooperations)
        elif optiune == '2':
            lista = UIstergerezervare(lista, undooperations)
        elif optiune == '3':
            lista = UImodificarezervare(lista, undooperations)
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
        elif optiune == 'u':
            if len(undooperations) > 0:
                lista = undooperations.pop()()
            else:
                print('Nu se poate face undo')
        #elif optiune == 'r':

        elif optiune == 'a':
            showall(lista)
        elif optiune == 'x':
            break
        else:
            print('Optiune gresita!. Reincercati')
