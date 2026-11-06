a = int(input("Entre une longueur a : "))
b = int(input("Entre une longueur b : "))
c = int(input("Entre une longueur c : "))

#Un triangle est constructible si la longueur du plus grand côté est strictement inférieure à la somme des longueurs des deux autres côtés
if a + b > c and a + c > b and b + c > a:
    print("Le triangle est constructible")
else : 
    print("Le triangle n'est pas constructible")

if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2 :
    print("Le triangle est rectangle")
elif a == b and a == c and b == c :
    print("Le triangle est equilatèral")
elif a != b and a != c and b == c or a != b and a == c and b != c or a == b and a != c and b != c :
    print("Le triangle est isocèle")
# elif a != b and a != c and b != c :
#     print("Le triangle est quelconque")
else : 
    print("Le triangle est quelconque")

