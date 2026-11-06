n=int(input("Entrez un entier supérieur à 0 : "))

for i in range(0, n+1):
    print("La table de multiplication de ", i)
    for j in range (0, 11):
        print(f"{j} x {i} = ", j*i)
    print("---------------")
