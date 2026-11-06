
for n in range (2, 50) :
    for i in range(2, n) : 
        if n % 1 == 0 and n % n == 0 and n % i == 0 :
            print(n)
