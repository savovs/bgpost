# БГ Пощи прилагат такса 1.50 евро за поръчки над 2кг
import os
import pandas as pd

data = pd.read_html('http://www.bgpost.bg/bg/347', match='тегло')

print('Цени Земен Път БГ Пощи \n', data[0], '\n\n')
print('Цени Въздушен Път БГ Пощи \n', data[1], '\n\n')

path = os.path.dirname(os.path.realpath(__file__))

new_headers = ['weight_kg', 'zone_1', 'zone_2',
           'zone_3', 'zone_4', 'zone_5', 'zone_6']

for index, name in enumerate(['land', 'air']):
    df = data[index]
    df.columns = new_headers

    # Remove first rows containing old column names
    df = df.iloc[2:]
    df = df.set_index('weight_kg')

    file_path = path + '/../{}_prices.csv'.format(name)
    df.to_csv(file_path, encoding='utf-8')
