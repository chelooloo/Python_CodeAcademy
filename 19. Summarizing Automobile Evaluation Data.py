#!/usr/bin/env python
# coding: utf-8

# # Summarizing Automobile Evaluation Data

# In the following project you'll use what you've learned about summarizing categorical data to analyze a sample from a popular open source dataset. This dataset contains information on the cost and physical attributes of several thousand cars. Originally, this dataset was used to train a classification model that assigned an acceptability score/category to cars based on these attributes.
# 
# The car evaluation dataset has been sourced from the UCI Machine Learning Repository and has been slightly modified for this project. Specifically, one additional field `manufacturer_country` has been simulated for illustrative purposes. You can read more about the details, features, and original uses of this dataset in research on the [UCI data description page](https://archive.ics.uci.edu/ml/datasets/car+evaluation).

# ## Summarizing Manufacturing Country

# 1. `manufacturer_country` is a _nominal categorical variable_ that indicates the country of the manufacturer of each car reviewed. Create a table of frequencies of all the cars reviewed by `manufacturer_country`. What is the modal category? Which country appears 4th most frequently? Print out your results.

# In[11]:


import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

#United States appears 4th most frequency.
car_eval['manufacturer_country'].value_counts()


# 2. Calculate a table of proportions for countries that appear in `manufacturer_country` in the dataset. What percentage of cars were manufactured in Japan?

# In[12]:


# 22.8% of cars were manufactured in Japan.
car_eval['manufacturer_country'].value_counts() / len(car_eval['manufacturer_country'])


# ## Summarizing Buying Costs

# 3. `buying_cost` is a categorical variable which describes the cost of buying any car in the dataset. Print out a list of the possible values for this variable.

# In[13]:


car_eval['buying_cost'].unique()


# 4. `buying_cost` is an _ordinal categorical variable_, which means we can create an order associated with the values in the data and perform numeric operations on the variable. Create a new list, `buying_cost_categories`, that contains the unique values in `buying_cost`, ordered from lowest to highest.

# In[14]:


buying_cost_categories = ['low', 'med', 'high', 'vhigh']


# 5. Convert `buying_cost` to type `'category'` using the list you created in the previous exercise.

# In[15]:


car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered=True)


# 6. Calculate the median category of the `buying_cost` variable and print the result.

# In[17]:


median_index = np.median(car_eval['buying_cost'].cat.codes)
print(median_index)

median_category = buying_cost_categories[int(median_index)]
print(median_category)


# ## Summarizing Luggage Capacity

# 7. `luggage` is a categorical variable in the car evaluations dataset that records the luggage capacity for each reviewed car. Calculate a table of proportions for this variable and print the result.

# In[21]:


car_eval['luggage'].value_counts(normalize=True)


# 8. Are there any missing values in this column? Replicate the table of proportions from the previous exercise, but do not drop any missing values from the count. Print the result.

# In[22]:


car_eval['luggage'].value_counts(dropna=False, normalize=True)


# 9. Without passing `normalize = True` to `.value_counts()`, can you replicate the result you got in the previous exercises?

# In[24]:


car_eval['luggage'].value_counts() / len(car_eval['luggage'])


# ## Summarizing Passenger Capacity

# 10. `doors` is a categorical variable in the car evaluations dataset that records the count of doors for each reviewed car. Find the count of cars that have 5 or more doors. You can identify cars with 5+ doors by looking for cars that have a value of `'5more'` in the `doors` column. Print your result.

# In[29]:


(car_eval['doors'] == '5more').sum()


# 11. Find the proportion of cars that have 5+ doors and print the result.

# In[30]:


(car_eval['doors'] == '5more').mean()


# In[ ]:




