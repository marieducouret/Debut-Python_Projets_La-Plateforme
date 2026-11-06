nom="lunettes de vue"
prix_unitaire=75
quantite_en_stock=150

print("Inventaire de")
print(f"Produits		: {nom}")
print(f"le prix unitaire est de	: {prix_unitaire}€")
print(f"La quantité est de	: {quantite_en_stock}")

quantite_commandee=int(input("Quantité a commandé : "))

new_quantite_en_stock=quantite_en_stock+quantite_commandee
print(f"La nouvelle quantité en stock après commande est de {new_quantite_en_stock}")

inflation=input("Une inflation sur le produit a-t-elle été constatée? : ")
tx_inflation=int(input("De combien est l'inflation?"))
prix_futur=(((prix_unitaire*tx_inflation)/100)+prix_unitaire)
print(f"Le prix après inflation est de {prix_futur}")
print("Inventaire final")
print(f"Produits		: {nom}")
print(f"le prix unitaire est de	: {prix_futur}€")
print(f"La quantité est de	: {new_quantite_en_stock}")
valeur_du_stock1=prix_futur*new_quantite_en_stock
print(f"Valeur total du stock : {valeur_du_stock1}€")
