
# coding: utf-8

# In[7]:


import pandas as pd
sawonDB = pd.read_csv('./../data/sawonDB.csv',header=None)
sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr']
sawonDB['saname'] = sawonDB['saname'].str.strip("' ")
sawonDB['sajob'] = sawonDB['sajob'].str.strip("' ")
sawonDB['sahire'] = sawonDB['sahire'].str.strip("' ")
sawonDB['sasex'] = sawonDB['sasex'].str.strip("' ") #전처리
sawonDB


# In[12]:


#문제 01 ] SawonDB 데이터에서 입사년도가 88년도인 사원 출력

q2_list88 = []
for i in range(len(sawonDB)):
    q2_list88.append(sawonDB['sahire'][i][0:4] == '1988')
sawonDB.loc[q2_list88]


# In[8]:


#문제 01 ] SawonDB 데이터에서 입사년도가 88년도인 사원 출력
'''
sawonDB = pd.read_csv('./../data/sawonDB.csv',header=None)
sawonDB.columns=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr']
sawonDB2 = sawonDB.replace("'",'',regex=True)

sawonDB2['sahire'] = pd.to_datetime(sawonDB2['sahire']) # 판다스의 to_datetime 함수를 통해 년월일로 바꿔라.
sawonDB2['year'] = sawonDB2['sahire'].dt.year 
sawonDB2[sawonDB2['year']==1988]
'''
#print(df22[df22['year']==1988]['saname'])

