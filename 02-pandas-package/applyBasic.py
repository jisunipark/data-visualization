#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd

filename = '../data/memberInfo.csv'
df = pd.read_csv(filename, index_col='id')

print('시리즈와 메서드')
print(df)


# In[8]:


print('일반적인 산술 연산')
print(df['kor'] + 5)


# In[20]:


def plus5(x):
    return x + 5

print('apply 함수를 적용한 결과')
sq = df['kor'].apply(plus5)
print(sq)


# In[26]:


def gob(x, n):
    return n * x

ex = df['kor'].apply(gob, n=2)
print(ex)
print('-' * 30)

ex = df['kor'].apply(gob, n=3)
print(ex)
print('-' * 30)


# In[38]:


def applyByColumn(col):    
    mysum = 0
    for item in col:
        mysum += item
    return mysum / df.shape[0]
print(df.apply(applyByColumn, axis=0))


# In[44]:


def applyByRow(row):
    mysum = 0
    for item in row:
        mysum += item
    return mysum / df.shape[1]
print(df.apply(applyByRow, axis=1))

