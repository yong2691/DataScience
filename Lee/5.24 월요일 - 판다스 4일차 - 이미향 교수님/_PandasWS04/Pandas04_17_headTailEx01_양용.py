
# coding: utf-8

# In[8]:


import pandas as pd
df = pd.read_csv("./../Data/gapminder.tsv", sep='\t')
print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[9]:


len(df)


# In[10]:


df.head()


# In[11]:


df[0:5]


# In[12]:


df.head(n=7)


# In[14]:


df.head(7)


# In[15]:


df.tail()


# In[17]:


df[len(df)-5:len(df)]


# In[19]:


df.tail(n=7)

