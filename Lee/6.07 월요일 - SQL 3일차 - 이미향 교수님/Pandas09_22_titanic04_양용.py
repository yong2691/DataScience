
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.columns)
print(len(titanic.columns))


# In[13]:


ages = list(range(0,90,10))

for i in ages:
    ageTemp =titanic[(titanic['age']>=i) & (titanic['age'] < i+10) & (titanic['survived']==0)]
    print("{}세 이상 - {}세 미만 사망자수 : {}".format(i,i+10,(ageTemp['survived']).count()))


# In[15]:


ages = list(range(0,90,10))

for i in ages:
    ageTemp = titanic[(titanic['age'] >= i ) & (titanic['age'] < i+10)& (titanic['survived']==0)]
    print("{}세 이상 - {}세 미만 사망자수 : {}".format(i,i+10,(ageTemp.groupby('sex')['survived']).count() ))

