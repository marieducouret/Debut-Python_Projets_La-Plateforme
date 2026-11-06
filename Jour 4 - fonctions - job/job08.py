def what_to_eat(type, season):
    if type == "fruits" and season == "hiver" :
        print("orange, mandarine et kiwi")
    elif type == "fruits" and season == "été" :
        print("Poire, fraise, cassis")
    elif type == "légumes" and season == "hiver" :
        print("carotte, topinambour, endive")
    elif type == "légumes" and season == "été" :
        print("artichaut, aubergine,navet")

what_to_eat("légumes", "été")