''' Print all even numbers between 1 and 20 using range().'''

def even_numbers(num_range):
    print("The even Numbers are : ")
    for i in range(1,num_range+1):
        if i %2 == 0:
            print(i)
even_numbers(int(input("Enter the range : ")))
