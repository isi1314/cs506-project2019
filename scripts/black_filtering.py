from more_itertools import unique_everseen
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pandas import *

#reading dataset


df = pd.read_csv('hispanic_final_no_duplicates.csv', index_col=0)
print (df.columns)

print(df.shape)
print()
print(df['RefUSA_NAICSCode'].value_counts())


#sns.catplot(x='RefUSA_revenue', kind="count", palette="ch:.25", data=df);


#plt.show()
