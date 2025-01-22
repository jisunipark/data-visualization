#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

myindex = ['김구', '이봉창', '안중근', '윤봉길']
mycolumns = ['강남구', '은평구', '마포구', '용산구']
mylist = list(10 * onedata for onedata in range(1, 17))
myframe = pd.DataFrame(np.reshape(mylist, (4,4)), index=myindex, columns=mycolumns)
myframe


# In[8]:


myframe.iloc[1]


# In[10]:


myframe.iloc[[1, 3]]


# In[37]:


myframe.loc[['윤봉길']]


# In[14]:


myframe.loc[['이봉창', '윤봉길']]


# In[20]:


myframe.loc[['윤봉길'], ['은평구']]


# In[25]:


myframe.loc[['김구', '이봉창'], ['용산구', '은평구']]


# In[27]:


myframe.loc[myframe['은평구'] <= 100]


# In[29]:


myframe.loc[myframe['은평구'] == 100]


# In[35]:


myframe.loc['김구':'안중근', ['용산구']] = 80
myframe


# In[ ]:




