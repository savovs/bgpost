# БГ Пощи прилагат такса 1.50 евро за поръчки над 2кг!
import pandas as pd

prices = pd.read_html("http://www.bgpost.bg/bg/347", match="тегло")

print("Цени Земен Път \n", prices[0], "\n\n")
print("Цени Въздушен Път \n", prices[1], "\n\n")
