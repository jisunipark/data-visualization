#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family="AppleGothic")
cnt, PNG, UNDERBAR = 0, '.png', '_'
CHART_NAME = 'barChartExam'
filename = '../../data/주요발생국가주간동향(4월2째주).csv'


# In[12]:


data = pd.read_csv(filename, index_col="국가")
data.columns


# In[14]:


chartdata = data['4월06일']
chartdata


# In[32]:


def MakeBarChart01(x, y, color, xlabel, ylabel, title):
    plt.figure()
    plt.bar(x, y, color=color, alpha=0.7)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)

    YTICKS_INTERVAL = 50000

    maxlim = (int(y.max() / YTICKS_INTERVAL) + 1) * YTICKS_INTERVAL
    print(maxlim)

    values = np.arange(0, maxlim + 1, YTICKS_INTERVAL)

    plt.yticks(values, ['%s' % format(val, ',') for val in values])

    # 그래프 위에 건수와 비율 구하기
    ratio = 100 * y / y.sum()
    print(ratio)
    print('-' * 40)

    plt.rc('font', size=6)
    for idx in range(y.size):
        value = format(y[idx], ',') + '건'
        ratioval = '%.1f%%.' % (ratio[idx])
        plt.text(x=idx, y=y[idx] + 1, s=value, horizontalalignment='center')
        plt.text(x=idx, y=y[idx], s=ratioval, horizontalalignment='center')

    meanval = y.mean()
    print(meanval)
    print('-' * 40)

    average = '평균 : %d건' % meanval
    plt.axhline(y=meanval, color='r', linewidth=1, linestyle='dashed')
    plt.text(x=y.size - 1, y=meanval + 200, s=average, horizontalalignment='center')

    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + ' 파일이 저장되었습니다.')


# In[36]:


colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
mycolor = colors[0:len(chartdata)]
MakeBarChart01(x=chartdata.index, y=chartdata, color=mycolor, xlabel='국가명', ylabel='발생건수', title='국가별 코로나 발생 건수')


# In[42]:


def MakeBarChart02(chartdata, rotation, title, ylim=None, stacked=False, yticks_interval=10000):
    plt.figure()
    chartdata.plot(kind='bar', rot=rotation, title=title, legend=True, stacked=stacked)

    plt.legend(loc='best')

    print('chartdata')
    print(chartdata)

    if stacked == False:
        maxlim = (int(max(chartdata.max()) / yticks_interval) + 1 ) * yticks_interval
        print('maxlim: ', maxlim)
        values = np.arange(0, maxlim + 1, yticks_interval)
        plt.yticks(values, ['%s' % format(val, ',') for val in values])

    if ylim != None:
        plt.ylim(ylim)
    global cnt
    cnt = cnt + 1
    savefile = CHART_NAME + UNDERBAR + str(cnt).zfill(2) + PNG
    plt.savefig(savefile, dpi=400)
    print(savefile + " 파일이 저장되었습니다.")


# In[48]:


data = pd.read_csv(filename, index_col='국가')
print(data.columns)


# In[50]:


COUNTRY = ['프랑스', '중국', '영국', '이란']
WHEN = ['4월06일', '4월07일', '4월08일']
data = data.loc[COUNTRY, WHEN]

data


# In[52]:


data.index.name = '국가명'
data.columns.name = '일자'

MakeBarChart02(chartdata=data, rotation=0, title='국가별 일별 발생 건수')


# In[ ]:




