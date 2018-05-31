import pandas as pd
pd.set_option('precision', 2)

df = pd.read_csv('../speedy_balkan_prices.csv')
df = df.apply(pd.to_numeric, axis=1)

weights_grams = df['weight_kg'].values * 1000
prices = dict(zip(weights_grams, df['BGN'].values))

print(prices)