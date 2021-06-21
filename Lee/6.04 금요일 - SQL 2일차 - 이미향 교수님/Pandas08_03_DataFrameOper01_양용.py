
# coding: utf-8

# In[ ]:


titanic.columns 컬럼명 확인
titanic.shape 행렬 확인


# In[4]:


import pandas as pd
import seaborn as sns

#titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
print(titanic.columns,'\n',titanic.shape)
df = titanic.loc[:,['age','fare']]
print(df.head())
print(type(df))


# In[8]:


addition = df +10
print(addition.head())
print(type(addition))

