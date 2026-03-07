'''The enumerate function is used to get both index and value while looping '''


fruits = ["apple","bananna","gauva","Orange","Mango"]
addep=[]
for i in enumerate(fruits):
    print(i)
    addep.append(i)
for index,fruit in enumerate(fruits):
    print(index,fruit)
print(addep)