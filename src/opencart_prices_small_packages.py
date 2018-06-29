import re, os
import pandas as pd
from pprint import pprint

pd.set_option("precision", 2)
df = pd.read_csv("../small_package_prices.csv")

prices_all_zones = dict()

def format_decimal_places(price):
    return "{:.2f}".format(price)

# https://stackoverflow.com/a/39436143/4957288
def clean_dict_string(dictionary):
    string = str(dictionary)
    chars_to_remove = ["{", "}", "'"]

    return string.translate({ ord(char): "" for char in chars_to_remove })


path = os.path.dirname(os.path.realpath(__file__))
file_path = path + "/../opencart_shipping_price_strings_small_packages.txt"

text_file = open(file_path, "w")



for index, zone_name in enumerate(df):
    current_prices = df[zone_name]

    # Такса за "Препоръчана" пратка
    current_prices = map(lambda price: price + 3.0, current_prices)


    current_prices = map(format_decimal_places, current_prices)
    
    prices_all_zones[zone_name] = dict(zip(df['weight_grams'], current_prices))

    if index > 0:
        text_file.write(zone_name + "\n")
        text_file.write(clean_dict_string(prices_all_zones[zone_name]) + "\n\n")


text_file.close()