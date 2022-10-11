# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:14:35 2022

@author: User
"""

#https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.csv
#all missing values are marked with a 0 for only columns 1-5

#1. save the above as a .csv file

#2. read the CSV into a df

#3. check the size of the df (size)

#4. check the first 5 rows (iterating via index or direct first 5)

#5. index out the first column (index_col=0)

#6. count the number of missing values for each column (iterate all columns, find df['column'] == 0 (find sum))

#7. replace '0' values with 'np.nan'

#8. drop rows with missing values

#9. check the size of the final df


import pandas as pd
import numpy as np
df = pd.read_csv('pima-indians-diabetes.csv', header=None) #index first column

#print(df.to_string())

print('initial size', df.size)
print('first 5 rows', df.head(5))
print('index first columnn', df.iloc[:,0])

count = (df[4] == 0).sum()
print('count of 0s', count)

df.replace(0, np.nan, inplace=True)
print('checking', df)

df = df.dropna()
print(df)
print('final size', df.size)