#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd

myindex = ['서울', '부산', '광주', '대구', '울산', '목포', '여수']
mylist = [50, 60, 70, 80, 90, 20, 40]
myseries = pd.Series(data=mylist, index=myindex)
print(myseries)


# In[28]:


# 색인의 이름으로 값 읽기'

print(myseries[['대구']])


# In[34]:


# 라벨 이름으로 슬라이싱

print(myseries['대구':'목포'])


# In[48]:


# 여러 개의 색인 이름으로 데이터 읽기

print(myseries[['대구', '여수']])


# In[54]:


# 정수를 이용한 데이터 읽기

print(myseries[[2]])


# In[58]:


#2, 4번째 데이터 읽기

print(myseries[0:5:2])


# In[64]:


# 1, 3, 5번째 데이터 읽기

print(myseries[[1, 3, 5]])


# In[68]:


# 슬라이싱 사용하기

print(myseries[3:6]) # from <= 결과 < to


# In[103]:


# 2번째 항목의 값 변경
myseries[2] = 22

# 2번째부터 4번째까지 항목의 값 변경
myseries[2:5] = 33

# 서울과 대구만 55로 변경
myseries[['서울', '대구']] = 55

# 짝수 행만 77로 변경
myseries[0::2] = 77

print(myseries)


# In[ ]:





# In[ ]:




