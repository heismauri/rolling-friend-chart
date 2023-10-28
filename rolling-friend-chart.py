from itertools import groupby
from operator import itemgetter


import globals as gb
from services.audio_scrobbler import get_user_top_tracks


def calculate_points(playcount):
    if playcount == 1:
        return 1

    adjusted_playcount = min(playcount, gb.MAX_PLAYCOUNT)
    total_points = 1
    next_point_amount = 0.5

    for _ in range(2, adjusted_playcount + 1):
        total_points += next_point_amount
        next_point_amount *= 0.25

    return total_points


users_list = []

user_top_lists = []

for user in users_list:
    response_json = get_user_top_tracks(user)
    parent_key = list(response_json.keys())[0]
    child_key = list(response_json[parent_key].keys())
    child_key.sort()
    # Cheking if the user has any song
    if response_json[parent_key]['@attr']['total'] == '0':
        print(f'The user "{user}" has no songs')
    else:
        for j in response_json[parent_key][child_key[1]]:
            if parent_key == 'topartists':
                name = j['name']
            else:
                # Combine the song name and artist name
                name = f'{j["name"]} - {j["artist"]["name"]}'
            playcount = int(j['playcount'])
            points = calculate_points(playcount)
            key = {'name': name,
                   'points': points,
                   'playcount': playcount,
                   'user': user}
            user_top_lists.append(key)
    print(f'Finished collecting the songs by "{user}"')


def group_by_name_and_sum_points(lst):
    lst.sort(key=itemgetter('name'))
    new_lst = []

    for name, grouped_dicts in groupby(lst, key=itemgetter('name')):
        dicts = list(grouped_dicts)
        dicts.sort(key=itemgetter('playcount'), reverse=True)

        points = sum(d['points'] for d in dicts)
        detail = ', '.join((f"{d['user']} ({d['playcount']})") for d in dicts)
        new_lst.append({
            'name': name,
            'points': points,
            'detail': detail
        })

    new_lst.sort(key=itemgetter('points'), reverse=True)
    return new_lst


user_top_lists = group_by_name_and_sum_points(user_top_lists)


for index, song in enumerate(user_top_lists[0:10]):
    song_information = f"#{index + 1}. {song['name']} [{song['points']:.2f}]"
    detail = f"# of plays: {song['detail']}"
    print(f"{song_information}, {detail}")
