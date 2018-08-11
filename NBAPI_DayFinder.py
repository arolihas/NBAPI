from nba_py import Scoreboard
from nba_py import game

print("Welcome to NBAPI: DayFinder. Enter a date in DD/MM/YYYY format and get the top stat leader that day.")
loopcondition = True
while loopcondition:
	try:
		#Selects day to find games
		month = int(input("Enter month: "))
		day = int(input("Enter day: "))
		year = int(input("Enter year: "))
		loopcondition = False
	except:
		print("Pick a calendar day in DD/MM/YYYY format please")
		loopcondition = True

	try:
		#Pulls games on day entered
		gamelist = Scoreboard(month,day,year,'00',0).available()
		loopcondition = False
		#No games, try again
		if(len(gamelist) == 0):
			print("No games on that day, pick another one")
			loopcondition = True
	except: 
		print("No games on that day, pick another one")
		loopcondition = True

#Enter desired stat
loopconditionStat = True
while loopconditionStat:
	value = input("Select a stat (MIN,REB,AST,OREB,DREB,PTS,PLUS_MINUS,STL,BLK,FG3M,FGM): ")
	if (value not in ["MIN","REB","AST","OREB","DREB","PTS","PLUS_MINUS","STL","BLK","FG3M","FGM"]):
		print("Pick a real stat")
		loopconditionStat = True
	else:
		loopconditionStat = False

print("Searching...")
#Retrieves boxscores for each game
boxScores = []
for i in range(len(gamelist['GAME_ID'])):
    boxScores.append(game.Boxscore(gamelist['GAME_ID'][i]).player_stats())


maxVal = 0 
player = '' 
for bx in range(len(boxScores)): 
    for vals in range(len(boxScores[bx])): 
        if boxScores[bx][value][vals] > maxVal: 
            maxVal = boxScores[bx][value][vals] 
            player = boxScores[bx]['PLAYER_NAME'][vals] 
#index of stat leader shared by values and player

#naming convention
if value == 'MIN': valuelabel = "most minutes"
elif value == 'REB': valuelabel = "most rebounds"
elif value == 'AST': valuelabel = "most assists"
elif value == 'OREB': valuelabel = "most offensive rebounds"
elif value == 'DREB': valuelabel = "most defensive rebounds"
elif value == 'PTS': valuelabel = "most points"
elif value == 'PLUS_MINUS': valuelabel = "highest plus/minus"
elif value == 'STL': valuelabel = "most steals"
elif value == 'BLK': valuelabel = "most blocks"
elif value == 'FG3M': valuelabel = "most 3 pointers made"
elif value == 'FGM': valuelabel = "most field goals"
print "On {}/{}/{}, {} had the {} with {} {}".format(month,day,year,player,valuelabel,max,value)
