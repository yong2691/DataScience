
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


student1 = pd.Series({'국어':100,'영어':80,'수학':90})
print(student1)


# In[5]:


percentage = student1 / 200
print(type(percentage))
print(percentage)


# In[6]:


student1 = pd.Series({'국어':100,'영어':80,'수학':90})
student2 = pd.Series({'수학':100,'국어':90,'영어':80})
#위처럼 치면, 국영수 수국영 으로 순서가 다른데, 알아서 인덱스를 찾아서 간다.
print(student1)
print(student2)


# In[14]:


addition = student1 + student2
subtraction = student1 - student2
multiplication = student1 * student2
division = student1 / student2
print(type(division))


# In[19]:


result = pd.DataFrame([addition,substraction,multiplication,division],
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result,"\n",type(result))
print(addition,'\n',subtraction,'\n',multiplication,'n',division)

# 만약 국어 수학 영어 순으로 보기 싫고 바꾸고 싶으면?
# columns=['수학','영어','국어'] 이렇게 DataFrame 마지막부분에 넣어주면
# 수 국 영 순으로 바꿔줄 수 있다. DB에서는 순서는 신경쓰지 말라고 기본적으로 오름차순으로 디폴트되어있다.   

