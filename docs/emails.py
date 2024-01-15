import pandas as pd

roster = pd.read_csv("ferpa/roster.csv")
for x in roster["Email Address"]:
    print(x)
