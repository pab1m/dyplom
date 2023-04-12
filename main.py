import os

import requests
import valorant

api_key = "RGAPI-e8ae929f-0c27-49f6-905e-89cd76cfd5ac"


client = valorant.Client(api_key,  locale="en-US")
# client = valorant.Client(api_key, locale=None)

# account = client.get_user_by_name("Pab1m#1606")
#
# matches = account.matchlist().history.find(queueId="competitive")
# matches = matches.get()
#
# print(matches.teams)



# match = account.matchlist().history.find(queueId="competitive")
# match = match.get()
# for team in match.teams:
#     print(f"{team.teamId} Team's Ranks: ")
#
#     players = match.players.get_all(teamId=team.teamId)
#
#     for player in players:
#         print(f"\t{player.gameName} - {player.rank}")




skins = client.get_skins()



pages = client.get_leaderboard(size=50)

print(pages.players[0].gameName)




# for i in act:
#     print(i)
# print(acts)
# print(act)



account = client.get_user_by_name(name='Pab1m#1606')

match = account.matchlist().history.find(queueId="competitive")
print(match)

# if match == None:
#     print("No Ranked match in recent history!")
#     exit(1)
# else:
#     match = match.get()


# for team in match.teams:
#     print(f"{team.teamId} Team's Ranks: ")
#
#     # Find all the players on the same team.
#     players = match.players.get_all(teamId=team.teamId)
#
#     for player in players:
#         print(f"\t{player.gameName} - {player.rank}")



# lb = client.get_leaderboard(size=100)
# res = lb.players.get_all(numberOfWins=89)
# for name in res:
#     print(f"{name.gameName}, {name.rankedRating}")


# name = input("Search a Valorant Skin Collection: ")
# results = skins.find_all(name=lambda x: name.lower() in x.lower())
# print("\nResults: ")
# for skin in results:
#     print(f"\t{skin.name.ljust(50)} {skin.localizedNames['ru-RU']}")


