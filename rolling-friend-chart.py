import requests
import json
from itertools import groupby
from operator import itemgetter

#LastFM user list
usersList = []

#Personal LastFM API Key
apiKey = ''

#Empty variable to append each song
dictList = []

#LastFM API
lastfmApi = 'http://ws.audioscrobbler.com/2.0/'
lastfmHeaders = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

#Getting daily, weekly, monthly, yearly chart of each user in the list
n = 0
for user in usersList:
    n = n + 1
    print('Collecting the songs by', user, f'{n}-{len(usersList)}')
    lastfmParams = {
        'method': 'user.gettoptracks', #user.gettoptracks, user.gettopalbums, user.gettopartists
        'user': user,
        'period': '7day', #overall, 7day, 1month, 3month, 6month, 12month 
        'limit': 1000, #1 to 1000
        'api_key': apiKey,
        'format': 'json'
    }
    lastfmResp = requests.get(lastfmApi, params = lastfmParams, headers = lastfmHeaders).text
    lastfmJson = json.loads(lastfmResp)
    mainkey = list(lastfmJson.keys())[0]
    childkey = list(lastfmJson[mainkey].keys())
    childkey.sort()
    #Cheking if the user has been using LastFM for the period specified in lastfmParams
    if lastfmJson[mainkey]['@attr']['total'] != '0':
        for j in lastfmJson[mainkey][childkey[1]]:
            if mainkey == 'topartists':
                name = j['name']
            else:
                #Combining each song with its artist to create a more complete 'name' tag, it only works for albums and tracks
                name = j['name'] + ' - ' + j['artist']['name']
            #It creates a new dictionary to make the count easier
            key = {'name': name, 'playcount': int(j['playcount'])}
            dictList.append(key)

#Grouping each track and adding them, more like combining
get_name = itemgetter('name')
dictList = [{'name': name, 'playcount': sum(d['playcount'] for d in dicts)} for name, dicts in groupby(sorted(dictList, key=get_name), key=get_name)]

#Sorting each song by its playcount
def get_playcount(track):
    return track.get('playcount')
dictList.sort(key=get_playcount, reverse=True)

#Printing the top 10
n = 0
for s in dictList:
    if n < 10:
        n = n + 1
        print('#' + str(n), s['name'], '[' + str(s['playcount']) + ']')
    else:
        break