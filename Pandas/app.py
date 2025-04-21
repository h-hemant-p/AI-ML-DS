import pandas as pd

# read the data from the csv file
# df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# read the data from the excel file
df = pd.read_excel('SampleSuperstore.xlsx')

# read the data from the json file 
# df = pd.read_json('sample_Data.json')


print(df)