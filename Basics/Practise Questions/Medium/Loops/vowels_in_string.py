'''Using a loop, count how many vowels are in a string:'''

vowels ="aeiouAEIOU"
string1 = "Hello World, I love Python"
count = 0
for vowel in string1:
    if vowel in vowels:
        count= count+1
print(count)