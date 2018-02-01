from nba_py import Scoreboard
from nba_py import game

print("Welcome to NBAPI: DayFinder. Enter a date in DD/MM/YYYY format and get the top stat leader that day.")
loopcondition = True
while loopcondition:
	try:
		#Selects day to find games
		day = input("Enter day: ")
		month = input("Enter month: ")
		year = input("Enter year: ")
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
	value = raw_input("Select a stat (MIN,REB,AST,OREB,DREB,PTS,PLUS_MINUS,STL,BLK,FG3M,FGM): ")
	if (value not in ["MIN","REB","AST","OREB","DREB","PTS","PLUS_MINUS","STL","BLK","FG3M","FGM"]):
		print("Pick a real stat")
		loopconditionStat = True
	else:
		loopconditionStat = False

print("Searching...")
#Retrieves boxscores for each game
boxScores = []
for games in gamelist:
	boxScores.append(game.Boxscore(games['GAME_ID']).player_stats())


values = []
players = []
for gameNumber in range(len(boxScores)):
	for player in range(len(boxScores[gameNumber])):
		#places each player's stats in entry of list
		players.append(boxScores[gameNumber][player]['PLAYER_NAME'])
		#places each player's specific stat desired in same index of a different list
		values.append(boxScores[gameNumber][player][value])
#index of stat leader shared by values and player
index = (values.index(max(values)))

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
print "On {}/{}/{}, {} had the {} with {} {}".format(month,day,year,players[index],valuelabel,max(values),value)
