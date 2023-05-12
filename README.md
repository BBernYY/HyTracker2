# Hytracker 2
*Rewrote my hytracker project!*
  
  
Basically, this program can track any hypixel player's activity, if they have the api settings enabled (almost everyone does). main.py is the code I wrote for the basic things, that I can reuse for similar projects, and hypixel.py is for this project. might do this with steam too.


## how to use
Edit the constants in the hypixel.py file, and create a file called '.env', with this data structure:

```
API_KEY=[hypixel api key here]
WEBHOOK_URL=[webhook url here]
```
*The square brackets are not part of the code, replace the [hypixel api key here] part with your api key, inculding the brackets.*

### Don't know how to find these?

1. api key: just use /api in hypixel.
2. webhook url: in channel settings on discord.