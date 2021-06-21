
# coding: utf-8

# In[10]:


#매개변수 지정하여 호출하기
# 1. 일반적인 함수

def add(a,b): # a, b는 매개변수
    return a,b,a+b

a,b,result=add(b=5,a=3)
print("%d +%d = %d" %(b,a,result))
print("-"*20)


# In[11]:


# 2. 입력값이 없는 함수

def say():
    return 'Hi'

print(say())


# In[19]:


# 3. 결과값이 없는 함수
# 결과값은 오직 return 명령어로만 돌려받을 수 있다.
def add2(a,b):
    print("%d, %d의 합은 %d입니다." %(a,b,a+b))
print(add2(3,4))
print("-"*20)


# In[13]:


# 4. 입력값도 결과값도 없는 함수
def say2():
    print('Hi')
    
say2()
print("-"*20)

