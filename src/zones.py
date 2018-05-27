# Zones taken from http://www.bgpost.bg/bg/347
# BG Posts apply a 1.50 euro tax for orders above 2kg!
import pandas as pd

xls = pd.ExcelFile("../zones.xls")

# Parse sheet number
sheet = xls.parse(0)

# Remove unneeded columns
sheet = sheet.drop('Unnamed: 13', axis=1)

# # Print first 5 rows
# print(sheet.head())

# Rename columns "DTS" meaning: http://www.bgpost.bg/bg/506
headers = ['number', 'code', 'country_en', 'country_bg',
           'land_zone', 'land_max_weight_kg', 'land_max_value_dts', 'land_category',
           'air_zone', 'air_max_weight_kg', 'air_max_value_dts', 'air_category',
           'letters_max_value_dts']

sheet.columns = headers

# Remove first row containing old column names
sheet = sheet.iloc[1:]

print(sheet.head())