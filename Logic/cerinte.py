from Domain.rezervare import creeazarezervare, getId, getnume, getclasa, getpret, getcheckin


def cerinta4(lista):
    '''
    creste clasa oricarei rezervari
    :param lista: lista de rezervari
    :return: listanoua
    '''
    listanoua = []
    for rezervare in lista:
        rezervarenoua = creeazarezervare(
            getId(rezervare),
            getnume(rezervare),
            getclasa(rezervare),
            getpret(rezervare),
            getcheckin(rezervare),
        )
        if getclasa(rezervarenoua) == 'economy':
            rezervarenoua['clasa'] = 'economy plus'
        elif getclasa(rezervarenoua) == 'economy plus':
            rezervarenoua['clasa'] = 'business'
        listanoua.append(rezervarenoua)
    return listanoua

def cerinta5(lista, procentaj):
    '''
    reduce fiecare pret cu procentajul introdus
    :param lista: lista de rezervari
    :param procentaj: float
    :return: listanoua
    '''
    listanoua = []
    for rezervare in lista:
        rezervarenoua = creeazarezervare(
            getId(rezervare),
            getnume(rezervare),
            getclasa(rezervare),
            getpret(rezervare),
            getcheckin(rezervare),
        )
        if getcheckin(rezervarenoua) == 'da' :
            rezervarenoua['pret'] = rezervarenoua['pret'] - (procentaj * rezervarenoua['pret'] / 100)
        listanoua.append(rezervarenoua)
    return listanoua

def cerinta6economy(lista):
    '''
    determina cel mai mare pret de la clasa economy
    :param lista: lista de rezervari
    :return: maxi
    '''
    maxi = 0
    for rezervare in lista:
        rezervarenoua = creeazarezervare(
            getId(rezervare),
            getnume(rezervare),
            getclasa(rezervare),
            getpret(rezervare),
            getcheckin(rezervare),
        )
        if getclasa(rezervarenoua) == 'economy' and getpret(rezervarenoua) > maxi :
            maxi = rezervarenoua['pret']
    return maxi

def cerinta6economyplus(lista):
    '''
        determina cel mai mare pret de la clasa economy plus
        :param lista: lista de rezervari
        :return: maxi
        '''
    maxi = 0
    for rezervare in lista:
        rezervarenoua = creeazarezervare(
            getId(rezervare),
            getnume(rezervare),
            getclasa(rezervare),
            getpret(rezervare),
            getcheckin(rezervare),
        )
        if getclasa(rezervarenoua) == 'economy plus' and getpret(rezervarenoua) > maxi:
            maxi = rezervarenoua['pret']
    return maxi

def cerinta6business(lista):
    '''
        determina cel mai mare pret de la clasa business
        :param lista: lista de rezervari
        :return: maxi
        '''
    maxi = 0
    for rezervare in lista:
        rezervarenoua = creeazarezervare(
            getId(rezervare),
            getnume(rezervare),
            getclasa(rezervare),
            getpret(rezervare),
            getcheckin(rezervare),
        )
        if getclasa(rezervarenoua) == 'business' and getpret(rezervarenoua) > maxi:
            maxi = rezervarenoua['pret']
    return maxi