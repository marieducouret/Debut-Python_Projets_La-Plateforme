def average():
    moy1 = int(input("Quelle est ta moyenne en français? "))
    print(moy1)
    moy2 = int(input("Quelle est ta moyenne en mathématiques? "))
    print(moy2)
    moy3 = int(input("Quelle est ta moyenne en histoire-géographie? "))
    print(moy3)
    moyenne_etudiant=(moy1+moy2+moy3)/3

    if moyenne_etudiant >= 15 :
        print("Très bon élève")
    elif moyenne_etudiant <= 14 and moyenne_etudiant >= 11 :
        print("Bon élève")
    elif moyenne_etudiant <= 10 and moyenne_etudiant >= 8 : 
        print("Elève moyen")
    else :
        print("Eleve devant faire des efforts")

average()




def average(moy1, moy2, moy3):
    moyenne_etudiant=(moy1+moy2+moy3)/3

    if moyenne_etudiant >= 15 :
        print("Très bon élève")
    elif moyenne_etudiant <= 14 and moyenne_etudiant >= 11 :
        print("Bon élève")
    elif moyenne_etudiant <= 10 and moyenne_etudiant >= 8 : 
        print("Elève moyen")
    else :
        print("Eleve devant faire des efforts")

average(14, 15, 19)