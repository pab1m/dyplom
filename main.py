import os
import requests
import valorant

api_key = "RGAPI-5ff5e39e-06e5-4439-a39d-29725610291b"

client = valorant.Client(api_key, locale="en-US")

skins = client.get_skins()
agents = client.get_characters()

acts = client.get_acts()

act = acts.get(isActive=True)

account = client.get_user_by_name("Pab1m#1606")

# match = account.matchlist().history.find(queueId="competitive")
match = account.matchlist()

print(match)


lb = client.get_leaderboard(size=100)
# res = lb.players.get_all(numberOfWins=89)
# for name in res:
#     print(f"{name.gameName}, {name.rankedRating}")

# name = input("Search a Valorant Skin Collection: ")
#
# results = skins.find_all(name=lambda x: name.lower() in x.lower())
#
# print("\nResults: ")
# for skin in results:
#     print(f"\t{skin.name.ljust(50)} ({skin.localizedNames['es-ES']})")


