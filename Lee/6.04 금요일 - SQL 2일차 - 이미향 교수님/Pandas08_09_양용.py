
# coding: utf-8

# In[1]:


import pandas as pd
scientists = pd.read_csv('./../data/scientists.csv')


# In[4]:


import random

random.seed(42)
random.shuffle(scientists['Age'])
print(scientists['Age'])


# In[11]:


random.shuffle(scientists['Age'])
print(scientists['Age'])

