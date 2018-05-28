import os
import pandas as pd

mixed_zones = pd.read_csv('../mixed_zones.csv')
eu_countries = pd.read_csv('../eu_countries.csv')

eu_countries = eu_countries[['name', 'alpha2Code']]

eu_mixed_zones = mixed_zones[mixed_zones['code'].isin(eu_countries['alpha2Code'])]
other_mixed_zones = mixed_zones[~mixed_zones['code'].isin(eu_countries['alpha2Code'])]

path = os.path.dirname(os.path.realpath(__file__))

for index, name in enumerate(['eu', 'other']):
    df = eu_mixed_zones if index == 0 else other_mixed_zones

    file_path = path + '/../{}_mixed_zones.csv'.format(name)
    df.to_csv(file_path, encoding='utf-8')