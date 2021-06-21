
# coding: utf-8

# In[4]:


import pandas as pd
scientists = pd.read_csv('../data/scientists.csv')
ages = scientists['Age']
print(ages)


# In[2]:


print(scientists[scientists['Age'] > scientists['Age'].mean()])


# In[3]:


print(scientists.loc[[True,True,False,True]])


# In[5]:


print(scientists * 2)

