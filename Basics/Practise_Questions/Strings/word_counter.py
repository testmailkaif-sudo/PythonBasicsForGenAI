'''Write a function analyse_text(text) that prints:

Total word count
Total character count (excluding spaces)
Most repeated word (loop manually, no built-ins like Counter)
Whether the text is a palindrome (reads same forwards and backwards)'''


'''analyse_text("hello world hello python hello")
# Words: 5
# Characters (no spaces): 36
# Most repeated: hello (3 times)
# Palindrome: No

analyse_text("madam")
# Words: 1
# Characters (no spaces): 5
# Most repeated: madam (1 time)
# Palindrome: Yes'''
text ="Afifa Vasiq Kaif Kaif Vasiq Kaif"
def analyse_text(text):
    text_sp = text.split()
    print("Words = ",len(text_sp))
    counter = 0
    for i in text_sp:
        for j in range (len(i)):
            counter+=1
    print("Characters = ",counter)
    text.lower()
    if text == text[::-1]:
        print("Palindrome = Yes")
    else:
        print("Palindrome = No")
    max_count =0
    for i in set(text_sp):
        count = text_sp.count(i)
        if count > max_count:
            max_count = count
            most_repeated = i
    print("Most Repeated :",most_repeated,"(",max_count," times)")

analyse_text(text)