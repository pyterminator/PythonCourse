import os 
import pandas as pd 
from collections import Counter
import matplotlib.pyplot as plt

BASE_DIR = os.getcwd()

file_name = "users.csv"
file_path = os.path.join(BASE_DIR, "modullar", file_name)

data = pd.read_csv(file_path)

countries = data.country.to_list()
countries = Counter(countries)
 
country_names = countries.keys()
country_values = countries.values()

plt.figure(figsize=(6, 4))
plt.bar(country_names, country_values)
plt.xlabel("Ölkələr")
plt.ylabel("Adam Sayı")
plt.title("Ölkələrə görə sıralama")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("modullar/data.png")
