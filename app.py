import constants
import sys
import pdb
Panthers = []
Bandits = []
Warriors = []

def cleaned_data():
        fixed = {}
        for player in constants.PLAYERS:
            fixed['name'] = player['name']
            fixed['guardians'] = player['guardians']
            if player['experience'] == 'YES':
                fixed['experience'] = True
            else:
                fixed['experience'] = False
            fixed['height'] = player['height'].split(" ")[0]
        return fixed

def balance_teams():
    length = len(constants.PLAYERS)
    teamSize = length/3

    for player in constants.PLAYERS:
        if len(Panthers) < teamSize:
            Panthers.append(player)

        elif len(Bandits) < teamSize:
            Bandits.append(player)
        else:
            Warriors.append(player)
    

def display_stats():
    print("BASKETBALL TEAM STATS TOOL")
    print("---- MENU----")
    print("Here are your choices:")
    print("A) Display Team Stats")
    print("B) Quit")
    pdb.set_trace()
    try:
        
        option = input("Enter option: \n")
        if option == 'b' or 'B':
            exit()
        elif option == 'a' or 'A':

            teamName = int(input('''For the Panthers press 1, for the Bandits press 2,
and for the Warriors press 3\n'''))
        

    except:
        print("Invalid Response")
        exit()

    displayList =[]
    match teamName:
        case 1:
            print("\nPanthers")
            print("Team size: {}".format(len(Panthers)))

            for player in Panthers:
                for key, val in player.items():
                    if key == 'name':
                        displayList.append(val)
            print(*displayList, sep = ", ")
            print()
        case 2:
            print("\nBandits")
            print("Team size: {}".format(len(Bandits)))

            for player in Bandits:
                for key, val in player.items():
                    if key == 'name':
                        displayList.append(val)
            print(*displayList, sep=", ")
            print()
        case 3:
            print("\nWarriors")
            print("Team size: {}".format(len(Warriors)))

            for player in Warriors:
                for key, val in player.items():
                    if key == 'name':
                        displayList.append(val)
            print(*displayList, sep = ", ")
            print()
        case _:
            print("INVALID RESPONSE")




        
if __name__ == '__main__':
    cleaned_data()
    balance_teams()
    display_stats()
