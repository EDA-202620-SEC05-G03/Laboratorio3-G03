def new_list():
    new_list = {
        'elements': [],
        'size': 0,
    }
    return new_list

def add_first (my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list
    
def add_last (my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def first_element (my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["elements"][0]


def last_element (my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["elements"][-1]

def size (my_list):
    return my_list["size"]

def get_element(my_list, pos):
    if 0 <= pos and pos < my_list["size"]:
        return my_list["elements"][pos]
    else:
        raise Exception('IndexError: list index out of range')
 

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def is_empty(my_list):
    return my_list["size"] == 0

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem = my_list["elements"].pop(0)
        my_list["size"] -= 1
    return elem

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem = my_list["elements"].pop(-1)
        my_list["size"] -= 1
    return elem

def delete_element(my_list, pos):
    if 0 <= pos and pos < my_list["size"]:
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if 0 <= pos and pos < size(my_list):
        my_list["elements"][pos] = new_info
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def exchange(my_list, pos_1, pos_2):
    if (0 <= pos_1 and pos_1 < size(my_list)) and (0 <= pos_2 and pos_2 < size(my_list)):
        elem_1 = my_list["elements"][pos_1] 
        elem_2 = my_list["elements"][pos_2]
        my_list["elements"][pos_1] = elem_2
        my_list["elements"][pos_2] = elem_1
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if 0 <= pos_i and pos_i < size(my_list):
        nueva_lista = new_list()
        for i in range(pos_i, pos_i + num_elements):
            elem = my_list["elements"][i]
            nueva_lista = add_last(nueva_lista, elem)
    else:
        raise Exception('IndexError: list index out of range')
    return nueva_lista