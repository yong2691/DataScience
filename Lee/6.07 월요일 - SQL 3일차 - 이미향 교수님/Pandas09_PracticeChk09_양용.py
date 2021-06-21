
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


# In[4]:


#문제 07] sawonDB 데이터에서 전산부 직원의 평균연봉 출력

q7_com_30 = sawonDB[sawonDB['deptno']==30]
print("전산부 직원의 평균 연봉 :",q7_com_30['sapay'].mean())

