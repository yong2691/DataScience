
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


s = pd.Series(['1. Ant.  ', '2. Bee!\n','3. Cat?\t', np.nan])
s


# In[6]:


s.str.strip()


# In[7]:


s.str.strip('.')


# In[23]:


s.str.strip('123.!? \n\t')

