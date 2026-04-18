#Set is an unorderd collection of data with no duplicates
#Best for removing duplicates and menbership testing

fruits = {"apple","kiwi","mango","avacado","banana","orange", "apple"}
print(fruits)
print(type(fruits))

#Methods in set
fruits.add("keera")
print(fruits)
fruits.update(["potato","carrot"])
print(fruits)
fruits.remove("carrot")
print(fruits)
fruits.discard("carrot")
print(fruits)
sel=fruits.copy()
fruits.clear()
print(fruits)


#Set Operations

set1 = {1,2,3,4,5,6,7}
set2 = {6,7,8,9,10}
#union
print(set1 | set2)
#intersection
print(set1 & set2)