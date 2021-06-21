
# coding: utf-8

# In[24]:


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


# In[3]:


# sawonDB= df2.replace("'",'',regex=True)


# In[26]:


q2_list04 = []
for i in range(len(sawonDB)):
    q2_list04.append(sawonDB['sahire'][i][5:7] == '04')
sawonDB.loc[q2_list04]

