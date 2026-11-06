n = input("Quel est ton prénom?")

if n == "Alex" :
    print("Bonjour", n)
elif n == "Lydie" :
    print("Coucou", n)
elif n == "Antoine" :
    print("Salut", n)
else :
    print("Qui es-tu?")




match n :
    case "Alex" :
        print("Bonjour", n)
    case "Lydie" :
        print("Coucou", n)
    case "Antoine" :
        print("Salut", n)
    case _:
        print("Qui es-tu?")




if n == "Alex" or n == "Lydie" or n == "Antoine" :
    print("Bonjour", n)
else :
    print("Qui es-tu?")

match n :
    case "Alex" | "Lydie" | "Antoine" :
        print("Salut", n)
    case _:
        print("Qui es-tu?")



n = "Marie"

if n == "Marie" : 
    print("Bonjour")