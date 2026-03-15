''' Using only loops and basic operators (no built-in functions like reverse, sort), reverse a string:'''

text = "Python"
text_l = list(text)
for i in range(1,len(text)+1):
    print(text_l[-i],end="")