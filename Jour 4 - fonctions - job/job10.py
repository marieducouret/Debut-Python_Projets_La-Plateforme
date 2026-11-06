def is_odd(x):
    if x >= 0 :
        if x % 2 == 0 :
            print("Pair")
        else : 
            print("Impair")

    else :
        print("Erreur")

is_odd(13)


def is_odd():
    x=int(input("Ecris un nombre : "))
    if x >= 0 :
        if x % 2 == 0 :
            print("Pair")
        else : 
            print("Impair")

    else :
        print("Erreur")

is_odd()