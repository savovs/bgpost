# БГ Пощи прилагат такса 1.50 евро за поръчки над 2кг!
import os
import pandas as pd

# Read and merge land and mixed data
land = pd.read_csv('../land_zones.csv')
land.columns = ['land_zone', 'code', 'shipping_method', 'country_en']
land = land[['land_zone', 'code', 'country_en']]

mixed = pd.read_csv('../mixed_zones.csv')
mixed = mixed[['land_zone', 'code', 'country_en']]

df = pd.concat([land, mixed])
df = df.sort_values('land_zone')
df = df.set_index('land_zone')

path = os.path.dirname(os.path.realpath(__file__))
df.to_csv(path + '/../all_land_countries.csv', encoding='utf-8')