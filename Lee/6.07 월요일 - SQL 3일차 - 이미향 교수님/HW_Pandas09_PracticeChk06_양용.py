
# coding: utf-8

# In[2]:


import pandas as pd

s1 = pd.Series(['Mouse','dog','house and parrot','23'])
s1.str.contains('og')


# In[3]:


ind = pd.Index(['Mouse','dog','23house and parrot','23.0'])
ind.str.contains('23')


# In[7]:


s1.str.contains('oG', case=False)


# In[8]:


s1.str.contains('house|dog') #or연산자


# In[13]:


s1.str.contains('\\d') # 숫자가 있는지를 확인


# In[10]:


s2 = pd.Series(['40','40.0','41','41.0','35'])
s2.str.contains('.0') #.하고 0하고 둘중 하나라도 있으면 인식

