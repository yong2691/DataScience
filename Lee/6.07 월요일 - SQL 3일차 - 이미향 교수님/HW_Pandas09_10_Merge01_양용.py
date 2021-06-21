
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


df1 = pd.DataFrame({'a':['foo','bar'], 'b':[1,2]})
df2 = pd.DataFrame({'a':['foo','baz'], 'c':[3,4]})


# In[6]:


df1


# In[7]:


df2


# In[8]:


df1.merge(df2, how='inner', on = 'a')


# In[10]:


df1.merge(df2, how='left', on='a')


# In[13]:


df1.merge(df2,how='right', on='a')

