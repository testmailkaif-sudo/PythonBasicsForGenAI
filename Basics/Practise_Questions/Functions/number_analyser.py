

def num_analyser(list_num):
    sum_num = 0
    list_num.sort()
    for i in list_num:
        sum_num+=i
    print("Sum = ",sum_num)
    print("Largest = ",list_num[-1])
    count_even=0
    count_odd = 0
    for i in list_num:
        if i % 2 !=0:
            count_odd +=1
        else:
            count_even +=1
    print("Even Count = ", count_even)
    print("Odd Count = ",count_odd)

num_analyser([4, 7, 2, 9, 11, 6, 3])