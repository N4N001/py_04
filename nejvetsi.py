def nejvetsi():
    nejvetsi=[int(x) for x in input("Zadejte čísla oddělená čárkou: ").split(",")]
    print(max(nejvetsi))
nejvetsi()
input("Stiskni klávesu ENTER pro ukončení programu")