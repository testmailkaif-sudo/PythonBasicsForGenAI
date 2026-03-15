'''Find all prime numbers between 1 and 50 using nested loops.
(A prime number is divisible only by 1 and itself)'''
target =int(input("Enter the number : "))
prime_numbers = []
for num in range (2,target):
    is_prime = True
    for i in range(2,num):
        if num %i ==0:
            is_prime = False
            break
    if is_prime == True:
        prime_numbers.append(num)

print(prime_numbers)