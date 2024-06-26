#!/usr/bin/env python
# coding: utf-8

# In[152]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[153]:


all_data = pd.read_csv("C:/Users/img30/Downloads/all_data.csv")
print(data.head())


# In[154]:


#life expectancy and GDP increase over time per country
## As GDP has increased over time, life expectancy has also increased across all six countries. 

six_nations = all_data['Country'].unique()
print(six_nations)

plt.subplots(figsize=(15, 5))

plt.subplot(1, 2, 1)
sns.lineplot(data=all_data, x='Year', y='Life expectancy at birth (years)', hue='Country', sizes=(.5, .5))
plt.legend(loc=0)
plt.title('Life expectancy over time per country')

plt.subplot(1, 2, 2)
sns.lineplot(data=all_data, x='Year', y='GDP', hue='Country', sizes=(.5, .5))
plt.legend(loc=2)
plt.title('GDP over time per country')

plt.show()
plt.clf()


# In[155]:


# life expantancy increase breakdown per country
## life expactancy increased has increased over time in all six countries.

chile_data = all_data[all_data['Country']=='Chile']
plt.subplot(2, 3, 1)
plt.plot(chile_data['Year'], chile_data['Life expectancy at birth (years)'], color='b')
plt.title('Chile')
plt.ylabel('Life expectancy')

chile_data = all_data[all_data['Country']=='China']
plt.subplot(2, 3, 2)
plt.plot(chile_data['Year'], chile_data['Life expectancy at birth (years)'], color='g')
plt.title('China')

chile_data = all_data[all_data['Country']=='Germany']
plt.subplot(2, 3, 3)
plt.plot(chile_data['Year'], chile_data['Life expectancy at birth (years)'], color='r')
plt.title('Germany')

chile_data = all_data[all_data['Country']=='Mexico']
plt.subplot(2, 3, 4)
plt.plot(chile_data['Year'], chile_data['Life expectancy at birth (years)'], color='c')
plt.title('Mexico')
plt.xlabel('Year')
plt.ylabel('Life expectancy')

chile_data = all_data[all_data['Country']=='United States of America']
plt.subplot(2, 3, 5)
plt.plot(chile_data['Year'], chile_data['Life expectancy at birth (years)'], color='m')
plt.title('US')
plt.xlabel('Year')

chile_data = all_data[all_data['Country']=='Zimbabwe']
plt.subplot(2, 3, 6)
plt.plot(chile_data['Year'], chile_data['Life expectancy at birth (years)'], color='y')
plt.title('Zimbabwe')
plt.xlabel('Year')

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.rcParams.update({'font.size': 8})
plt.show()
plt.clf()


# In[156]:


# GDP increase breakdown per country
## GDP has increased over time in six countries; however, GDP peaked in Chile, Germany, and Mexico in 2013, 2014, and 2014 respectively, before decreasing.

chile_data = all_data[all_data['Country']=='Chile']
plt.subplot(2, 3, 1)
plt.plot(chile_data['Year'], chile_data['GDP'], color='b')
plt.title('Chile')
plt.ylabel('GDP')

chile_data = all_data[all_data['Country']=='China']
plt.subplot(2, 3, 2)
plt.plot(chile_data['Year'], chile_data['GDP'], color='g')
plt.title('China')

chile_data = all_data[all_data['Country']=='Germany']
plt.subplot(2, 3, 3)
plt.plot(chile_data['Year'], chile_data['GDP'], color='r')
plt.title('Germany')

chile_data = all_data[all_data['Country']=='Mexico']
plt.subplot(2, 3, 4)
plt.plot(chile_data['Year'], chile_data['GDP'], color='c')
plt.title('Mexico')
plt.xlabel('Year')
plt.ylabel('GDP')

chile_data = all_data[all_data['Country']=='United States of America']
plt.subplot(2, 3, 5)
plt.plot(chile_data['Year'], chile_data['GDP'], color='m')
plt.title('US')
plt.xlabel('Year')

chile_data = all_data[all_data['Country']=='Zimbabwe']
plt.subplot(2, 3, 6)
plt.plot(chile_data['Year'], chile_data['GDP'], color='y')
plt.title('Zimbabwe')
plt.xlabel('Year')

plt.subplots_adjust(wspace=0.5, hspace=0.5)
plt.rcParams.update({'font.size': 8})
plt.show()
plt.clf()


# In[157]:


# average life expectancy by nation
## The average life expectancy in Chile, China, Germany, Mexico, and the United States is above 74, while Zimbabwe has the lowest average life expectancy at 50.

avg_life_expectancy = all_data.groupby('Country')['Life expectancy at birth (years)'].mean()
print(avg_life_expectancy)


# In[ ]:




