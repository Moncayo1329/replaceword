def replace_word():
    str_to_modify = "Hi guys, I am Michael and Hi hi hi hi"
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word to replacement: ")
    modified_str = str_to_modify.replace(word_to_replace, word_replacement)
    print(modified_str)

replace_word()
