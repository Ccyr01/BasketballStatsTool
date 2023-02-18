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
    print(len(players))
    print(len(teams))
    playerNo =0
    listPointer=0
    n = len(teams)
    listNeeded = [[] for x in range(n)]
    
    print(listNeeded)
    for player in players:
            if len(listNeeded[listPointer]) < playersPerTeam:
                print(len(listNeeded[listPointer]))
                listNeeded[listPointer].append(player)
                playerNo+=1
            else:
                print(len(listNeeded[listPointer]))
                listPointer+=1
                listNeeded[listPointer].append(player)
            
    print(listNeeded)

    
    
    
    
        
            

            


        
if __name__ == '__main__':
    cleaned_players = cleaned_data()
    
    balance_teams(cleaned_players)    


    
    # display_stats()
