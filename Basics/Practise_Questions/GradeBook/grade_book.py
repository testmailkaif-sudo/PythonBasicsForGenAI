book = {}

def add_student(book, name, *marks):
    book[name] = list(marks)
    return book

def get_average(book, name):
    avg = 0
    for i in book.get(name):
        avg += i
    return avg/len(book[name])
def top_student(book):
    top_name = None
    high_avg = 0
    avg=0
    for name in book:
        marks = book[name]
        avg = sum(marks)/len(marks)

        if avg >high_avg:
            high_avg = avg
            top_name = name
    return top_name
add_student(book,"kaif",90,10)
add_student(book,"kaif1",10,10)
add_student(book,"hussain",90,90,10)
print(get_average(book, "kaif"))
print(top_student(book))