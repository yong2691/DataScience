
# coding: utf-8

# In[12]:


import pandas as pd #데이터로부터 유용한 데이터를 불러올때 판다스를 사용
file_path = "./../dataset/read_csv_sample.csv"
df1 = pd.read_csv(file_path)
print(df1, '\n')
print(type(df1))


# In[14]:


df2 = pd.read_csv(file_path, header = None)
print(df2, '\n')


# In[15]:


df3 = pd.read_csv(file_path, index_col=None)
print(df3, '\n')


# In[16]:


df4 = pd.read_csv(file_path, index_col='c0')
print(df4, '\n')

