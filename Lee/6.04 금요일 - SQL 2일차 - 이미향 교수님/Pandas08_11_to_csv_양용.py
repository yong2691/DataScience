
# coding: utf-8

# In[2]:


#2.7_to_csv.py
import pandas as pd

data = {'name':['Jerry','Riah','Paul'],
       'algol' : ["A","A+","B"],
       'basic' : ["C", "B", "B+"],
       'c++' : ["B+","C","C+"],
       }
df = pd.DataFrame(data)

df.set_index('name', inplace=True) #'name' 컬럼을 인덱스로 쓰겠다.
print(df)

df.to_csv("./df_sample.csv")

