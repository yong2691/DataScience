
# coding: utf-8

# In[6]:


import pandas as pd
df = pd.DataFrame({'animal' : ['alligator','bee','falcon','lion','monkey','parrot','shark','whale','zebra']})
print(df)
# ({'ddd':['aaa','bbb']}) ddd 는 헤더 aaa,bbb는 값


# In[4]:


print(df.head())


# In[5]:


print(df.head(-3))

