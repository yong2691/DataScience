
# coding: utf-8

# In[3]:


import pandas as pd


# In[10]:


df = pd.read_csv('./data/gapminder.tsv',sep='\t')


# In[11]:


country_df = df['country'] # country column만 불러오니까 이건 series 타입이다.
print(type(country_df))


# In[18]:


print(country_df.head()) #이거 한줄씩 쓸때는 print 굳이 쓸 핑료 없다.


# In[13]:


print(country_df.tail())


# In[14]:


subset = df[['country','continent','year']]
print(type(subset))


# In[15]:


print(subset.head())


# In[16]:


print(subset.tail())

