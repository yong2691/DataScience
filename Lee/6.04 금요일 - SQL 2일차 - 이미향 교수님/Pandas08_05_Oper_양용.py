
# coding: utf-8

# In[3]:


import pandas as pd
scientists = pd.read_csv('../data/scientists.csv')
ages = scientists['Age']


# In[4]:


print(ages + ages)


# In[5]:


print(ages+100)


# In[6]:


print(ages*2)


# In[9]:


print(pd.Series([1,100]))


# In[10]:


print(ages)
print(pd.Series([1,100]))
print(ages + pd.Series([1,100]))


# In[14]:


print(ages)


# In[15]:


rev_ages = ages.sort_index(ascending=False)
print(rev_ages)


# In[17]:


print(ages+rev_ages)
print(ages*2)
# 두개의 값은 같은 값이 나온다. ages + rev_ages 를 할 때,
# 그냥 순서대로 더하는게 아니고 인덱스값을 찾아서 맞는애들끼리 더해진다.

