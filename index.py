import system
import main_character


print("Welcome to the Arena of the Archi. World's gratest arena in this land")
print("You want to enter?")


system.test("WItamy")

player1 = main_character.MainCh("Stolas")
player1.note()

while True:
    try:
        weapon = int(input("Wpisz bron: "))
        print(system.attack(weapon))
    except ValueError:
        print("Podaj liczbę")






#    if input() == "Y" or "y":
#        print("You've enter to the arena")
#   else:
#        print("You've come back to City")