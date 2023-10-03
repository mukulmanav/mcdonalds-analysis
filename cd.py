#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

import seaborn as sns 

# %%
df=pd.read_csv("Datasets/menu.csv")
# %%
df.shape
# %%
df.head()
# %%
df.describe()
# %% Inference-info tells us about the type of value within eaach column.
df.info()
# %%  Confirming all the null values
df.isnull().sum()
# %% printing all the categories
df['Category'].value_counts()
# %% getting total numbers of categories 
df['Category'].nunique()
# %% printing all the values in ITEM column
df['Item'].value_counts().head()
# %%
df['Item'].nunique()
# %% Q1>Plot graphically which food categories have the highest and lowest varieties?
plt.figure(figsize=(15,6))

df['Category'].hist()

# %% Q2> Which all variables have an outlier?
df.describe()
plt.figure(figsize=(15,10))

sns.boxplot(data=df[['Calories','Calories from Fat','Total Fat','Saturated Fat']])
 
# %% Q3>Which variables have the highest correlation? Plot them and find out the value?
#correlation above 50% will be highlighted

correlation=df.corr()

correlation

# %%
plt.figure(figsize=(15,11))

sns.heatmap(correlation,annot=True)
# %% Q4> Which category contributes to the maximum % of Cholesterol in a diet (% daily value)?
print("Number of categories-",df['Category'].nunique())

# %%
df['Category'].unique()

from pandas import DataFrame

category_List= sorted(df['Category'].unique())
type(sorted(df['Category'].unique()))

a=pd.DataFrame(category_List,columns=[''])
a.index +=1
print("The different food categories available ",a)
# %%
b=pd.pivot_table(df,'Cholesterol (% Daily Value)',index=['Category'])
result=b.sort_values(('Cholesterol (% Daily Value)'),ascending=False)
result

# %% Q5> Which item contributes maximum to the Sodium intake?
df['Item'].head()

# %%
df['Item'].nunique()
# %%
c=pd.pivot_table(df,'Sodium',index=['Item'])

result_c=c.sort_values(('Sodium'),ascending=False)

result_c.head(15)
# %% Q6> Which 4 food items contain the most amount of Saturated Fat?
d=pd.pivot_table(df,'Saturated Fat',index=['Item'])

result_d=d.sort_values(('Saturated Fat'),ascending=False)


result_d.head(15)

# %%
