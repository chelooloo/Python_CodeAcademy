#!/usr/bin/env python
# coding: utf-8

# # Cleaning US Census Data

# You just got hired as a Data Analyst at the Census Bureau, which collects census data and creates interesting visualizations and insights from it.
# 
# The person who had your job before you left you all the data they had for the most recent census. It is in multiple `csv` files. They didn't use pandas, they would just look through these `csv` files manually whenever they wanted to find something. Sometimes they would copy and paste certain numbers into Excel to make charts.
# 
# The thought of it makes you shiver. This is not scalable or repeatable.
# 
# Your boss wants you to make some scatterplots and histograms by the end of the day. Can you get this data into `pandas` and into reasonable shape so that you can make these histograms?

# ## Inspect the Data!

# 1. The first visualization your boss wants you to make is a scatterplot that shows average income in a state vs proportion of women in that state.
# 
#    Open some of the census `csv` files that came with the kit you downloaded. How are they named? What kind of information do they hold? Will they help us make this graph?

# In[ ]:





# 2. It will be easier to inspect this data once we have it in a DataFrame. You can't even call `.head()` on these `csv`s! How are you supposed to read them?
# 
#    Using `glob`, loop through the census files available and load them into DataFrames. Then, concatenate all of those DataFrames together into one DataFrame, called something like `us_census`.

# In[109]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

us_census = glob.glob('states*.csv')
us_census_list = []

for census in us_census:
    us_census_list.append(pd.read_csv(census))
    
data = pd.concat(us_census_list)    


# 3. Look at the `.columns` and the `.dtypes` of the `us_census` DataFrame. Are those datatypes going to hinder you as you try to make histograms?

# In[110]:


print(data.columns)
print(data.dtypes)


# 4. Look at the `head()` of the DataFrame so that you can understand why some of these `dtypes` are objects instead of integers or floats.
# 
#    Start to make a plan for how to convert these columns into the right types for manipulation.

# In[111]:


print(data.head())


# ## Regex to the Rescue

# 5. Use regex to turn the `Income` column into a format that is ready for conversion into a numerical type.

# In[112]:


data.Income = data['Income'].replace('[\$,]', '', regex=True)
data.Income = pd.to_numeric(data.Income)
print(data.head())


# 6. Look at the `GenderPop` column. We are going to want to separate this into two columns, the `Men` column, and the `Women` column.
# 
#    Split the column into those two new columns using `str.split` and separating out those results.

# In[113]:


GenderPop_split = data.GenderPop.str.split('_')
data['Men'] = GenderPop_split.str.get(0)
data['Women'] = GenderPop_split.str.get(1)
print(data.head())


# 7. Convert both of the columns into numerical datatypes.
# 
#    There is still an `M` or an `F` character in each entry! We should remove those before we convert.

# In[114]:


data['Men'] = data['Men'].replace('[\D]', '', regex=True)
data['Women'] = data['Women'].replace('[\D]', '', regex=True)


data['Men'] = pd.to_numeric(data['Men'])
data['Women'] = pd.to_numeric(data['Women'])

print(data.head())


# 8. Now you should have the columns you need to make the graph and make sure your boss does not slam a ruler angrily on your desk because you've wasted your whole day cleaning your data with no results to show!
# 
#    Use matplotlib to make a scatterplot!
#    
#    ```py
#    plt.scatter(the_women_column, the_income_column)
#    ```
#    
#    Remember to call `plt.show()` to see the graph!

# In[115]:


plt.scatter(data.Women, data.Income)
plt.xlabel('Population of Women per State')
plt.ylabel('Income')
plt.title('Income vs Number of Women per State')
plt.show()
plt.clf()


# 9. You want to double check your work. You know from experience that these monstrous csv files probably have `nan` values in them! Print out your column with the number of women per state to see.
# 
#    We can fill in those `nan`s by using pandas' `.fillna()` function.
#    
#    You have the `TotalPop` per state, and you have the `Men` per state. As an estimate for the `nan` values in the `Women` column, you could use the `TotalPop` of that state minus the `Men` for that state.
#    
#    Print out the `Women` column after filling the `nan` values to see if it worked!

# In[116]:


print(data.isna().sum())

data['Women'] = data['Women'].fillna(data['TotalPop'] - data['Men'])
print(data['Women'])


# 10. We forgot to check for duplicates! Use `.duplicated()` on your `census` DataFrame to see if we have duplicate rows in there.

# In[117]:


print(data.duplicated(subset=data.columns[1:]))


# 11. Drop those duplicates using the `.drop_duplicates()` function.

# In[118]:


data.drop_duplicates(subset=data.columns[1:])


# 12. Make the scatterplot again. Now, it should be perfect! Your job is secure, for now.

# In[119]:


plt.scatter(data.Women, data.Income)
plt.xlabel('Population of Women per State')
plt.ylabel('Income')
plt.title('Income vs Number of Women per State')
plt.show()
plt.clf()


# ## Histogram of Races

# 13. Now your boss wants you to make a bunch of histograms out of the race data that you have. Look at the `.columns` again to see what the race categories are.

# In[120]:


data.columns
data.head()


# 14. Try to make a histogram for each one!
# 
#     You will have to get the columns into the numerical format, and those percentage signs will have to go.
#     
#     Don't forget to fill the `nan` values with something that makes sense! You probably dropped the duplicate rows when making your last graph, but it couldn't hurt to check for duplicates again.

# In[143]:


for race in ['Hispanic', 'White', 'Black','Native', 'Asian', 'Pacific']:
    data[race] = data[race].replace('%', '', regex=True)
    data[race] = pd.to_numeric(data[race])
    
data['Pacific'] = data['Pacific'].fillna(100 - data['Hispanic'] - data['White'] - data['Black'] - data['Native'] - data['Asian'])

for race in ['Hispanic', 'White', 'Black','Native', 'Asian', 'Pacific']:
    plt.figure(figsize=(4, 4))
    plt.hist(data[race]) 
    plt.xlabel('Percentage')
    plt.ylabel('Frequency')
    plt.title('Histogram of the Percentage of {} People per State'.format(race))
    plt.show()
    plt.clf()


# ## Get Creative

# 15. Phew. You've definitely impressed your boss on your first day of work.
# 
#     But is there a way you really convey the power of pandas and Python over the drudgery of `csv` and Excel?
#     
#     Try to make some more interesting graphs to show your boss, and the world! You may need to clean the data even more to do it, or the cleaning you have already done may give you the ease of manipulation you've been searching for.

# In[ ]:




