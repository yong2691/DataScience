
# coding: utf-8

# In[43]:


import pandas as pd
df1 = pd.read_excel('./../DataSet/datalabPractice01.xlsx')
df2 = pd.read_excel('./../DataSet/datalabPractice01.xlsx',
                    sheet_name="Sheet1", usecols=[0,1,2], skiprows=[0],
                    skipfooter=5, header = None)
#skiprows=[0] 는 idx 0번 행을 스킵.
#skipfooter = 2 는 idx 맨 뒤에부터 2개를 스킵.
#header = None 맨위에 값을 해더로 쓰지 않는다.
print(df2.columns,"\n")
print(df2,"\n")
print(df1)

