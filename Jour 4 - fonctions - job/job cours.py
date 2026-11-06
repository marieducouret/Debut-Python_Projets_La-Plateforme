#Définir une fonction sans paramètres
def addition():
    x=int(input("Choisis un nombre :"))
    print(x * 10)

addition()

#Définir une fonction avec paramètres
def addition(a, b):
    print("Le premier nombre est ",a)
    print("Le deuxième nombre est ", b)
    x=a * b
    print("La multiplication de", a, "et", b, "est", x)

addition(3, 6)


#Définir une fonction avec une valeur en retour
def addition(a, b):
    x=a * b
    return x
resultat=addition(3, 10)
print(resultat)