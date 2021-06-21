
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame({'col1':[1,2],'col2':[3,4]})


# In[3]:


print(df)


# In[5]:


df = pd.DataFrame({'col1':[1,2],'col2':[3,4],'col3':[5,6]})
print(df)


# In[6]:


df.shape #shape치면 2행 3열 나온다.

