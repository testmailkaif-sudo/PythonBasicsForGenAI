fruits = ["apple","mange","banana"]
numbers=[1,2,3,4,5]
alpha_num = ["apple",1,"mango",2,"banana",3]
empty =[]


#Accessing Items
print(fruits[0]) #prints value of start index
print(numbers[1:5]) # prints value from 1st index to 4 index
print(alpha_num[-1]) # prints the value of last index
print(alpha_num[::-1]) #prints reverse of the list

#Modifying a list

fruits[0]="name"
print(fruits,"---------") # modifys the list




#List Methods
list_method = ["apple","kiwi","mango","avacado","banana","orange"]
list_method.append("grapes") # adds the item at the end of the list
list_method.insert(1,"guava") # inserts the item at the desired index
list_method.remove("guava") #removes the item by value
list_method.pop()#removes last item
list_method.pop(3) # removes item by index
list_method.sort() # sorts the list alphabetically
list_method.reverse() # reverses the list
list_method.clear()  #makes the list empty by removing all the items
print(list_method)

list_method = ["apple","kiwi","mango","avacado","banana","orange", "apple"]
print(len(list_method)) # prints the len of the list
print("apple" in list_method) # Returns True if the condition is true
print(list_method.count("apple"))# prints the no.of occurences
print(list_method.index("apple"))

#Looping a list

fruits = ["apple","kiwi","mango","avacado","banana","orange", "apple"]
for i in fruits:
    print(i)
#printing with index
for i,j in enumerate(fruits):
    print(i,j)



#List Comprehension
squares=[i*i for i in range(1,6)]
print(squares)
#list comprehension with condition
even_numbers=[i for i in range(1,11) if i%2 ==0]
print(even_numbers)