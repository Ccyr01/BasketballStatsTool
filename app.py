import constants
import sys
import pdb

players = constants.PLAYERS
teams = constants.TEAMS


def cleaned_data():
        cleaned = []
        
        for player in players:
            fixed = {}
            fixed['name'] = player['name']
            fixed['guardians'] = player['guardians']
            if player['experience'] == 'YES':
                fixed['experience'] = True
            else:
                fixed['experience'] = False
            fixed['height'] = int(player['height'].split(" ")[0])
            cleaned.append(fixed)
        return cleaned
#pre: list of dictionaries cleaned version
#post: Create as many lists as their are teams
#       and evenly distribute players to each list
#       List 0 should be team 0 etc... 
def balance_teams(players):
    playersPerTeam = len(players)/len(teams)
    print(len(players))
    print(len(teams))
    
    playerNo =0
    listPointer=0
    n = len(teams)
    listNeeded = [[] for x in range(n)]
    
    print(listNeeded)
    for player in players:
            if len(listNeeded[listPointer]) < playersPerTeam:
                listNeeded[listPointer].append(player)
                playerNo+=1
            else:
                listPointer+=1
                listNeeded[listPointer].append(player)
    return listNeeded
def display_menu(listNeeded):
    listOfPlayersToPrint = []
    print("\n---MENU---\n")
    print('''Below is a number next to each team. 
To find out information on a specific team,
press the number that is shown to the left of it.
    ''')
    for team in teams:
        print("{}: {}".format(teams.index(team),team))
    print("{}: Quit".format(len(teams)))
    try:
        teamSelection = int(input("Select number choice here: \n"))
        if(teamSelection == len(teams)):
            print("quit")
            quit()

        else:
            print(len(teams))
            print("\nTeam Name: {}".format(teams[teamSelection]))
            print("Number of players in team: {}".format(len(listNeeded[teamSelection])))
            for player in listNeeded[teamSelection]:
                listOfPlayersToPrint.append(player['name'])
            print("Players in team:")
            print(', '.join(listOfPlayersToPrint))
            print("\n")
    except:
        print("Invalid Input.")



        
if __name__ == '__main__':
    cleaned_players = cleaned_data()
    
    listNeeded = balance_teams(cleaned_players) 
    display_menu(listNeeded)


    
    # display_stats()
