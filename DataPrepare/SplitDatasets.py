### Slipt Data into multiple data parties ### 

import pandas as pd
import numpy as np
import json

with open('input.json') as data_file:    
    inputJson = json.load(data_file)

num_of_party = inputJson['num_of_party']

df = pd.read_csv(inputJson['data_file'])
variables = df.columns[4:]
PI = df[df.columns[0:4]]

sets = int(len(variables)/num_of_party)

for i in range(0, num_of_party):
    if i == num_of_party-1:
        df_sub = df[variables[int(i*sets):]]
    else:
        df_sub = df[variables[int(i*sets): int((i+1)*sets)]]
    save_df = pd.concat([PI, df_sub], axis=1, join='inner')
    save_df.to_csv('data_party_%d.csv' %(i+1), index=None)