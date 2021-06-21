
# coding: utf-8

# In[1]:


import pandas as pd

deptDB = pd.read_csv('./../data/deptDB.csv',header=None)
sawonDB = pd.read_csv('./../data/sawonDB.csv',header=None)
gogekDB = pd.read_csv('./../data/gogekDB.csv',header=None)
deptDB.columns = ['deptno','dname','loc']
sawonDB.columns = ['sabun','saname','deptno','sajob','sapay','sahire',
                  'sasex','samgr']
gogekDB.columns = ['gobun','goname','gotel','gojumin','godam']

deptDB['dname'] = deptDB['dname'].str.strip("' ")
deptDB['loc'] = deptDB['loc'].str.strip("' ")

sawonDB['saname'] = sawonDB['saname'].str.strip("' ")
sawonDB['sajob'] = sawonDB['sajob'].str.strip("' ")
sawonDB['sahire'] = sawonDB['sahire'].str.strip("' ")
sawonDB['sasex'] = sawonDB['sasex'].str.strip("' ")

gogekDB['goname'] = gogekDB['goname'].str.strip("' ")
gogekDB['gojumin'] = gogekDB['gojumin'].str.strip("' ")
gogekDB['gotel'] = gogekDB['gotel'].str.strip("' ")

# 쓰레기값이 많으니까, 쿼테이션을 지우는 전처리 과정이다.
# strip("' ") 이렇게쓰면, '도 지우고 눈에 보이지않는 화이트 스페이스도 지울 수 있따.


# In[12]:


# 문제 08] 컬럼 이름순 재배치, sort_values() 함수 적용 Chk

# columns = list(sawonDB.columns.values)
# columns_sorted = sorted(columns)
# df_sorted = sawonDB[columns_sorted]
# df_sorted

columnsSort = sawonDB.columns.sort_values(ascending=True) # 디폴트가 오름차순
columnsSort

sawonDB[columnsSort]

