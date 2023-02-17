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
def balance_teams():
    playersPerTeam = len(players)/len(teams)
    playerNo = 1
    for team in teams:
        print(team)
        for player in players:
            if playerNo < playersPerTeam:
                print(player['name'])
    
    
        
            

            


        
if __name__ == '__main__':
    cleaned_data()
    balance_teams()    


    
    # display_stats()
