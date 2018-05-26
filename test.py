import pandas as pd

prices = pd.read_html("http://www.bgpost.bg/bg/347", match="тегло")

print("Цени Земен Път \n", prices[0], "\n\n")
print("Цени Въздушен Път \n", prices[1], "\n\n")

xls = pd.ExcelFile("zones.xls")
sheet = xls.parse(0) # sheet number
# var1 = sheet['ColumnName']
# print(var1[1]) #1 is the row number

print(sheet.head()) # print first 5 rows


