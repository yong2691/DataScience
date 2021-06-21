
# coding: utf-8

# In[38]:


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

result1 = add_mul('add',2,3)
print(result1)
print("-"*20)
result2 = add_mul('mul',2,3)
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

