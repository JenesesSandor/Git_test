

def összead(number1, number2):
    return (number1 + number2)



def kivonás(number1, number2):
    return number1 - number2

def szorzás(a, b):
    return a *b


def osztás(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Nullával nem lehetséges az osztás")



