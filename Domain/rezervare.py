def creeazarezervare(id , nume , clasa , pret , checkin):
    '''
    creeaza o rezervare
    :param ID: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :return: un dictionar ce retine o rezervare
    '''
    tuplu = (id , nume , clasa , pret , checkin)
    return tuplu


def getId(tuplu):
    '''
    ia id-ul rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: id-ul prajiturii
    '''
    return tuplu[0]

def getnume(tuplu):
    '''
    ia numele din rezervare
    :param rezervare: dictionar de tipul rezervare
    :return: numele din rezervare
    '''
    return tuplu[1]

def getclasa(tuplu):
    '''
    ia clasa rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: clasa rezervarii
    '''
    return tuplu[2]

def getpret(tuplu):
    '''
    ia pretul din rezervare
    :param rezervare: dictionar de tipul rezervare
    :return: pretul din rezervare
    '''
    return tuplu[3]

def getcheckin(tuplu):
    '''
    ia checkin ul rezervarii
    :param rezervare: dictionar de tipul rezervare
    :return: checkin ul rezervarii
    '''
    return tuplu[4]

def toString(tuplu):
    return 'id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}'.format(
        getId(tuplu) ,
        getnume(tuplu) ,
        getclasa(tuplu) ,
        getpret(tuplu) ,
        getcheckin(tuplu)
    )