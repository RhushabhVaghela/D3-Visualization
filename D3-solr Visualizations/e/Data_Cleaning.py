import pandas as pd

df = pd.read_csv('solr_data.csv')
df = df.transpose()

lab = []
rank = []

for i in range(len(df)):
    if 'No_in_lab' in df.index[i]:
        lab.append(df.iloc[i][0])
    else:
        rank.append(df.iloc[i][0])
        
lab = lab[:len(rank)]
        
cleaned_data = pd.DataFrame({"university_rank": rank, "no_of_labs": lab})

cleaned_data.to_csv('Cleaned_Data.csv')
