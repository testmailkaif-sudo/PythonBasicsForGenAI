'''Check if the word "python" is inside the string "I love python programming"'''
def str_in_word(string, word):
    if string in word:print(True)
    else:print(False)
str_in_word(str(input("Enter the string :")),str(input("Enter the word :")))