from Logic.CRUD import adaugaRezervareUndoRedo
from Logic.cerinte import Undo, Redo


def testUndoRedo():
    lista=[]
    undo=[]
    redo=[]
    lista = adaugaRezervareUndoRedo("1", "Ionut", "economy", 100, "da", lista,undo,redo)
    lista = adaugaRezervareUndoRedo("2", "Denis", "economy", 100, "da", lista,undo,redo)
    lista = adaugaRezervareUndoRedo("3", "Robert", "economy", 100, "da", lista, undo, redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '3', 'nume': 'Robert', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = Undo(lista, undo, redo)
    assert lista ==[]
    lista = Undo(lista, undo, redo)
    assert lista is None
    undo=[]
    redo=[]
    lista=[]
    lista = adaugaRezervareUndoRedo("1", "Ionut", "economy", 100, "da", lista,undo,redo)
    lista = adaugaRezervareUndoRedo("2", "Denis", "economy", 100, "da", lista,undo,redo)
    lista = adaugaRezervareUndoRedo("3", "Robert", "economy", 100, "da", lista, undo, redo)
    lista=Redo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '3', 'nume': 'Robert', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = Undo(lista, undo, redo)
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Redo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = Redo(lista, undo, redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '3', 'nume': 'Robert', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)
    lista=adaugaRezervareUndoRedo("4", "Razvan", "economy", 100.00, "da", lista, undo, redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                   {'id': '4', 'nume': 'Razvan', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                     {'id': '4', 'nume': 'Razvan', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = Undo(lista, undo, redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = Undo(lista, undo, redo)
    assert lista == []
    lista=Redo(lista,undo,redo)
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                     {'id': '4', 'nume': 'Razvan', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                     {'id': '4', 'nume': 'Razvan', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]