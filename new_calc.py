

def összead(number1, number2):
    return number1 + number2



def kivonás(number1, number2):
    return number1 - number2

def szorzás(a, b):
    return a *b


def osztás(number1, number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        print("Nullával nem lehetséges az osztás")
