
########## Simple Linear Regression ##########
import time
start_time = time.time()

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import r2_score,mean_squared_error

combined_df = pd.read_csv('/data/act_data.csv').drop('encString', axis=1)
# Separate features and target class
features = combined_df.drop(['Target'], axis = 1)
target = combined_df

# Split training and testing datasets and train&test 
x_train,x_test,y_train,y_test = train_test_split(features,target, random_state = 1)
LR_model = LinearRegression()
LR_model.fit(x_train,y_train)

LR_model_train_pred = LR_model.predict(x_train)
LR_model_test_pred = LR_model.predict(x_test)

result = 'MSE train data: %.3f, MSE test data: %.3f' % (
mean_squared_error(y_train,LR_model_train_pred),
mean_squared_error(y_test,LR_model_test_pred)) 

result = result + '\n' +'R2 train data: %.3f, R2 test data: %.3f' % (
r2_score(y_train,LR_model_train_pred),
r2_score(y_test,LR_model_test_pred))

file = open('/output/LR_result.txt', 'w')
file.write(result)
file.close()

print("Analysis took", time.time() - start_time, "to run")
print("Result is generated at TSE!")