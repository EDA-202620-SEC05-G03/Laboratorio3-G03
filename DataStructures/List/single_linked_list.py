def new_list():
    new_list = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return new_list

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count

def is_empty(my_list):
    return my_list["size"] == 0

def add_first(my_list, element):
    my_list["first"] = {"info": element, "next": my_list["first"]}
    if my_list["size"] == 0:
        my_list["last"] = my_list["first"]
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    new_node = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = new_node
    else:
        my_list["last"]["next"] = new_node
    my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]["info"]

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]["info"]
    
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem = my_list["first"]["info"]
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        if my_list["size"] == 0:
            my_list["last"] = None
        return elem
    
def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem = my_list["last"]["info"]
        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
        else:
            node = my_list["first"]
            for i in range(my_list["size"]-2):
                node = node["next"]
            node["next"] = None
            my_list["last"] = node
        my_list["size"] -= 1
    return elem

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        if pos == 0:
            my_list = add_first(my_list, element)
        elif pos == size(my_list):
           my_list = add_last(my_list, element)
        else:
            new_node = {'info': element, 'next': None}
            node = my_list["first"]
            for i in range(pos-1):
                node = node["next"]
            new_node["next"] = node["next"]
            node["next"] = new_node
            my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        if pos == 0:
            remove_first(my_list)
        elif pos == size(my_list) - 1:
            remove_last(my_list)
        else:
            actual = my_list["first"]
            for i in range(1, pos):
                actual = actual["next"]
            actual["next"] = actual["next"]["next"]
            my_list["size"] -= 1
        return my_list
    
def change_info (my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise IndexError('list index out of range')
    else:
        node = my_list["first"]
        for i in range(pos):
            node = node["next"]
        node["info"] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise IndexError('list index out of range')
    else:
        node_1 = my_list["first"]
        for i in range(pos_1):
            node_1 = node_1["next"]
        node_2 = my_list["first"]
        for i in range(pos_2):
            node_2 = node_2["next"]
        node_1["info"], node_2["info"] = node_2["info"], node_1["info"]
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= size(my_list) or num_elements < 0 or pos_i + num_elements > size(my_list):
        raise IndexError('list index out of range')
    else:
        nueva_lista = new_list()
        node = my_list["first"]
        for i in range(pos_i):
            node = node["next"]
        for i in range(num_elements):
            nueva_lista = add_last(nueva_lista, node["info"])
            node = node["next"]
    return nueva_lista