def get_integers(list_group):
    new_list = []
    non_integer = []
    for i in range(len(list_group)):
        if type(list_group[i]) == int:
            new_list.append(list_group[i])
        else:
            non_integer.append(list_group[i])
    return new_list


print(get_integers(["book", 1, "Peter", "Mark", 2, 5, "Funky"]))
