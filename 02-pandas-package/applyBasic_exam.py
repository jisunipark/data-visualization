#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd

filename = '../data/memberInfo_exam.csv'
df = pd.read_csv(filename, index_col='이름')
df


# In[6]:


def sungjuk(midterm):
    if midterm >= 90:
       return '수'
    elif midterm >= 80:
        return '우'
    elif midterm >= 70:
        return '미'
    elif midterm >= 60:
        return '양'
    else:
        return '가'


# In[8]:


sq = df['중간'].apply(sungjuk)
sq


# In[ ]:




