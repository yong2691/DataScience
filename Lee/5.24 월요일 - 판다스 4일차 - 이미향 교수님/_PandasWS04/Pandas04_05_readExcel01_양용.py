
# coding: utf-8

# In[8]:


import pandas as pd
file_path = "./../data/gapminder.tsv"
df01 = pd.read_csv(file_path, sep = '\t')
print(df01, '\n')


# In[9]:


import pandas as pd
file_pathExcel = "./../dataset/datalabPractice01.xlsx"
dfExcel = pd.read_excel(file_pathExcel)
print(dfExcel)

