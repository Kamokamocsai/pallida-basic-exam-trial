dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'

hun_word = input("HUN word: ")
eng_word = input("ENG word: ")

def add_word(hun_word, eng_word):
    new_word = {hun_word: eng_word}
    dictionary.append(new_word)
    print(dictionary)
    

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


# def translate_to_hun(eng_word):
#     new_word = {hun_word: eng_word}
#     for i in dictionary:
#         if new_word in dictionary:
#             solution = dictionary(i)
#             print(solution)
#         else:
#             False


# def translate_to_eng(hun_word):
#     pass

# translate_to_hun(eng_word)

# check_words(hun_word, eng_word)

add_word(hun_word, eng_word)