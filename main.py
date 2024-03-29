import argparse
from itertools import groupby
from operator import itemgetter


from services.audio_scrobbler import get_user_top_items


def calculate_points(playcount):
    total_points = 1.0
    current_play_points = 0.9

    for _ in range(2, playcount + 1):
        total_points += current_play_points
        current_play_points *= 0.9

    return total_points


def process_request(json, user, user_top_lists):
    parent_key = list(json.keys())[0]
    child_key = list(json[parent_key].keys())
    child_key.sort()
    # Cheking if the user has any song
    if json[parent_key]['@attr']['total'] == '0':
        print(f"The user '{user}' has no songs")
    else:
        for j in json[parent_key][child_key[1]]:
            if parent_key == 'topartists':
                name = j['name']
            else:
                # Combine the song name and artist name
                name = f'{j["name"]} - {j["artist"]["name"]}'
            playcount = int(j['playcount'])
            points = calculate_points(playcount)
            key = {'name': name,
                   'points': points,
                   'user': user,
                   'playcount': playcount}
            user_top_lists.append(key)


def group_by_name_and_sum_points(lst):
    lst.sort(key=itemgetter('name'))
    new_lst = []

    for name, grouped_dicts in groupby(lst, key=itemgetter('name')):
        dicts = list(grouped_dicts)
        # If the song is only in one user's top list, then skip it
        if len(dicts) == 1:
            continue

        dicts.sort(key=itemgetter('playcount'), reverse=True)

        points = 0
        detail_parts = []

        for d in dicts:
            points += d['points']
            detail_parts.append(f"{d['user']} ({d['playcount']})")

        new_lst.append({
            'name': name,
            'points': points,
            'detail': ', '.join(detail_parts)
        })

    new_lst.sort(key=itemgetter('points'), reverse=True)
    return new_lst


def main():
    parser = argparse.ArgumentParser(description='Build a top list of users')
    parser.add_argument('users',
                        type=str,
                        nargs='+',
                        help='User names to get the top items from')
    parser.add_argument('-m', '--method',
                        choices=['gettoptracks',
                                 'gettopalbums',
                                 'gettopartists'],
                        default='gettoptracks',
                        help='Method to get the top items from')
    parser.add_argument('-p', '--period',
                        choices=['7day',
                                 '1month',
                                 '3month',
                                 '6month',
                                 '12month',
                                 'overall'],
                        default='7day',
                        help='Period to get the top items from')
    parser.add_argument('-l', '--length',
                        type=int,
                        default=10,
                        choices=range(1, 101),
                        help='Length of the top list')
    parser.add_argument('-d', '--detail',
                        action='store_true',
                        help='Show the detail of the top list')
    args = parser.parse_args()

    user_top_lists = []
    for user in args.users:
        response_json = get_user_top_items(args.method, user, args.period)
        process_request(response_json, user, user_top_lists)
        print(f"Finished collecting the items from '{user}'")

    user_top_lists = group_by_name_and_sum_points(user_top_lists)

    for rank, song in enumerate(user_top_lists[0:args.length], 1):
        song_information = f"#{rank}. {song['name']} [{song['points']:.2f}]"
        if args.detail:
            song_information += f", # of plays: {song['detail']}"
        print(song_information)


if __name__ == '__main__':
    main()
