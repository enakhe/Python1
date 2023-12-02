def character(word):
    return_string = []
    for letter in word:
        return_string.append(letter + letter)
    return "".join(return_string)


user_input = input("Enter in word to be traversed: ")
print(character(user_input))
