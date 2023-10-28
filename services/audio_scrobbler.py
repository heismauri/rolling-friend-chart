import requests


import globals as gb


LAST_FM_ENDPOINT = 'http://ws.audioscrobbler.com/2.0/'


def get_user_top_tracks(user, period='7day', limit=1000):
    last_fm_params = {
        # Available methods:
        # user.gettoptracks, user.gettopalbums, user.gettopartists
        'method': 'user.gettoptracks',
        'user': user,
        # Available periods: overall, 7day, 1month, 3month, 6month, 12month
        'period': period,
        # Available limits: 1 to 1000
        'limit': limit,
        'api_key': gb.API_KEY,
        'format': 'json'
    }
    last_fm_response = requests.get(LAST_FM_ENDPOINT, params=last_fm_params)
    return last_fm_response.json()
