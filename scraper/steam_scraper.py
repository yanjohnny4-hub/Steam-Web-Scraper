import requests
import lxml.html
import json
from pathlib import Path

html = requests.get('https://store.steampowered.com/explore/new/')
doc = lxml.html.fromstring(html.content)

new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

# get title and prices
titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

# get tags for each title
tags_divs = new_releases.xpath('.//div[@class="tab_item_top_tags"]')
tags = []
# tags = [tag.text_content() for tag in tags_divs] | list comprehension ver.
for div in tags_divs:
    tags.append(div.text_content())
tags = [tag.split(',') for tag in tags] # groups tags for same game into sublists

# get platform for each title
platform_div = new_releases.xpath('.//div[@class="tab_item_details"]')
total_platforms = []
for game in platform_div:
    temp = game.xpath('.//span[contains(@class, "platform_img")]')
    platforms = [t.get('class').split(' ')[-1] for t in temp]
    if 'hmd_separator' in platforms:
        platforms.remove('hmd_separator')
    total_platforms.append(platforms)

# all info put together
output = []
for info in zip(titles, prices, tags, total_platforms):
    resp = {}
    resp['title'] = info[0] if info[0] else 'N/A'
    resp['price'] = info[1] if info[1] else 'N/A'
    resp['tags'] = info[2]
    resp['platforms'] = info[3]
    output.append(resp)

downloads = Path.home() / "Downloads"
out_path = downloads / "Steam_Pop_New_Releases.json"
with open(out_path, 'w') as json_file:
     json.dump(output, json_file, indent=4)
print(f'Saved {len(output)} games to {out_path}')
