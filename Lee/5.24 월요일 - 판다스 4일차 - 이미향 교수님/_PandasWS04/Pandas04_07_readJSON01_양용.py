
# coding: utf-8

# In[5]:


import pandas as pd

df = pd.read_json('./../dataset/read_json_sample.json')
print(df,'\n')
print(df.index) # index를 표시한다.

