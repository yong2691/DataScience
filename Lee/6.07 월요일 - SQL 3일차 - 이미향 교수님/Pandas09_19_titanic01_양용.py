
# coding: utf-8

# In[4]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')

print(titanic.columns)
print(len(titanic.columns))


# In[7]:


for i in titanic.columns:
    print("[%s]\n"%i) #총 15개 컬럼이 있는데, 이걸 모두 한번씩 프린트하고
    print(titanic[i].unique()) #유니크한 값에 대해서도 프린트 한다.
    print("="*80)

