#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[8]:


# 값 설정
myindex = ['이순신', '김유신', '강감찬', '광해군', '연산군']
mycolumns = ['서울', '부산', '광주', '목포', '경주']
mylist = list(10 * onedata for onedata in range(1, 26))
print(mylist)


# In[12]:


myframe = pd.DataFrame(np.reshape(mylist, (5, 5)), index=myindex, columns=mycolumns)
print(myframe)


# In[20]:


# 1행만 Series로 읽어 오기
result = myframe.iloc[1]
print(type(result))
print(result)


# In[44]:


# 몇개의 행을 읽어 오기
result = myframe.iloc[[1,3]]
print(type(result))
print(result)


# In[32]:


# 짝수행만 가져오기
result = myframe[0::2]
print(result)


# In[36]:


# 이순신 행만 Series로 읽어오기
result = myframe.loc['이순신']
print(type(result))
print(result)


# In[38]:


# 이순신 행만 DataFrame으로 읽어오기
result = myframe.loc[['이순신']]
print(type(result))
print(result)


# In[40]:


# 강감찬과 이순신 행 읽어오기
result = myframe.loc[['이순신', '강감찬']]
print(type(result))
print(result)


# In[48]:


print(myframe.index)
print('-' * 40)


# In[56]:


mytarget = np.random.choice(myframe.index, 3)
print(mytarget)
print('-' * 40)


# In[58]:


mytarget = np.random.choice(myframe.index, 3)
result = myframe.loc[mytarget]
print(result)


# In[64]:


# 강감찬의 광주 실력 정보 가져오기
result = myframe.loc[["강감찬"], ["광주"]]
print(result)


# In[66]:


# 연산군과 광해군의 광주/목포 정보 가져오기
result = myframe.loc[['연산군', '광해군'], ['광주', '목포']]
print(result)


# In[70]:


# 연속적인 데이터 가져오기
result = myframe.loc['김유신':'광해군', '광주':'목포']
print(result)


# In[72]:


# 김유신 ~ 광해군까지 부산 실적 정보 가져오기
result = myframe.loc['김유신':'광해군', ['부산']]
print(result)


# In[74]:


# Boolean으로 데이터 처리하기
result = myframe.loc[[False, True, True, False, True]]
print(result)


# In[78]:


# 부산 실적이 100이하인 항목들
result = myframe.loc[myframe['부산'] <= 100]
print(result)


# In[80]:


# 목포 실적이 140인 항목들
result = myframe.loc[myframe['목포'] == 140]
print(result)


# In[84]:


cond1 = myframe['부산'] >= 70
cond2 = myframe['목포'] >= 140
print(type(cond1))
print(cond1)
print(cond2)


# In[88]:


df = pd.DataFrame([cond1, cond2])
print(df)
print('-' * 40)
print(df.all())
print('-' * 40)


# In[90]:


print(df.any())
print('-' * 40)


# In[92]:


result = myframe.loc[df.all()]
print(result)
print('-' * 40)


# In[94]:


result = myframe.loc[df.any()]
print(result)
print('-' * 40)


# In[98]:


# 람다 함수의 사용
result = myframe.loc[lambda df: df['광주'] >= 130]
print(result)


# In[134]:


# 이순신과 강감찬의 부산 실적을 30으로 변경하기
myframe.loc[['이순신', '강감찬'], ['부산']]
print(myframe)


# In[132]:


# 김유신부터 광해군까지 경주 실적을 80으로 변경하기
myframe.loc['김유신':'광해군', ['경주']] = 80
print(myframe)


# In[130]:


# 연산군의 모든 실적을 50으로 변경하기
myframe.loc[['연산군'], :] = 50
print(myframe)


# In[128]:


# 모든 사람의 광주 컬럼을 60으로 변경하기
myframe.loc[:, ['광주']] = 60
print(myframe)


# In[136]:


# 경주 실적이 150 이하인 데이터를 모두 0으로 변경하기
myframe.loc[myframe['경주'] <= 150, ['경주']] = 0
print(myframe)


# In[138]:


# 데이터 프레임 사용하기
print(myframe)


# In[ ]:




