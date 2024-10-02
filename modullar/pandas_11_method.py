import os 
import pandas as pd 

BASE_DIR = os.getcwd()
file_path = os.path.join(BASE_DIR, "modullar", "videos.csv")

df = pd.read_csv(file_path)

df = df.sort_values(by="Video views", ascending=False)

df.to_csv("new_df.csv", index=False)

# ------------------
# df = df.iloc[::-1]
# df.to_csv("new_df.csv", index=False)
# ------------------
# print(df.count())
# ------------------
# print(df[df["Video views"] == df["Video views"].min()])
# print(df[df["Video views"] == df["Video views"].max()])
# print(df.min())
# print(df.max())
# ------------------
# print(df.describe())
# ------------------
# print(df.index)
# ------------------
# print(df.info())
# ------------------
# print(df.tail())
# ------------------
# print(df.head(10))
# ------------------
# setir, sutun = df.shape
# print(f"Sətir sayı : {setir}, Sütun sayı : {sutun}")

"""
    1  - shape
    2  - head 
    3  - tail
    4  - info
    5  - index
    6  - describe
    7  - min
    8  - max
    9  - count
    10 - iloc
    11 - sort_values
"""