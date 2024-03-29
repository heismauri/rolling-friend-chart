import requests


import globals as gb


LAST_FM_ENDPOINT = 'http://ws.audioscrobbler.com/2.0/'


def get_user_top_items(method, user, period, limit=1000):
    last_fm_params = {
        # Available methods:
        # user.gettoptracks, user.gettopalbums, user.gettopartists
        'method': f"user.{method}",
        'user': user,
        # Available periods: 7day, 1month, 3month, 6month, 12month, overall
        'period': period,
        # Available limits: 1 to 1000
        'limit': limit,
        'api_key': gb.API_KEY,
        'format': 'json'
    }
    last_fm_response = requests.get(LAST_FM_ENDPOINT, params=last_fm_params)
    return last_fm_response.json()
