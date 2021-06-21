
# coding: utf-8

# In[1]:


import random


# In[17]:


print(random.random()) #seed를 안박아 놓으면? 계속해서 랜덤한수가나온다.


# In[19]:


random.seed(13)
print(random.random()) #seed 값을 박아놓으면, 계속 똑같은 수만 나오게 된다.

