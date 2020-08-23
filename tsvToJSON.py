import pandas as pd

df = pd.read_csv('ProjectTeamID_9_v3.tsv', delimiter='\t', encoding='utf-8')

df.to_json('ProjectTeamID_9_v3.json')