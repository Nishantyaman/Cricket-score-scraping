import requests
from datetime import datetime
import time

from collections import defaultdict

res=requests.get("https://www.cricbuzz.com/match-api/20239/commentary.json")
data = res.json()

match_dict=defaultdict(dict)

teams = ['team1','team2']

venue_details = data.get('venue')
score_dict = data.get('score')

match_dict['toss'] = data.get('toss')
match_dict['score'] = score_dict.get('batting').get('score')
match_dict['crr'] = score_dict.get('crr')

whos_batting_id = score_dict.get('batting').get('id')

for team in teams:
	team_detail = data.get(team)
	match_dict[team]['id'] = team_detail.get('id') 
	match_dict[team]['name'] = team_detail.get('name')

	if(match_dict[team]['id']==whos_batting_id):
		match_dict['batting'] = match_dict[team]['name']

print(match_dict['team1']['name'],"vs",match_dict['team2']['name'])
print()
print(match_dict['batting'],"is batting")
print("{}:{}".format("Score",match_dict['score']))
print("{}:{}".format("Run rate",match_dict['crr']))