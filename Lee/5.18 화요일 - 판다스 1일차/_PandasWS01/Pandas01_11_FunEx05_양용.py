
# coding: utf-8

# In[43]:


# 함수의 결괏값은 언제나 하나이다.
# 튜플값 하나인 (a+b, a*b)로 돌려준다.

def add_and_mul(a,b):
    return a+b,a*b

result=add_and_mul(3,4)
print(result)

#튜플 값을 2개의 결괏값처럼 받고 싶다면,
result1, result2 = add_and_mul(3,4)
print(result1, result2)


# In[40]:


def add_mul(choice,*args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result=result*i
    return result

result1 = add_mul('add',3,4)
print(result1)
print("-"*20)
result2 = add_mul('mul',3,4)
print(result2)
print("-"*20)


# In[29]:


# *가 있으면 튜플로 받아들여 여러 인자를 받을 수 있다.
def add_many(*args):
    result=0
    print(args)
    for i in args:
        print(i,end="\t")
        result=result+i
    return result

result1 = add_many(1,2)
print("=> 합 %d" %result1)
print("-"*20)

result2 = add_many(1,2,3)
print("=> 합 %d" %result2)
print("-"*20)

