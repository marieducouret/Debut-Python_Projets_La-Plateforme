def any_computation():
    num1 = int(input("Donnes moi un premier chiffre ou nombre : "))
    operator = input("Donnes moi le sigle de l'opération que tu souhaites : ")
    num2 = int(input("Donnes moi un deuxième chiffre ou nombre pour ton opération : "))
    x = f"{num1} {operator} {num2}"
    y = eval(x)
    print("Le résultat est ", y)

any_computation()





def any_computation(num1, operator, num2):
    x = f"{num1} {operator} {num2}"
    return eval(x)

print(any_computation(3, "*", 5))