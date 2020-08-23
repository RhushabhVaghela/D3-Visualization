import pandas as pd
import csv

df = pd.read_csv('solr_data.csv')
df = df.transpose()

career = []

for i in range(len(df)):
    career.append(df[0][i])

unique = list(set(career))

dict1 = {}
for i in range(len(unique)):
    count = 0
    for j in range(len(df)):
        if unique[i] == df[0][j]:
            count += 1
        dict1[str(unique[i])+" yrs"] = count

keys = []
values = []        
for k,v in dict1.items():
    keys.append(str(k))
    values.append(v)
    

df1 = pd.DataFrame({"Career": keys, "Count": values})
df1.to_csv('Cleaned_Data.csv',index=False)