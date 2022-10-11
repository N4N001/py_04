cisla=input("Zadejte čísla oddělená čárkou: ")
cisla=cisla.split(",")
cisla=[int(x) for x in cisla]
print(max(cisla))
input("Stiskni klávesu ENTER pro ukončení programu")