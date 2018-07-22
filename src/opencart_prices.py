import re, os
import pandas as pd
from pprint import pprint

# БГ Пощи прилагат такса 1.50 евро за поръчки над 2кг
TAX_BGN = 2.93

pd.set_option("precision", 2)

def format_weight(row):
    # Remove symbols and whitespace
    row["weight_kg"] = re.sub(r"\s", "", row["weight_kg"])

    # Get string after "до"
    row["weight_kg"] = row["weight_kg"].split("до", 1)[1]
    
    row["weight_kg"] = re.sub(",", "", row["weight_kg"])
    row["weight_kg"] = re.sub("кг", "", row["weight_kg"])

    # Convert strings to numbers
    return pd.to_numeric(row, errors="coerce")

def add_tax(data_tuple):
    index, price = data_tuple

    if index > 1:
        return price + TAX_BGN
    
    return price

def format_decimal_places(price):
    return "{:.2f}".format(price)


# https://stackoverflow.com/a/39436143/4957288
def clean_dict_string(dictionary):
    string = str(dictionary)
    chars_to_remove = ["{", "}", "'"]

    return string.translate({ ord(char): "" for char in chars_to_remove })

for index, file_path in enumerate(["../land_prices.csv", "../air_prices.csv"]):
    df = pd.read_csv(file_path)
    df = df.apply(format_weight, axis=1)

    # Convert weights to grams 
    weights = df["weight_kg"].values
    weights = weights * 1000

    df = df.drop("weight_kg", axis=1)

    prices_all_zones = dict()

    path = os.path.dirname(os.path.realpath(__file__))

    if index == 0:
        name = 'land_price'
    else:
        name = 'air_price'

    file_path = path + "/../opencart_shipping_{}_strings_parcels.txt".format(name)

    text_file = open(file_path, "w")

    for index, zone_name in enumerate(df):
        current_prices = df[zone_name]
        current_prices = map(add_tax, enumerate(current_prices))
        current_prices = map(format_decimal_places, current_prices)
        
        prices_all_zones[zone_name] = dict(zip(weights, current_prices))

        text_file.write(zone_name + "\n")
        text_file.write(clean_dict_string(prices_all_zones[zone_name]) + "\n\n")


    text_file.close()
