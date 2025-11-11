import matplotlib.pyplot as plt
import pandas

file = pd.read_parquet("titanic.parquet")  #Читаем parquet
df = pd.read_parquet(file)

# Сохраняем в csv
df.to_csv("titanic1.csv", index=False)
print("CSV сохранён как titanic1.csv")

text = pd.read_csv("result.csv")    # Читаем CSV обратно
print(text.head())

text.hist()     # Строим гистограмму всех числовых колонок
plt.show()
