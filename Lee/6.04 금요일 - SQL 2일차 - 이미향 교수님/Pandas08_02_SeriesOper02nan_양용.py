
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


student1 = pd.Series({'국어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80,'국어':90})

print(student1)
print(student2)

#np.nan은? numpy에서 nan 이라는 속성을 쓰면 결측치(NaN) 되는 것이다.


# In[12]:


#두 학생의 과목별 점수로 사칙연산 수행 (시리즈 vs 시리즈)
addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))

result = pd.DataFrame([addition, subtraction, multiplication, division],
                     index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result) #결과적으로 결측치 NaN이 존재하게 된다.


# In[11]:


#결측치를 없애려면, fill_value=0 을 사용한다.
sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)

result = pd.DataFrame([sr_add,sr_sub,sr_mul,sr_div],
                     index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)

