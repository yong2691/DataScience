
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


deptDB = pd.read_csv('./../data/deptDB.csv',header=None)
sawonDB = pd.read_csv('./../data/sawonDB.csv',header=None)
gogekDB = pd.read_csv('./../data/gogekDB.csv',header=None)


# In[5]:





# In[4]:


deptDB.columns = ['deptno','dname','loc']

sawonDB.columns = ['sabun','saname','deptno','sajob','sapay','sahire',
                  'sasex','samgr']

gogekDB.columns = ['gobun','goname','gotel','gojumin','godam']

deptDB = deptDB.replace("'","",regex=True)
sawonDB = sawonDB.replace("'","",regex=True)
gogekDB = gogekDB.replace("'","",regex=True)

