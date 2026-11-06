def language():
    x=input("Quel language préfèes-tu: Javascript, Python, Java, React Native, autre ?")
    print(x)

    match x :
        case "Javascript" :
            print("Tu es un développeur Web.")
        case "Python" :
            print("Tu es un développeur IA.")
        case "Java" :
            print("Tu es un développeur Logiciel.")
        case "React Native" :
            print("Tu es un développeur Mobile.")
        case _ :
            print("Un jour, je serai le meilleur développeur…")
        
language()




def language(x):
    match x :
        case "Javascript" :
            print("Tu es un développeur Web.")
        case "Python" :
            print("Tu es un développeur IA.")
        case "Java" :
            print("Tu es un développeur Logiciel.")
        case "React Native" :
            print("Tu es un développeur Mobile.")
        case _:
            print("Un jour, je serai le meilleur développeur…")
        
language("Python")