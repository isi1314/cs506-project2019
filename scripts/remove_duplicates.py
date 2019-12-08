from more_itertools import unique_everseen
import pandas as pd

from pandas import *

#reading dataset


df = pd.read_csv('../datasets/finals/all_data_ref_Name_no_dup.csv', index_col=0)
print (df.columns)

print(df.shape)
# Notes:
# - the `subset=None` means that every column is used 
#    to determine if two rows are different; to change that specify
#    the columns as an array
# - the `inplace=True` means that the data structure is changed and
#   the duplicate rows are gone  
#df.drop_duplicates(subset=['Name'], inplace=True)

df = df.replace('Not Available',np.NaN)
df = df.replace('NA',np.NaN)
dupes = df.duplicated(subset=['USBC_phone'])
dupes[df['USBC_phone'].isnull()] = False
df_dup = df[dupes]
df = df[~dupes]



# Write the results to a different file
df.to_csv('../datasets/finals/all_data_ref_usbc_no_dup.csv')
df_dup.to_csv('../datasets/finals/all_data_ref_usbc_only_dup.csv')
print (df.shape, df_dup.shape)


