
for n in range(1,101) :
    if n == 26 or n == 37 or n == 88 :
        print("-")
    else : 
        print(n)

for n in range(1,101) :
    if n not in {26, 37,88} :
        print(n)

