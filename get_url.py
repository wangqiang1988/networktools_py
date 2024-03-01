import json
from haralyzer import HarParser, HarPage

urllist=[]

with open('discord.com.har', 'r',encoding='utf-8') as f:
    har_parser = HarParser(json.loads(f.read()))

    data = har_parser.har_data

    for url in har_parser.har_data['entries']:
        urllist.append(url['request']['url'].split('/')[2])

for urltxt in list(set(urllist)):
    print(urltxt)