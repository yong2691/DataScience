
# coding: utf-8

# In[5]:


import pandas as pd
scientists = pd.read_csv('./../data/scientists.csv')
print(scientists['Born'].dtype)
print(scientists['Died'].dtype)
print(scientists)
print(scientists['Born'])


# In[8]:


born_datetime = pd.to_datetime(scientists['Born'],format='%Y-%m-%d')
print(born_datetime)


# In[9]:


died_datetime = pd.to_datetime(scientists['Died'],format='%Y-%m-%d')
print(died_datetime)


# In[10]:


scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
print(scientists)

