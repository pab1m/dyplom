import os
import valorant
from riotwatcher import LolWatcher, ApiError
import pandas as pd

api_key = 'RGAPI-e8ae929f-0c27-49f6-905e-89cd76cfd5ac'
watcher = LolWatcher(api_key)
my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'Doublelift')
print(me)

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)