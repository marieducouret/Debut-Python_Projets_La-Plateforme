L = ["Antoine", "Alexandre", "Evan"]
X = ["Dorine", "Marie", "Emeline"]
Y = ["Yves", "Marius", "Paul"]

P = [L, X, Y]

# for i in P :
#         for j in i :
#             print(j)

i=0
j=0
while i < len(P) :
    while j < len(P) :
        print(j)
        j+=1
    i+=1