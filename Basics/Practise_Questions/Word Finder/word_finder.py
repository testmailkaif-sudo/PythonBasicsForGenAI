'''Unique Word Finder 🔤
(Set + List + String + Functions + Loops)
Write a function word_analysis(text1, text2) that:

Finds words only in text1 (not in text2)
Finds words only in text2 (not in text1)
Finds words common to both
Finds all unique words across both

word_analysis(
    "python is great and python is fun",
    "java is great and java is popular"
)
# Only in text1: {'python', 'fun'}
# Only in text2: {'java', 'popular'}
# Common: {'is', 'great', 'and'}
# All unique: {'python','java','is','great','and','fun','popular'}
'''
def word_analysis(text1,text2):
    only_1 = []
    only_2 = []
    common = set()
    text1=set(text1.split())
    text2=set(text2.split())
    for i in text1:
        if i in text2:
            common.add(i)
        else:
            only_1.append(i)
    for i in text2:
        if i in text1:
            common.add(i)
        else:
            only_2.append(i)
    only_1=list(only_1)
    only_2 = list(only_2)
    common = list(common)
    print("Only in text 1 is ",only_1)
    print("Only in text 2 is ",only_2)
    print("Common is ",common)
word_analysis(
    "python is great and python is fun",
    "java is great and java is popular"
)