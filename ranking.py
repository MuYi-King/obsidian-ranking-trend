from datetime import datetime
import requests
import json

response = requests.get(
    'https://raw.githubusercontent.com/obsidianmd/obsidian-releases/master/community-plugin-stats.json')

rank_dict = json.loads(response.text)


with open('data.json', 'r') as f:
    data = json.load(f)


tstamp = datetime.strftime(datetime.today(), '%Y-%m-%d_%H:%M')

today_data = {}
for k, v in rank_dict.items():
    if rank_dict[k]:
        today_data[k] = rank_dict[k]['downloads']

today_data = {
    "date": tstamp,
    "data": today_data
}
data.append(today_data)

with open('data.json', 'w') as f:
    json.dump(data, f)
