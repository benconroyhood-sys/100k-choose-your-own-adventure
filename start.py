"""
from os import system
from rich import print

system("clear||cls")

print("[red on white]Welcome to your first day of Dragon Training![/red on white]")

print("Today you will start your journey as a [bold cyan underline]dragon hunter[/bold cyan underline]. This class will help you learn all of the tricks and treats of training your own dragon pet")
print("")
print("What do you want to do next?")
print("1. Look at the [bold red]dragon pen")
print("2. Introduce yourself to some of the people in your class")

choice = input("Make a choice!:")
if choice == 1:
    print("You are looking at the dragon pen.")
elif choice == "2":
    print("You say, 'Hi, I'm Widget!'")
    print("What do you want to do next?")
    print("1. Look at the people in your class")
"""

title = "The Lighthouse (mystery)"
print()
print(title.title())
print()
print("1. You arrive at an abandoned lighthouse by dusk. The door hangs open and a light flickers above.")
print("Climb the stairs → 2")
print("Check the cellar → 3")
choice = input("Make a choice: ")
if choice == "2":
    print()
    print("2. At the top, a lantern burns beside a note: “Don’t trust the keeper.” Footsteps echo behind you.")
    print("Hide behind the lens → 4")
    print("Confront whoever is coming → 5")
    choice = input("Make a choice: ")
    if choice == "4":
        print()
        print("4. A figure in a raincoat snuffs the lantern, then signals to a boat offshore.")
        print("Follow the figure down the cliff path → 8")
        print("Signal the boat yourself → 9")
        choice = input("Make a choice: ")
        if choice == "8":
            print()
            print("8. The figure hurries along the cliff edge, and you gain on them.")
            print("Call out → 16")
            print("Leap to tackle them → 17")
            choice = input("Make a choice: ")
            if choice == "16":
                print()
                print("16. THE END: Family Secrets. The figure is the keeper’s daughter, who confesses it all to you.")
                print()
            elif choice == "17":
                print()
                print("17. THE END: A Long Swim. You both tumble into the sea, and you wash up in the next town with a great story.")
                print()
        elif choice == "9":
            print()
            print("9. The boat swings toward shore, its lamp blinking a code.")
            print("Flash the code back → 18")
            print("Flash a random pattern → 19")
            choice = input("Make a choice: ")
            if choice == "18":
                print()
                print("18. THE END: Smuggler’s Share. The captain welcomes you aboard and offers a cut. You take it.")
                print()
            elif choice == "19":
                print()
                print("19. THE END: Cold Case. The boat flees and never returns, and the case goes cold.")
                print()
    elif choice == "5":
        print()
        print("5. The keeper appears. “You’re the third detective this year,” he says, holding out a kettle.")
        print("Accept his tea → 10")
        print("Demand the truth → 11")
        choice = input("Make a choice: ")
        if choice == "10":
            print()
            print("10. The tea is warm and strangely sweet.")
            print("Drink it all → 20")
            print("Pour it out when he’s not looking → 21")
            choice = input("Make a choice: ")
            if choice == "20":
                print()
                print("20. THE END: The Vanishing Lighthouse. You wake on the dock, and the lighthouse is gone from the map.")
                print()
            elif choice == "21":
                print()
                print("21. THE END: A Ghost’s Company. You discover the keeper has been dead for decades. You stay for the stories.")
                print()
        elif choice == "11":
            print()
            print("11. The keeper sighs and looks at the sea.")
            print("Press him harder → 22")
            print("Soften your tone → 23")
            choice = input("Make a choice: ")
            if choice == "22":
                print()
                print("22. THE END: Treasure Hunters. He confesses he’s guarding buried treasure, and you split it.")
                print()
            elif choice == "23":
                print()
                print("23. THE END: The Lonely Keeper. He wrote the notes himself because he wanted visitors. You visit every month.")
                print()
elif choice == "3":
    print()
    print("3. The cellar is full of crates stamped with a ship’s name. A hatch in the floor leads to a sea cave.")
    print("Open the hatch → 6")
    print("Examine the crates → 7")
    choice = input("Make a choice: ")
    if choice == "6":
        print()
        print("6. The sea cave floods as the tide rises. A rowboat is tied nearby, and a rocky ledge climbs the wall.")
        print("Take the rowboat → 12")
        print("Climb the ledge → 13")
        choice = input("Make a choice: ")
        if choice == "12":
            print()
            print("12. THE END: Daring Escape. You row to the mainland and hand the coast guard the smugglers’ location.")
            print()
        elif choice == "13":
            print()
            print("13. THE END: Wrong Rescuers. Fishermen pull you from the ledge at dawn. They’re the smugglers.")
            print()
    elif choice == "7":
        print()
        print("7. The crates hold maps and a thick ledger.")
        print("Take the ledger → 14")
        print("Burn the evidence → 15")
        choice = input("Make a choice: ")
        if choice == "14":
            print()
            print("14. THE END: Headline Detective. The ledger names the mayor, and you make the front page.")
            print()
        elif choice == "15":
            print()
            print("15. THE END: Beacon of Flame. The fire climbs the tower and lights the coast for miles. Everyone comes to see.")
            print()
else:
    print()
    print("Invalid choice. Please start over.")
    print()