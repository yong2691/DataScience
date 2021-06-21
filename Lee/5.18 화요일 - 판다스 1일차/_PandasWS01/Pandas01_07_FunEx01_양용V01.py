
# coding: utf-8

# # 기본 함수 선언 연습 01
# ## 기본 함수 선언 연습 01
# ### 기본 함수 선언 연습 01
# 
# <h1> 기본 연습 </h1>
# <h2> 기본 연습 </h2>
# <h3> 기본 연습 </h3>
# <h4> 기본 연습 </h4>
# <h5> 기본 연습 </h5>
# HTML : Hyper Text Markup Language
# (하이퍼링크를 지원해주는 텍스트) <, >, /

# In[ ]:


def add(a,b): #a,b 는 매개변수
    return a+b #이렇게 하면 add(a,b) 라고 치면 a+b가 되는 함수를 만든 것이다.

a=3
b=4
c=add(a,b) #3,4는 인수

print("%d+%d = : %d" %(a,b,c))

#return은 나를 부른 곳으로 반환한다.


# In[ ]:


def add(a,b):
    return a,b,a+b

a,b,result=add(b=5,a=3)
print()


# In[5]:


def say():
    return 'Hi'

print(say())


# In[ ]:


def add2(a,b):
    print()

