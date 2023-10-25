import pandas as pd
import json

df = pd.read_json("simple.json", orient="values")

df.to_csv("simple.csv", index =False)
