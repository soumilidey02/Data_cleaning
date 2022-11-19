import csv
import pandas as pd

df=pd.read_csv("main.csv")

print(df.shape)

del df["Luminosity"]

df.to_csv("final.csv")