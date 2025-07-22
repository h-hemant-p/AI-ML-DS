import pandas as pd

data = {
    "Name":"Hemant",
    "Age":21,
    "Gender":"Male"
}

# create a dataframe
df = pd.DataFrame([data])

df.to_csv('data.csv', index=True)
