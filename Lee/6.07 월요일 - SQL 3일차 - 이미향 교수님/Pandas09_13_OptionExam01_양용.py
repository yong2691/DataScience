
# coding: utf-8

# In[23]:


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


# In[68]:


deptSawon = deptDB.merge(sawonDB, how='inner', on='deptno')
deptSawon


# In[72]:


name = input('이름을 입력하세요.')
# result = deptSawon[deptSawon['saname'] == name]
# deptSawon[deptSawon['saname'] == name]['sapay']
#int를 안붙여서 에러가 계속 났다.

if int(deptSawon[deptSawon['saname'] == name]['sapay'])  >= 3000:
    print('고소득자')
elif int(deptSawon[deptSawon['saname'] == name]['sapay']) >= 2000:
    print('중위소득자')
else:
    print('월급조정대상자')

