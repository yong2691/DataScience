
# coding: utf-8

# In[5]:


import pandas as pd
s = pd.Series(['lama','cow','lama','beetle','lama','hippo'], name='animal')
s


# In[3]:


s.isin(['cow','lama'])

