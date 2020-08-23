import pandas as pd
import json

df = pd.read_csv('solr_data.csv')
df = df.transpose()

temp_P = {}
temp_U = {}
temp_C = {}

for i in range(len(df)):
    if 'Publication_Rate' in df.index[i]:
        temp_P[df.index[i]] = df.iloc[i][0]
    elif 'Country' in df.index[i]:
        temp_C[df.index[i]] = df.iloc[i][0]
    else:
        temp_U[df.index[i]] = df.iloc[i][0]

P = []
U = []
C = []

final_P = {}
final_U = {}
final_C = {}

for i in range(len(temp_P)):
    if ('Publication_Rate.'+str(i) in temp_P.keys()) and ('Country.'+str(i) in temp_C.keys()) and ('University_name.'+str(i) in temp_U.keys()):
        final_P['Publication_Rate.'+str(i)] = temp_P['Publication_Rate.'+str(i)]
        final_C['Country.'+str(i)] = temp_C['Country.'+str(i)]
        final_U['University_name.'+str(i)] = temp_U['University_name.'+str(i)]
        
for i in range(len(temp_P)):
    if 'Publication_Rate.'+str(i) in final_P:
        P.append(final_P['Publication_Rate.'+str(i)])
    if 'Country.'+str(i) in final_C:
        C.append(final_C['Country.'+str(i)])
    if 'University_name.'+str(i) in final_U:
        U.append(final_U['University_name.'+str(i)])

# =============================================================================
#         P.append(temp_P['Publication_Rate.'+str(i)])
#         C.append(temp_C['Country.'+str(i)])
#         U.append(temp_U['University_name.'+str(i)])
# =============================================================================

df1 = pd.DataFrame({"Countries": C, "Universities": U, "Publications": P})

dict1 = {}

for i in range(len(C)):
    if C[i] in dict1.keys():
        continue
# =============================================================================
#         dict1[C[i]].append({"name": U[i],
#                             "children": 
#                                 [{"name": str(P[i])+" publications"}]
#                                 })
# =============================================================================
    else:
        dict1[C[i]] = {"name": U[i],
                            "children": 
                                [{"name": str(P[i])+" publications"}]
                            }



dict2 = {"name": "Country"}

list2 = []
for k,v in dict1.items():
    list2.append({"name": k,"children": [v]})

dict2['children'] = list2

with open('Cleaned_Data.json', 'w') as f:
    json.dump(dict2, f)