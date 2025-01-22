#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas

df = pandas.read_csv('../data/welfare.csv')
print(df.head())


# In[10]:


print(type(df))
print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[12]:


print(df.columns)


# In[14]:


print(df.dtypes)


# In[16]:


print(df.info())


# In[18]:


gender_df = df['gender']
print(gender_df)


# In[22]:


print(type(gender_df))


# In[24]:


print(gender_df.head())
print(gender_df.tail())


# In[28]:


subset = df[['gender', 'birth', 'marriage']]
print(type(subset))
print(subset.head())
print(subset.tail())


# In[34]:


print(df.loc[0])


# In[38]:


print(df.loc[1])


# In[48]:


number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1

print(df.loc[last_row_index])


# In[56]:


print(df.tail(n=1))
print(df.tail(n=2))
print(df.loc[[0,99,999]])


# In[64]:


subset_loc = df.loc[0]
subset_tail = df.tail(n=1)
print(type(subset_loc))
print(type(subset_tail))


# In[66]:


print(df.iloc[1])


# In[76]:


subset = df.loc[:, ['marriage', 'income']]
print(subset.head())


# In[78]:


subset = df.iloc[:, [2, 4, -1]]
print(subset.head())


# In[82]:


small_range = list(range(5))
print(small_range)


# In[84]:


print(type(small_range))


# In[90]:


small_range = list(range(3, 6))
print(small_range)


# In[92]:


subset = df.iloc[:, small_range]
print(subset.head())


# In[94]:


print(df['marriage'].unique())


# In[96]:


print(df.groupby('marriage')['code_religion'].mean())


# In[98]:


mygrouping = df.groupby('marriage')
print(type(mygrouping))
print(mygrouping)


# In[100]:


grp_code_religion = mygrouping['code_religion']
print(type(grp_code_religion))


# In[102]:


mean_code_religion = grp_code_religion.mean()
print(mean_code_religion)


# In[104]:


mean_code_religion = grp_code_religion.mean()
print(mean_code_religion)


# In[ ]:




