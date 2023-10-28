from decouple import config

MAX_PLAYCOUNT = config('MAX_PLAYCOUNT', default=10, cast=int)
API_KEY = config('LAST_FM_API_KEY')
