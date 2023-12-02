def vowel_counter(word) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0

    for v in vowels:
        for letter in word:
            if letter.lower() == v.lower():
                counter += 1
    return f"There are {counter} vowels in the word '{word}'"


user_input = input("Enter a word to count the number of vowels: ")
print(vowel_counter(user_input))
