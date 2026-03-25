name = "Mohammad Kaif Shaik Podile  "
print(name.upper()) # returns all in caplital letters
print(name.lower())  # returns all in lower case letters
print(name.capitalize()) # only first letter in caps
print(name.title()) # first letter od every word will be capitalized
print(name.swapcase()) # turns lower into upper and upper into lower
name = "    Mohammad Kaif Shaik Podile  "
print(name)
print(name.strip())
print(name.lstrip())
print(name.rstrip())


text = "I love Python and Python loves me"
print(text.find("Python"))
print(text.count("Python"))
print(text.replace("Python","Java"))

print(text.split())
words = ["Hello","World","I","love","Python"]
print(" ".join(words))
text = "Python"

print(len(text))        # 6    ← length
print(min(text))        # P    ← smallest character (alphabetically)
print(max(text))        # y    ← largest character
print(sorted(text))     # ['P', 'h', 'n', 'o', 't', 'y']
print(list(text))       # ['P', 'y', 't', 'h', 'o', 'n']

