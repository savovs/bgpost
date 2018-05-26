import pandas as pd

xls = pd.ExcelFile("zones.xls")

sheet = xls.parse(0) # sheet number

# var1 = sheet['ColumnName']

# print(var1[1]) #1 is the row number

print(sheet.head()) # print first 5 rows