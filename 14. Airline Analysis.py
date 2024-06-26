#!/usr/bin/env python
# coding: utf-8

# # Airline Analysis

# In this project, you'll imagine that you work for a travel agency and need to know the ins and outs of airline prices for your clients. You want to make sure that you can find the best deal for your client and help them to understand how airline prices change based on different factors.
# 
# You decide to look into your favorite airline. The data include:
# - `miles`: miles traveled through the flight
# - `passengers`: number of passengers on the flight
# - `delay`: take-off delay in minutes
# - `inflight_meal`: is there a meal included in the flight?
# - `inflight_entertainment`: are there free entertainment systems for each seat?
# - `inflight_wifi`: is there complimentary wifi on the flight?
# - `day_of_week`: day of the week of the flight
# - `weekend`: did this flight take place on a weekend?
# - `coach_price`: the average price paid for a coach ticket
# - `firstclass_price`: the average price paid for first-class seats
# - `hours`: how many hours the flight took
# - `redeye`: was this flight a redeye (overnight)?
# 
# In this project, you'll explore a dataset for the first time and get to know each of these features. Keep in mind that there's no one right way to address each of these questions. The goal is simply to explore and get to know the data using whatever methods come to mind.
# 
# You will be working in this file. Note that there is the file **Airline Analysis_Solution.ipynb** that contains the solution code for this project. We highly recommend that you complete the project on your own without checking the solution, but feel free to take a look if you get stuck or if you want to compare answers when you're done.
# 
# In order to get the plots to appear correctly in the notebook, you'll need to show and then clear each plot before creating the next one using the following code:
# 
# ```py
# plt.show() # Show the plot
# plt.clf() # Clear the plot
# ```
# 
# Clearing the plot will not erase the plot from view, it will just create a new space for the following graphic.

# ## Univariate Analysis

# 1. What do coach ticket prices look like? What are the high and low values? What would be considered the average? Does $500 seem like a good price for a coach ticket?

# In[21]:


import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math

## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())

## Task 1
sns.histplot(x='coach_price', data=flight)
plt.show()
plt.clf()

print(np.min(flight.coach_price))
print(np.max(flight.coach_price))
print(np.mean(flight.coach_price))
print(np.median(flight.coach_price))


# 2. Now visualize the coach ticket prices for flights that are 8 hours long. What are the high, low, and average prices for 8-hour-long flights? Does a $500 dollar ticket seem more reasonable than before?

# In[22]:


## Task 2
print(np.min(flight.coach_price[flight.hours == 8]))
print(np.max(flight.coach_price[flight.hours == 8]))
print(np.mean(flight.coach_price[flight.hours == 8]))
print(np.median(flight.coach_price[flight.hours == 8]))

sns.histplot(flight.coach_price[flight.hours == 8])
plt.show()
plt.clf()


# 3. How are flight delay times distributed? Let's say there is a short amount of time between two connecting flights, and a flight delay would put the client at risk of missing their connecting flight. You want to better understand how often there are large delays so you can correctly set up connecting flights. What kinds of delays are typical?

# In[23]:


## Task 3
sns.histplot(flight.delay[flight.delay < 200])
plt.show()
plt.clf()


# ## Bivariate Analysis

# 4. Create a visualization that shows the relationship between coach and first-class prices. What is the relationship between these two prices? Do flights with higher coach prices always have higher first-class prices as well?

# In[24]:


## Task 4
perc=0.05
flight_sub = flight.sample(n=int(flight.shape[0]*perc))

sns.lmplot(x = 'coach_price', y = 'firstclass_price', data = flight_sub, line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()


# 5. What is the relationship between coach prices and inflight features &mdash; inflight meal, inflight entertainment, and inflight WiFi? Which features are associated with the highest increase in price?

# In[34]:


## Task 5
sns.histplot(flight, x=flight.coach_price, hue=flight.inflight_meal)
plt.show()
plt.clf()

sns.histplot(flight, x=flight.coach_price, hue=flight.inflight_entertainment)
plt.show()
plt.clf()

sns.histplot(flight, x=flight.coach_price, hue=flight.inflight_wifi)
plt.show()
plt.clf()


# 6. How does the number of passengers change in relation to the length of flights?

# In[40]:


## Task 6
sns.lmplot(x='hours', y='passengers', data = flight_sub, x_jitter=0.25, scatter_kws={"s": 5, "alpha":0.2}, fit_reg = False)
plt.show()
plt.clf()


# ## Multivariate Analysis

# 7. Visualize the relationship between coach and first-class prices on weekends compared to weekdays.

# In[43]:


## Task 7
sns.scatterplot(x='coach_price', y='firstclass_price', data=flight_sub, hue='weekend')
plt.show()
plt.clf()


# 8. How do coach prices differ for redeyes and non-redeyes on each day of the week?

# In[50]:


## Task 8

sns.boxplot(x='day_of_week', y='coach_price', data=flight, hue='redeye')
plt.show()
plt.clf()


# In[ ]:




