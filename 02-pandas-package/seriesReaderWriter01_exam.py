#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd

myindex = ['마포구', '용산구', '서대문구', '동대문구', '은평구', '구로구', '강서구']
mylist = [40, 80, 70, 50, 60, 30, 20]
myseries = pd.Series(data=mylist, index=myindex)
myseries


# In[12]:


# 은평구만 조회
myseries['은평구']


# In[14]:


# '서대문구'부터 '구로구'까지 조회
myseries['서대문구':'구로구']


# In[18]:


# '용산구'와 '동대문구'만 조회
myseries[['용산구', '동대문구']]


# In[28]:


# 2번째 요소만 조회
myseries[1]
myseries.iloc[1]


# In[32]:


myseries[[0,2,4]]


# In[34]:


myseries[[1,3,4]]


# In[36]:


myseries[2:5]


# In[38]:


myseries.iloc[2] = 99
myseries


# In[40]:


myseries[2:5] = 66
myseries


# In[42]:


myseries[['마포구', '강서구']] = 55
myseries


# In[44]:


myseries[::2] = 77
myseries


# In[ ]:




