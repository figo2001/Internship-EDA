import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_data():
    return pd.read_csv('brooklyn99_episodes.csv')

data = load_data()

# Page Title
st.title('Brooklyn Nine-Nine Episode Analysis 📊')
st.image('image.JPEG', caption='Brooklyn Nine-Nine', use_column_width=True)

st.write("After successfully completing my internship, this project showcases my analysis of a TV show dataset through exploratory data analysis.📈")

st.write(" ")
st.write(" ")

data[['year','month','day']]=data['original_air_date'].str.split('-',expand=True) 
color = ['#C3073F','#1A1A1D', '#4E4E50', '#C5C6C7', '#6F2232', '#950740'] 

# Show the first five rows of the dataset
st.write('**The first five rows of the dataset**')
st.write(data.head())

# Show the last five rows of the dataset
st.write('**The last five rows of the dataset**')
st.write(data.tail())

# Show shape of the dataset
st.write('**Dataset shape**')
st.write(data.shape)

# Show the dataset columns  
st.write('**Show all the columns**')
st.write(data.columns)

# Check for missing values
st.write('**Missing Values:**')
st.write(data.isnull().sum())

# Descriptive Statistics
st.write('**Extra Statistical Measures**')
st.write(data.describe())

# unique values in the dataset
st.write('**Unique Values:**')
st.write(data.nunique())

# Show categorical columns
st.write('**Categorical Columns:**')
st.write(data.select_dtypes(include=['object']).columns)

# Show numerical columns
st.write('**Numerical Columns:**')
st.write(data.select_dtypes(include=['int64', 'float64']).columns)


# Show the dataset datatypes
st.write('**Data Types:**')
st.write(data.dtypes)

# Show the dataset correlation
st.write('**Correlation Matrix:**')
st.write(data.corr(numeric_only=True))


st.write(" ")
st.write(" ")

st.header('Exploratiry Data Analysis 📉')

st.write(" ")

# How much episodes are released yearly?
st.subheader('A) Yearly Episodes Distribution')
yearly_counts = data['year'].value_counts()
fig_yearly = plt.figure(figsize=(12, 5))
sns.barplot(x=yearly_counts.index, y=yearly_counts.values, palette=color)
plt.title('Year of Episodes Distribution')
plt.xlabel('Year')
plt.ylabel('Number of Episodes')
st.pyplot(fig_yearly)

# How much monthly release episode and yearly?
st.subheader('B) Year & Month Episode Distribution')
fig_year_month, ax_year_month = plt.subplots(1, 2, figsize=(12, 5))
sns.barplot(x=data['year'].value_counts().index, y=data['year'].value_counts().values, ax=ax_year_month[0], palette=color)
sns.barplot(x=data['month'].value_counts().index, y=data['month'].value_counts().values, ax=ax_year_month[1], palette=color)
ax_year_month[0].set_title('Yearly Episode Distribution')
ax_year_month[0].set_xlabel('Year')
ax_year_month[0].set_ylabel('Number of Episodes')
ax_year_month[1].set_title('Monthly Episode Distribution')
ax_year_month[1].set_xlabel('Month')
ax_year_month[1].set_ylabel('Number of Episodes')
st.pyplot(fig_year_month)

# Which Director runs the most episodes?
st.subheader('C) Directors Distribution')
fig_director = plt.figure(figsize=(14, 5))
sns.lineplot(x=data['directed_by'].value_counts().index,y=data['directed_by'].value_counts().values,markers='markers')
sns.barplot(x=data['directed_by'].value_counts().index, y=data['directed_by'].value_counts().values, palette=color)
plt.xticks(rotation=90)
plt.title('Directors Distribution')
plt.xlabel('Directors')
plt.ylabel('Number of Episodes Directed')
st.pyplot(fig_director)

# Which title of the episode has more views?
st.subheader('D) Title by Viewers')
fig_title_views = plt.figure(figsize=(20, 8))
title_views = data.groupby(['title'])['us_viewers'].sum().sort_values(ascending=False)
sns.barplot(x=data.groupby(['title'])['us_viewers'].sum().index,
            y=data.groupby(['title'])['us_viewers'].sum().values,palette=color)
plt.tick_params(axis='x',rotation=90,labelsize=7)
plt.xlabel('Total Viewers')
plt.ylabel('Title')
plt.title('Title by Viewers')
st.pyplot(fig_title_views)

# Yearly and Monthly Views
st.subheader('E) % of Yearly Views & Monthly Views')
fig_year_month_pie, ax_year_month_pie = plt.subplots(1, 2, figsize=(18, 8))
ax_year_month_pie[0].pie(data.groupby(['year'])['us_viewers'].sum(), labels=data.groupby(['year'])['us_viewers'].sum().index, autopct='%1.1f%%', colors=sns.color_palette(color, len(data.groupby(['year'])['us_viewers'].sum())))
ax_year_month_pie[1].pie(data.groupby(['month'])['us_viewers'].sum(), labels=data.groupby(['month'])['us_viewers'].sum().index, autopct='%1.1f%%', colors=sns.color_palette(color, len(data.groupby(['month'])['us_viewers'].sum())))
ax_year_month_pie[0].set_xlabel('Yearly Views', weight='semibold', fontsize=15)
ax_year_month_pie[1].set_xlabel('Monthly Views', weight='semibold', fontsize=15)
plt.suptitle('% of Yearly Views & Monthly Views')
st.pyplot(fig_year_month_pie)

# Written Views Vs Directed Views
st.subheader('F) Written Views Vs Directed Views')
direct = data.groupby(['directed_by'])['us_viewers'].sum().reset_index()

written = data.groupby(['written_by'])['us_viewers'].sum().reset_index().sort_values('us_viewers',ascending=False)
written=written.drop(written.index[60:65])

number=np.arange(1,61)
number=pd.DataFrame(number)
number.columns=['num']

fig_views_comparison = plt.figure(figsize=(20, 8))
sns.lineplot(x=number['num'],
            y=written['us_viewers'],sizes=20,
             color='#C3073F',label='Written Views')
sns.despine()
sns.lineplot(x=number['num'],
            y=direct['us_viewers'],sizes=20,
             color='#4E4E50',label='Directer Views')
plt.xlabel('Views')
plt.ylabel('Episode Number')
plt.title('Written Views Vs Directed Views')
st.pyplot(fig_views_comparison)
