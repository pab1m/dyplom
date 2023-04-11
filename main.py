import os

import match as match
import requests
import valorant

api_key = "RGAPI-6622d638-c0ef-4fc3-b913-36b2e588f7cb"


client = valorant.Client(api_key, locale=None)
# client = valorant.Client(api_key, locale=None)

account = client.get_user_by_name("Pab1m#1606")

matches = account.matchlist().history.find(queueId="competitive")
matches = matches.get()

print(matches.teams)



# match = account.matchlist().history.find(queueId="competitive")
# match = match.get()
# for team in match.teams:
#     print(f"{team.teamId} Team's Ranks: ")
#
#     players = match.players.get_all(teamId=team.teamId)
#
#     for player in players:
#         print(f"\t{player.gameName} - {player.rank}")




# skins = client.get_skins()
#
# name = []
#
# pages = client.get_leaderboard(size=50)
#
# print(pages.players[1].gameName)




# for i in act:
#     print(i)
# print(acts)
# print(act)



# account = client.get_user_by_name(name='Pab1m#1606', route='europe')

# match = account.matchlist().history.find(queueId="competitive")
# matchs = account.matchlist()



# lb = client.get_leaderboard(size=100)
# res = lb.players.get_all(numberOfWins=89)
# for name in res:
#     print(f"{name.gameName}, {name.rankedRating}")



# name = input("Search a Valorant Skin Collection: ")
# results = skins.find_all(name=lambda x: name.lower() in x.lower())
# print("\nResults: ")
# for skin in results:
#     print(f"\t{skin.name.ljust(50)} {skin.localizedNames['ru-RU']}")


