import re
import pandas as pd

TAX_BGN = 2.93

pd.set_option('precision', 2)
df = pd.read_csv('../land_prices.csv')

def format_weight(row):
    # Remove symbols and whitespace
    row['weight_kg'] = re.sub(r'\s', '', row['weight_kg'])

    # Get string after 'до'
    row['weight_kg'] = row['weight_kg'].split('до', 1)[1]
    
    row['weight_kg'] = re.sub(',', '', row['weight_kg'])
    row['weight_kg'] = re.sub('кг', '', row['weight_kg'])

    # Convert strings to numbers
    return pd.to_numeric(row, errors='coerce')

df = df.apply(format_weight, axis=1)

# Convert weights to grams 
weights = df['weight_kg'].values
weights = weights * 1000

df = df.drop('weight_kg', axis=1)

prices_all_zones = dict()

def add_tax(data_tuple):
    index, price = data_tuple

    if index > 0:
        return price + TAX_BGN
    
    return price

for index, zone_name in enumerate(df):
    print('\n', zone_name)
    current_prices = df[zone_name]
    current_prices = map(add_tax, enumerate(current_prices))

    prices_all_zones[zone_name] = dict(zip(weights, current_prices))
    print(prices_all_zones[zone_name])
