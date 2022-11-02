# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 19:42:29 2022

@author: Yuanyuan_Tang
"""

from io import StringIO
import numpy as np
import pandas as pd


'''
Import data into Data Frame,  read_csv, 
DataFrame: in the structure of Dictionary

https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
'''
#df0=pd.read_csv(data_csv)  # Read data infer the header based on the first row
# The following command added headers mannually
df1=pd.read_csv("Movie.csv", header=0, \
                names=['Rank','MovieTitle','Studio','TotalGross','Theaters','OpeningGross','OpeningTheaters','OpenDate'])  # Read data
#df2=pd.DataFrame(data_csv,
#\ columns=['Rank','MovieTitle','Studio','TotalGross','Theaters','OpeningGross','OpeningTheaters','OpenDate'])  # Read data

print(df1.head(n=5))  # Show the first 5 rows of data


'''
Write data in DataFrame to a csv
https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
'''
df1.to_csv('Movie.csv')


'''
Read specific columns, rows, and location
df.iloc[]--based on integer index
df.loc[]--based on label index
df['']
Read a specific column  df1['Rank']
https://www.educative.io/blog/pandas-cheat-sheet

https://www.statology.org/pandas-select-rows-by-index/
'''
a=df1['Rank']   # Read a specific column
b=df1['Rank'][:5]  # Get the first 5 elements of the first column

c=df1.iloc[2:5, -1] # Read the elements from index 2 to 5-1 of the last column
e=df1.iloc[[2,5,8], 0] # Read 2th,5th, 8th elements of first column
d=df1.iloc[0]    # 0-th row
f=df1.iloc[:,0]   # 0th column



'''
Retrieval information of pandas
read the size of Pandas DataFrame
Data types of DataFrame
https://pbpython.com/pandas_dtypes.html
'''
print(df1.dtypes)
df_shape=df1.shape  # The size of DataFrame
print(df1.info())  # See the datainformation of DataFrame


'''
A toy example to change data type of strings
https://towardsdatascience.com/how-to-change-column-type-in-pandas-dataframes-d2a5548888f8
'''
df = pd.DataFrame(
  [
    ('1', 1, 'hi'),
    ('2', 2, 'bye'),
    ('3', 3, 'hello'),
    ('4', 4, 'goodbye'),
  ],
  columns=list('ABC')
)
print(df)
df.info()

# Change data type of the columns
df['A'] = df['A'].astype(int)
df.info()
df['B'] = df['B'].astype(str)
df.info()
df['B'] = df['B'].astype(float)
df.info()


'''
Pandas to numpy 
https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array
'''
g=df[['A','B']].to_numpy()
print(type(g))

'''
Pandas DataFrame remove characters
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.str.replace.html
'''
import re
df2=df1.head(n=5)
Y=df2['TotalGross'].values
print(Y)
for i in range(len(Y)):
    Y[i]=float(re.sub('[$,]','', Y[i])) # replace %, in [] by '' and convert to float
#print(Y)
df2['TotalGross']=Y
df2['TotalGross']=df2['TotalGross'].astype(float)

print(df2.info())




'''
Pandas add a new column to specific positions
'''







