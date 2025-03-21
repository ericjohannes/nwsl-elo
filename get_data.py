import requests

url = "https://api-sdp.nwslsoccer.com/v1/nwsl/football/seasons/nwsl::Football_Season::79664e9589084e1b83d2dec2c279c18c/matches?locale=en-US"

data = requests.get(url)
print(data.content())

data.json()['matches'] # has a list of mathces
data.json()['competition']['name'] # is NWSL
data.json()['competition']['seasonName'] # year of season

# or i could use this api https://app.americansocceranalysis.com/api/v1/__docs__/#/National%20Women's%20Soccer%20League%20(NWSL)/get_nwsl_games
# for instance
# curl -X GET "https://app.americansocceranalysis.com/api/v1/nwsl/games?season_name=2023" -H  "accept: application/json"