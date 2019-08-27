import time
import json
start_time = time.time()

import pandas as pd
from PQencryption.hashing import sha_512_PyNaCl

with open('input.json', 'r') as f:
    input = json.load(f)

df = pd.read_csv(input['data_file'])

# Salt must be 128 bytes in hex.
### 18-08-2019 ###
salt_text = input['salt_text']
salt_byte = int(128/len(salt_text))
salt = salt_text.encode('UTF-8') * salt_byte #2.2 Salt (key)

# Input names of PI columns
PI = input['id_feature'] 
act_data = df.drop(PI, axis=1)
# ["housenum", "zipcode", "date_of_birth", "sex"]

# act_data = act_data.drop(input['internal_id'], axis=1)
# 2.3 PI columns (personal identifier)

hashedPI = []
if df[PI].isnull().sum().sum() == 0:
    for i in range(0, len(df)):
        combine_PI = str()
        for j in range(0, len(PI)):
            id_feature =  df.iloc[i][PI[j]]
            combine_PI = combine_PI + str(id_feature)
        
        # Remove space from strings #
        combine_PI =  combine_PI.replace(' ', '')
        hashed = sha_512_PyNaCl.sha512_hash(salt, combine_PI.encode('UTF-8'))
        hashedPI.append(hashed)
else:
    print("Work cannot be done because missing values are in personal identifiers!")
    print(df.isnull().sum())

# print(len(hashedPI))

hashedPI_df = pd.DataFrame(hashedPI, columns=['encString'])
hashedData_df = pd.concat([hashedPI_df, act_data], axis=1, join='inner')
print(len(hashedData_df))

hashedData_df.to_csv("/data/encrypted_%s.csv" %(input['party_name']), index=None, sep=',', encoding='utf-8') #2.4 Output file name

print("My program took", time.time() - start_time, "to run")