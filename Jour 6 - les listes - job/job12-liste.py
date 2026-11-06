L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

for i in range(len(L)): 
    for j in range(i+1, len(L)): 
        if L[i] > L[j]: 
            L[i], L[j] = L[j], L[i]
        
print(L)
