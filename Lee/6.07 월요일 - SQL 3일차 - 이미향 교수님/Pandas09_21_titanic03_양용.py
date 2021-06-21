
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[2]:


titanic = sns.load_dataset('titanic')


# In[10]:


age0 = titanic[(titanic['age']>=0)&(titanic['age']<10)]
age10 = titanic[(titanic['age']>=10)&(titanic['age']<20)]
age20 = titanic[(titanic['age']>=20)&(titanic['age']<30)]
age30 = titanic[(titanic['age']>=30)&(titanic['age']<40)]
age40 = titanic[(titanic['age']>=40)&(titanic['age']<50)]
age50 = titanic[(titanic['age']>=50)&(titanic['age']<60)]
age60 = titanic[(titanic['age']>=60)&(titanic['age']<70)]
age70 = titanic[(titanic['age']>=70)&(titanic['age']<80)]
age80 = titanic[(titanic['age']>=80)&(titanic['age']<90)]


# In[6]:


print("10세 미만 사망자수: ", len(age0['survived']==0))
print("10대 사망자수: ", len(age10['survived']==0))
print("20대 사망자수: ", len(age20['survived']==0))
print("30대 사망자수: ", len(age30['survived']==0))
print("40대 사망자수: ", len(age40['survived']==0))
print("50대 사망자수: ", len(age50['survived']==0))
print("60대 사망자수: ", len(age60['survived']==0))
print("70대 사망자수: ", len(age70['survived']==0))
print("80대 사망자수: ", len(age80['survived']==0))

