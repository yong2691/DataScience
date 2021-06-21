
# coding: utf-8

# In[17]:


import pandas as pd

url = './../DataSet/Test01.html'

tables = pd.read_html(url)

print(len(tables), '\n==>')

print(tables, "\n==>")

for i in range(len(tables)):
    print("tables[%s]" %i, '\n')
    print(tables[i], '\b')

df = tables[1]
print(df.columns,"\n")

