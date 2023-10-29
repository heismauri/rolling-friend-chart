**Rolling Friend Chart** is a Python script that creates a chart based on your friends' recent scrobbles from LastFM. It can create charts for artists, albums and tracks. It uses the [LastFM API](https://www.last.fm/api) to collect the data. You can customize the chart by changing the length of the chart and by showing the detail of it, which is how much each item was scrobbled by the user.

# Usage & options
```bash
python main.py users [users...] -m {gettoptracks,gettopalbums,gettopartists}
```

## General options
```
-h, --help            show this help message and exit
-l, --length {1-100}  length of the top list
-d, --detail          show the detail of the top list
```

# Output

## Example without detail
```
Finished collecting the items from 'USERNAME'
Finished collecting the items from 'USERNAME'
Finished collecting the items from 'USERNAME'
#1. no tears left to cry - Ariana Grande [4.33]
#2. bad idea right? - Olivia Rodrigo [4.28]
#3. MORE - K/DA [4.16]
#4. Howl - CHUU [3.66]
#5. Hold On Tight - aespa [2.67]
#6. Newtopia - Loosemble [2.67]
#7. Sugarcoat (NATTY Solo) - KISS OF LIFE [2.67]
#8. because i liked a boy - Sabrina Carpenter [2.62]
#9. Dance the Night - Dua Lipa [2.62]
#10. El Amor No Duele - Denise Rosenthal [2.62]
```

## Example with detail
```
Finished collecting the items from 'USERNAME'
Finished collecting the items from 'USERNAME'
Finished collecting the items from 'USERNAME'
#1. no tears left to cry - Ariana Grande [4.33], # of plays: USERNAME (5), USERNAME (5), USERNAME (1)
#2. bad idea right? - Olivia Rodrigo [4.28], # of plays: USERNAME (4), USERNAME (3), USERNAME (1)
#3. MORE - K/DA [4.16], # of plays: USERNAME (5), USERNAME (2), USERNAME (1)
#4. Howl - CHUU [3.66], # of plays: USERNAME (4), USERNAME (1), USERNAME (1)
#5. Hold On Tight - aespa [2.67], # of plays: USERNAME (21), USERNAME (1)
#6. Newtopia - Loosemble [2.67], # of plays: USERNAME (8), USERNAME (1)
#7. Sugarcoat (NATTY Solo) - KISS OF LIFE [2.67], # of plays: USERNAME (7), USERNAME (1)
#8. because i liked a boy - Sabrina Carpenter [2.62], # of plays: USERNAME (3), USERNAME (1)
#9. Dance the Night - Dua Lipa [2.62], # of plays: USERNAME (3), USERNAME (1)
#10. El Amor No Duele - Denise Rosenthal [2.62], # of plays: USERNAME (3), USERNAME (1)
```
