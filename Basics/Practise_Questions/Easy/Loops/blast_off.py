''' Using a while loop, print a countdown from 10 to 1, then print "Blast off!".'''

def blast_off(num):
    while num >0:
        print(num)
        num = num-1
    print("Blast Off")
blast_off(10)