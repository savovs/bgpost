import json, requests, os
import pandas as pd

url = 'https://restcountries.eu/rest/v2/regionalbloc/eu'
req = requests.get(url)

df = pd.read_json(req.text)
df = df.sort_values('name')
df = df.set_index('name')

file_path = os.path.dirname(os.path.realpath(__file__)) + '/../eu_countries.csv'
df.to_csv(file_path, encoding='utf-8')
