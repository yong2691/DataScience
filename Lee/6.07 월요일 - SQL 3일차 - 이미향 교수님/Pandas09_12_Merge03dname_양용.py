
# coding: utf-8

# In[6]:


import pandas as pd

deptDB = pd.read_csv('./../data/deptDB.csv',header=None)
sawonDB = pd.read_csv('./../data/sawonDB.csv',header=None)
gogekDB = pd.read_csv('./../data/gogekDB.csv',header=None)

deptDB.columns = ['deptno','dname','loc']

sawonDB.columns = ['sabun','saname','deptno','sajob','sapay','sahire',
                  'sasex','samgr']

gogekDB.columns = ['gobun','goname','gotel','gojumin','godam']

deptDB = deptDB.replace("'","",regex=True)
sawonDB = sawonDB.replace("'","",regex=True)
gogekDB = gogekDB.replace("'","",regex=True)
#쓰레기값이 많으니까, 쿼테이션을 지우는 전처리 과정이다.


# In[66]:


deptSawon = deptDB.merge(sawonDB, how='inner', on = 'deptno')
deptSawon.head()

deptSawon['dname'].str.strip()

deptSawon


# In[71]:


q7_com_30 = deptSawon[deptSawon['dname'] == ' 전산부']
print("전산부 직원의 평균 연봉 : ", q7_com_30['sapay'].mean())

