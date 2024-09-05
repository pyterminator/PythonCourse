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

plt.plot(country_names, country_values)
plt.show()
