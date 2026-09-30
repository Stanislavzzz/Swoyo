import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt


path_nout_csv = Path('new_laptop.csv')

if path_nout_csv.exists():
    df = pd.read_csv(path_nout_csv, encoding='utf-8')
    print("OK")
else:
    print('No file found')

first_prices = df["Price_euros"].head(3)

fig, ax = plt.subplots(figsize=(15, 7))
ax.bar(["Ноут1", "Ноут2", "Ноут3"], first_prices)
ax.set_title("Цены первых 3 ноутов")
ax.set_xlabel("Наименование ноутов")
ax.set_ylabel("Цены в евро")
ax.grid(True, axis="y")
plt.show()