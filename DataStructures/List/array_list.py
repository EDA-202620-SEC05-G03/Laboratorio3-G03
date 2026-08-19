def new_list():
    new_list = {
        'elements': [],
        'size': 0,
    }
    return new_list
#hola
def add_first (lista, valor):
    lista["elements"].insert(0,valor)
    size = len(lista["elements"]) 
    size += 1
    return lista
    
def add_last (lista, valor):
    lista["elements"].append(valor)
    size = len(lista["elements"]) 
    size += 1
    return lista

def first_element (lista):
    if lista["elements"][0] != None:
        primera=lista["elements"][0]
        return primera
    else:
        return None


def last_element (lista):
    if len(lista["elements"]) > 0:
        ultimo=lista["elements"][-1]
        return ultimo
    else:
        return None

def size (lista):
    return len(lista["elements"])
