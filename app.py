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
def balance_teams(players):
    playersPerTeam = len(players)/len(teams)
    print(len(teams))
    playerNo =1
    listPointer = -1
    listNeeded = [] * len(teams)
    print(listNeeded)

    for player in players:
        listPointer+=1
        while playerNo < playersPerTeam:
            listNeeded[listPointer].append(player)
            playerNo+=1
    print(listNeeded)

    
    
    
    
        
            

            


        
if __name__ == '__main__':
    cleaned_players = cleaned_data()
    balance_teams(cleaned_players)    


    
    # display_stats()
