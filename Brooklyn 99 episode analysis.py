#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data= pd.read_csv('D:/Internship/Project/brooklyn99_episodes.csv')
data 
data.columns
data.isnull().sum()
data[['year','month','day']]=data['original_air_date'].str.split('-',expand=True) 
color = ['#C3073F','#1A1A1D', '#4E4E50', '#C5C6C7', '#6F2232', '#950740'] 

#How Much Eposides are yealy release?#

fig = plt.figure(figsize=(12,5))
sns.barplot(x=data['year'].value_counts().index,y=data['year'].value_counts().values,palette=color)
sns.despine()
plt.title('Year of Episodes Distripution',weight='bold',fontsize=20)

#How much monthly release episode and yealy?#

month = data['month'].value_counts().reset_index().sort_values('index',ascending=False)
month.columns=['month','counts']

fig,ax = plt.subplots(1,2,figsize=(12,5))
sns.barplot(x=data['year'].value_counts().index,y=data['year'].value_counts().values,
            ax=ax[0],palette=color)
sns.barplot(x=month['month'],y=month['counts'],ax=ax[1],palette=color)
sns.despine()
plt.suptitle('Year & Month Episode Distripution',weight='bold',fontsize=20)

#Which Director runs the more episodes?#

fig = plt.figure(figsize=(14,5))
ax[0]=sns.lineplot(x=data['directed_by'].value_counts().index,y=data['directed_by'].value_counts().values,
             markers='markers')
ax[0]=sns.barplot(x=data['directed_by'].value_counts().index,y=data['directed_by'].value_counts().values
                 ,palette=color,)

ax[0].tick_params(axis='x',rotation=90)
ax[0].set_xlabel('Directors',weight='semibold')
plt.title('Directors Distripution',weight='bold',fontsize=20)
sns.despine()
 
#Which title of the episode has more views?#

fig = plt.figure(figsize=(14,6))
sns.barplot(x=data.groupby(['title'])['us_viewers'].sum().index,
            y=data.groupby(['title'])['us_viewers'].sum().values,palette=color)
plt.tick_params(axis='x',rotation=90,labelsize=7)
sns.despine()
plt.xlabel('Tittle',weight='semibold')
plt.title('Tittle by Viewers',weight='bold',fontsize=20) 

#Compare between episode views and monthly views?

title = data.groupby(['title'])['us_viewers'].sum().reset_index()
title=title['us_viewers']
title=title.astype(int)
fig = plt.figure(figsize=(14,5))
sns.lineplot(x=data.groupby(['episode_num_overall'])['us_viewers'].sum().index,
            y=data.groupby(['episode_num_overall'])['us_viewers'].sum().values,sizes=20,
             color='#C3073F',label='Episode Views')
sns.lineplot(x=data.groupby(['episode_num_overall'])['us_viewers'].sum().index,
            y=title,color='#4E4E50',label ='Title Views')
sns.despine()
plt.xlabel('Views',weight='bold')
plt.title('Episode Views Vs Title Views',weight='bold',fontsize='20')

#How much monthly and yearly views?#

fig,ax= plt.subplots(1,2,figsize=(14,6))
ax[0].pie(data.groupby(['year'])['us_viewers'].sum().values,labels=data.groupby(['year'])['us_viewers'].sum().index,
         colors=color,autopct='%1.1f%%')
ax[1].pie(data.groupby(['month'])['us_viewers'].sum().values,labels=data.groupby(['month'])['us_viewers'].sum().index,
         colors=color,autopct='%1.1f%%')
ax[0].set_xlabel('Yearly Views',weight='semibold',fontsize=15)
ax[1].set_xlabel('Yearly Views',weight='semibold',fontsize=15)
plt.suptitle('% of Yearly Views & Monthly Views',weight='bold',fontsize=20) 

#Compare with written and directed episodes?#

direct = data.groupby(['directed_by'])['us_viewers'].sum().reset_index()

written = data.groupby(['written_by'])['us_viewers'].sum().reset_index().sort_values('us_viewers',ascending=False)
written=written.drop(written.index[60:65])

number=np.arange(1,61)
number=pd.DataFrame(number)
number.columns=['num']

fig = plt.figure(figsize=(14,5))
sns.lineplot(x=number['num'],
            y=written['us_viewers'],sizes=20,
             color='#C3073F',label='Written Views')
sns.despine()
sns.lineplot(x=number['num'],
            y=direct['us_viewers'],sizes=20,
             color='#4E4E50',label='Directer Views')
plt.xlabel('Views',weight='bold')
plt.title('Written Views Vs Direction Views',weight='bold',fontsize='20')










# In[ ]:




