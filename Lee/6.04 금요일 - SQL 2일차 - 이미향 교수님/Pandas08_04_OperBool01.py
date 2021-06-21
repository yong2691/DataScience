
# coding: utf-8

# In[2]:


import pandas as pd
scientists = pd.read_csv('../data/scientists.csv')


# In[8]:


ages = scientists['Age']
print(ages.max())
print(type(ages))


# In[4]:


print(ages.mean())


# In[5]:


print(ages>ages.mean())


# In[9]:


print(ages[ages>ages.mean()])
#ages 라는 시리즈에서 True인것만 값을 가져오기


# In[10]:


print(type(ages > ages.mean()))


# In[12]:


manual_bool_values = [True, True, True, False, True, True, False, True]
print(ages[manual_bool_values])
#True라고 친것만 프린트가 된다.

