
# coding: utf-8

# In[3]:


import pandas as pd
sawonDB = pd.read_csv('./../data/sawonDB.csv',header=None)
#전처리
sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr']
sawonDB['saname'] = sawonDB['saname'].str.strip("' ")
sawonDB['sajob'] = sawonDB['sajob'].str.strip("' ")
sawonDB['sahire'] = sawonDB['sahire'].str.strip("' ")
sawonDB['sasex'] = sawonDB['sasex'].str.strip("' ")
sawonDB
#"' " 이런식으로 스페이스를 띄어야 된다.


# In[7]:


#1 문제
sawon_1988 = sawonDB[sawonDB['sahire'].str.contains('1988')]
print(sawon_1988)


# In[9]:


#2 문제

sawon_april = sawonDB[sawonDB['sahire'].str.contains('/04/')]
print(sawon_april)


# In[12]:


#3 문제

slist = []
for i, value in enumerate(sawonDB['sabun']):
    if value % 2 == 0 :
        slist.append(i)


# In[20]:


sawonDB.iloc[slist]

