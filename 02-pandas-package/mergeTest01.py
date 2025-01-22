#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd

dict1 = {
    'name': ['홍길동', '홍길동', '김철수', '박영희', '김철수', '김철수', '홍길동'],
    'korean': range(7)
}
df1 = pd.DataFrame(dict1)

# DataFrame 출력 01
print(df1)


# In[16]:


dict2 = {
    'name': ['김철수', '홍길동', '심수봉'],
    'english': range(3)
}
df2 = pd.DataFrame(dict2)

# DataFrame 출력 02
print(df2)


# In[24]:


# merge 메소드의 on="name"을 이용하여 데이터 합치기
print(pd.merge(df1, df2, on='name'))


# In[26]:


# how='outer'이라고 명시하면 full outer join이 됨
print(pd.merge(df1, df2, how="outer"))


# In[30]:


# 컬럼 이름이 동일하지 않는 경우
dict3 = {
    'leftkey': ['홍길동', '홍길동', '김철수', '박영희', '김철수', '김철수', '홍길동'],
    'korean': range(7)
}
df3 = pd.DataFrame(dict3)

# DataFrame 출력 03
print(df3)


# In[40]:


dict4 = {
    'rightkey': ['김철수', '홍길동', '심수봉'],
    'english': range(3)
}
df4 = pd.DataFrame(dict4)

# DataFrame 출력 04
print(df4)


# In[44]:


# merge() 메소드의 left_on과 right_on 사용하기
print(pd.merge(df3, df4, left_on='leftkey', right_on='rightkey'))


# In[50]:


dict5 = {
    'key1': ['김철수', '김철수', '박영희'],
    'key2': ['one', 'two', 'three'],
    'leftval': [1,2,3]
}
left = pd.DataFrame(dict5)

# DataFrame 출력 05
print(left)


# In[52]:


dict6 = {
    'key1': ['김철수', '김철수', '박영희', '박영희'],
    'key2': ['one', 'one', 'one', 'two'],
    'rightval': [4, 5, 6, 7]
}
right = pd.DataFrame(dict6)

# DataFrame 출력 06
print(right)


# In[58]:


mylist = ['key1', 'key2'] # 조인할 컬럼 리스트

# 여러 개의 컬럼 병합하기
print(pd.merge(left, right, on=mylist, how='outer'))


# In[66]:


# suffixes 옵션 사용하기
# 동일한 컬럼 이름 key2에 대하여 접미사를 부텨준다.'
# print(pd.merge(left, right, on='key', suffixes=('_왼쪽', '_오른쪽')))


# In[72]:


# 색인을 이용한 머지 사용하기
newdf1 = df1.set_index('name')
print(newdf1)


# In[76]:


newdf2 = df2.set_index('name')
print(newdf2)


# In[78]:


print(pd.merge(newdf1, newdf2, left_index=True, right_index=True, how='outer', indicator=True))

