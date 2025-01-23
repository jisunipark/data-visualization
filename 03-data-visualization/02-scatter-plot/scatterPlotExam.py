#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'scatterPlotExam'
filename = '../../data/mpg.csv'
plt.style.use('ggplot')

print('스타일 목록')
print(plt.style.available)


# In[10]:


msg = pd.read_csv(filename, encoding='utf-8')
msg.head()


# In[16]:


msg.info()


# In[42]:


xdata = msg.loc[:, ['displ']]
ydata = msg.loc[:, ['hwy']]

plt.figure()
plt.plot(xdata, ydata, marker='o', linestyle='None')
plt.xlabel('엔진 크기')
plt.ylabel('주행 마일수')
plt.title('산점도 그래프')
plt.grid(True)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + ' 파일이 저장되었습니다.')


# In[46]:


mycolors = ['r', 'g', 'b'] # 항목을 구분할 색상 리스트
label_dict = {
    'f': '전륜 구동',
    '4': '사륜 구동',
    'r': '후륜 구동',
}


# In[54]:


plt.figure()

idx = 0 # 색상 구분을 위한 카운터 변수
labels = msg['drv'].unique() # ['f', '4' ,'r']

for finditem in labels:
    xdata = msg.loc[msg['drv'] == finditem, 'displ']
    ydata = msg.loc[msg['drv'] == finditem, 'hwy']
    plt.plot(xdata, ydata, color=mycolors[idx], marker="o", linestyle="None", label=label_dict[finditem])
    idx += 1
    
plt.legend()
plt.xlabel('엔진 크기')
plt.ylabel('주행 마일수')
plt.title('산점도 그래프')
plt.grid(True)

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + ' 파일이 저장되었습니다.')


# In[77]:


fig = plt.figure(figsize=(16, 10), dpi=80)
grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)

# 축 정의
ax_main = fig.add_subplot(grid[:-1, :-1])
ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

# 메인 산점도
ax_main.scatter('displ', 'hwy', s=msg.cty*4, c=msg.manufacturer.astype('category').cat.codes, alpha=.9, data=msg, cmap='tab10', edgecolors='gray', linewidths=.5)

# 하단 히스토그램
ax_bottom.hist(msg.displ, 40, histtype='stepfilled', orientation='vertical', color='lightpink')
ax_bottom.invert_yaxis()

# 오른쪽 히스토그램
ax_right.hist(msg.hwy, 40, histtype='stepfilled', orientation='horizontal', color='lightblue')

# Decorations
ax_main.set(title='산점도(엔진의 크기 vs 주행 마일수)', xlabel='엔진의 크기', ylabel='주행 마일수')
ax_main.title.set_fontsize(20)
for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
    item.set_fontsize(14)

xlabels = ax_main.get_xticks().tolist()
cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + ' 파일이 저장되었습니다.')


# In[123]:


diamond_file = '../../data/diamonds.csv'

diamonds = pd.read_csv(diamond_file)
diamonds


# In[125]:


FRACTION = 0.005
diamonds = diamonds.sample(frac=FRACTION)
diamonds.columns


# In[127]:


diamonds.describe()


# In[129]:


diamonds.head()


# In[131]:


xdata = diamonds['price']
ydata = diamonds['depth']
table = diamonds['table']

table.max()


# In[133]:


table.min()


# In[137]:


mycolor = ['r', 'g', 'b', 'y', 'm']
cut_list = diamonds['cut'].unique()
cut_list


# In[141]:


cut_dict = {cut_list[idx]: mycolor[idx] for idx in range(len(cut_list))}
cut_dict


# In[147]:


def recode_cut(cut):
    return cut_dict[cut]

diamonds['newcut'] = diamonds['cut'].apply(recode_cut)
newcut = diamonds['newcut']

newcut


# In[151]:


def recode_table(table):
    if table >= 60:
        return 100
    elif table >= 58:
        return 30
    elif table >= 54:
        return 5
    else:
        return 1

diamonds['newtable'] = diamonds['table'].apply(recode_table)
newtable = diamonds['newtable']
newtable


# In[155]:


diamonds.loc[:, ['price', 'depth', 'newtable', 'table', 'newcut']]


# In[161]:


scatter_plot = plt.figure()
ax1 = scatter_plot.add_subplot(1,1,1)

ax1.scatter(x=xdata, y=ydata, s=newtable, c=newcut, alpha=0.8)

ax1.set_title('Price vs Depth Colored by Cut and Table')
ax1.set_xlabel('Price')
ax1.set_ylabel('Depth')

cnt += 1
savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
plt.savefig(savefile, dpi=400)
print(savefile + ' 파일이 저장되었습니다.')


# In[ ]:




