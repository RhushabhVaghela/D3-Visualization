import pandas as pd
import json

df = pd.read_csv('solr_data.csv')
df = df.transpose()

degree_area = []

for i in range(len(df)):
    degree_area.append(df.iloc[i][0])
 
dict1 = {}

DA = list(set(degree_area))
    
for i in range(len(DA)):
    count = 0
    for j in range(len(degree_area)):
       if DA[i] == degree_area[j]:
           count += 1 
    dict1[DA[i]] = count 
    
key = []
value = []

for k,v in dict1.items():
    key.append(k)
    value.append(v)
    
list1 = []   
for i in range(len(key)):
    list1.append({"Degree_Area": key[i], "Counts": value[i]})

with open('Cleaned_Data.json', 'w') as f:
    json.dump(list1, f)