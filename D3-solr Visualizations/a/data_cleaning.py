import pandas as pd

df = pd.read_csv('solr_data.csv')
df = df.transpose()

citations = []
year = []

for i in range(len(df)):
    if 'citations' in df.index[i]:
        citations.append(df.iloc[i][0])
    else:
        year.append(int(df.iloc[i][0]))
 
year = list(set(year))

citations = citations[:len(year)]

cleaned_data = pd.DataFrame({"Year": year, "Citation": citations})

cleaned_data.to_csv('Cleaned_Data.csv')