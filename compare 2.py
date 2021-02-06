


def compare():
    x = input("What is the number you would like to be your X?")
    y = input("What is the number you want to be your Y?")
    z = input("What is the number you want to be your Z? ")
    if x <= y:
        if y <= z:
            return True
        else:
            return False
    else:
        return False
compare()

