montant_initial=15000
taux_rendement=10

gain_annuel=montant_initial*(1+(taux_rendement/100))
print(f"L'investissement intial de {montant_initial}€, avec un taux de rendement de {taux_rendement}% a permis un gain final de {gain_annuel}")

aug_capital=5000
new_capital=montant_initial+aug_capital
aug_rendement=2
new_rendement=taux_rendement+aug_rendement

print(f"En année N+1 l'investisseur augmente son capital de {aug_capital}€, le capital est alors de {new_capital}€")
print(f"Le rendement augmente également de {aug_rendement}%, il passe alors à {new_rendement}%")
gain_n1=int(new_capital*(1+(new_rendement/100)))
print(f"Le gain à la fin de l'année N+1 est de {gain_n1}€")

reduc_capital=int(gain_n1-(gain_n1*(10/100)))
reduc_rendement=new_rendement-1
print(f"En annee N+2, l'investissuer retire 10% de son capital, son nouveau cpaital est de {reduc_capital}€")
print(f"Le rendement subit cette réduction, et perds 1% de rendement, nous avons donc un rendement de {reduc_rendement}%")
gain_n2=int(reduc_capital*(1+(new_rendement/100)))
print(f"Le gain en N+2, et donc de {gain_n2}€")
