n = int(input("Jusqu'à quel nombre souhaites-tu les tables de multiplication ? "))
print(f"Tables de multiplication de 1 à {n}")

for i in range(1, n + 1):
    print(f"Table de multiplication de {i}:")
    for j in range (1, 11):
        print(f"{j} x {i} = {j * i}")

        
