def sort_number(list_number, order):
    if order == "asc":
        for x in range(len(list_number)):
            for j in range(len(list_number) - x - 1):
                if list_number[j] > list_number[j + 1]:
                    list_number[j], list_number[j + 1] = list_number[j + 1], list_number[j]

    if order == "dsc":
        for x in range(len(list_number)):
            for j in range(len(list_number) - x - 1):
                if list_number[j] < list_number[j + 1]:
                    list_number[j + 1], list_number[j] = list_number[j], list_number[j + 1]

    if order == "none":
        return list_number

    return list_number


max_number = input("How many numbers do you want to sort? ")
print("Please enter the numbers")
list_number_input = []
for i in range(int(max_number)):
    number = int(input())
    list_number_input.append(number)
user_input = input("Enter order e.g asc, dsc, none: ")
print(sort_number(list_number_input, user_input))
