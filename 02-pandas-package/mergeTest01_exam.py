#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[8]:


data1 = {
    '이름': ['유관순', '유관순', '황진이', '황진이', '유관순'],
    '중간': list(range(10, 51, 10))
}
df1 = pd.DataFrame(data1)
df1


# In[26]:


data2 = {
    '이름': ['황진이', '유관순', '신사임당'],
    '기말': list(range(30, 51, 10))
}
df2 = pd.DataFrame(data2)
df2


# In[28]:


result1 = pd.merge(df1, df2, on="이름")
result1


# In[32]:


result2 = pd.merge(df1, df2, how='right')
result2


# In[34]:


result3 = pd.merge(df1, df2, how='left')
result3


# In[ ]:




