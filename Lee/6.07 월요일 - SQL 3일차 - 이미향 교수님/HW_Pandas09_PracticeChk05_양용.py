
# coding: utf-8

# In[1]:


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


# In[4]:


q3_sabun = sawonDB[sawonDB['sabun']%2 == 0]
q3_sabun

