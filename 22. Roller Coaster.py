#!/usr/bin/env python
# coding: utf-8

# # Roller Coaster

# #### Overview

# This project is slightly different than others you have encountered thus far. Instead of a step-by-step tutorial, this project contains a series of open-ended requirements which describe the project you'll be building. There are many possible ways to correctly fulfill these requirements, and you should expect to use the internet, Codecademy, and other resources when you encounter a problem that you cannot easily solve.

# #### Project Goals

# You will work to create several data visualizations that will give you insight into the world of roller coasters.

# ## Prerequisites

# In order to complete this project, you should have completed the first two lessons in the [Data Analysis with Pandas Course](https://www.codecademy.com/learn/data-processing-pandas) and the first two lessons in the [Data Visualization in Python course](https://www.codecademy.com/learn/data-visualization-python). This content is also covered in the [Data Scientist Career Path](https://www.codecademy.com/learn/paths/data-science/).

# ## Project Requirements

# 1. Roller coasters are thrilling amusement park rides designed to make you squeal and scream! They take you up high, drop you to the ground quickly, and sometimes even spin you upside down before returning to a stop. Today you will be taking control back from the roller coasters and visualizing data covering international roller coaster rankings and roller coaster statistics.
# 
#    Roller coasters are often split into two main categories based on their construction material: **wood** or **steel**. Rankings for the best wood and steel roller coasters from the 2013 to 2018 [Golden Ticket Awards](http://goldenticketawards.com) are provded in `'Golden_Ticket_Award_Winners_Wood.csv'` and `'Golden_Ticket_Award_Winners_Steel.csv'`, respectively. Load each csv into a DataFrame and inspect it to gain familiarity with the data.

# In[63]:


# 1 
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# load rankings data
wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
print(wood)

# load rankings data
steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
print(steel)


# 2. Write a function that will plot the ranking of a given roller coaster over time as a line. Your function should take a roller coaster's name and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with `"El Toro"` as the roller coaster name and the wood ranking DataFrame. What issue do you notice? Update your function with an additional argument to alleviate the problem, and retest your function.

# In[64]:


# 2
# Create a function to plot rankings over time for 1 roller coaster
def plot_coaster_ranking(coaster_name, park_name, ranking_data): 
    coaster_ranking = ranking_data[(ranking_data['Name'] == coaster_name) & (ranking_data['Park'] == park_name)]  
    
    ax = plt.subplot()
    ax.plot(coaster_ranking['Year of Rank'], coaster_ranking['Rank'])
    ax.set_xticks(coaster_ranking['Year of Rank'].values)
    ax.set_yticks(coaster_ranking['Rank'].values)
    ax.invert_yaxis()
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title("{} Rankings".format(coaster_name))
    plt.show()
    plt.close()

# Create a plot of El Toro ranking over time
plot_coaster_ranking('El Toro', 'Six Flags Great Adventure', wood)


# 3. Write a function that will plot the ranking of two given roller coasters over time as lines. Your function should take both roller coasters' names and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with `"El Toro"` as one roller coaster name, `"Boulder Dash"` as the other roller coaster name, and the wood ranking DataFrame. What issue do you notice? Update your function with two additional arguments to alleviate the problem, and retest your function.

# In[65]:


# 3
# Create a function to plot rankings over time for 2 roller coasters
def plot_coaster_ranking(coaster_name1, park_name1, coaster_name2, park_name2, ranking_data): 
    coaster_ranking1 = ranking_data[(ranking_data['Name'] == coaster_name1) & (ranking_data['Park'] == park_name1)]  
    coaster_ranking2 = ranking_data[(ranking_data['Name'] == coaster_name2) & (ranking_data['Park'] == park_name2)]
    
    ax = plt.subplot()
    ax.plot(coaster_ranking1['Year of Rank'], coaster_ranking1['Rank'])
    ax.plot(coaster_ranking2['Year of Rank'], coaster_ranking2['Rank'])
    ax.invert_yaxis()
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.title("{} vs {} Rankings".format(coaster_name1, coaster_name2))
    plt.legend([coaster_name1, coaster_name2])
    plt.show()
    plt.close()
    
# Create a plot of El Toro and Boulder Dash roller coasters
plot_coaster_ranking('El Toro', 'Six Flags Great Adventure', 'Boulder Dash', 'Lake Compounce', wood)


# 4. Write a function that will plot the ranking of the top `n` ranked roller coasters over time as lines. Your function should take a number `n` and a ranking DataFrame as arguments. Make sure to include informative labels that describe your visualization.
# 
#    For example, if `n == 5`, your function should plot a line for each roller coaster that has a rank of `5` or lower.
#    
#    Call your function with a value of `n` and either the wood ranking or steel ranking DataFrame.

# In[66]:


# 4
# Create a function to plot top n rankings over time
def plot_top_n(n, ranking_data):
    top_n_rankings = ranking_data[ranking_data['Rank'] <= n]
    fig, ax = plt.subplots(figsize=(7, 7))
    
    for name in set(top_n_rankings['Name']):
        coaster_ranking = top_n_rankings[top_n_rankings['Name'] == name]
        ax.plot(coaster_ranking['Year of Rank'], coaster_ranking['Rank'], label=name)
    
    ax.invert_yaxis()
    plt.xlabel('Year')
    plt.ylabel('Rank')
    ax.set_yticks([i for i in range(1,6)])
    plt.title("Top {} Rankings".format(n))
    plt.legend(fontsize='xx-small', loc=0)
    plt.show()
    plt.close()

# Create a plot of top n rankings over time
plot_top_n(5, wood)


# 5. Now that you've visualized rankings over time, let's dive into the actual statistics of roller coasters themselves. [Captain Coaster](https://captaincoaster.com/en/) is a popular site for recording roller coaster information. Data on all roller coasters documented on Captain Coaster has been accessed through its API and stored in `roller_coasters.csv`. Load the data from the csv into a DataFrame and inspect it to gain familiarity with the data.

# In[67]:


# 5
# load roller coaster data
roller_coasters = pd.read_csv('roller_coasters.csv')
roller_coasters.head()


# 6. Write a function that plots a histogram of any numeric column of the roller coaster DataFrame. Your function should take a DataFrame and a column name for which a histogram should be constructed as arguments. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with the roller coaster DataFrame and one of the column names.

# In[68]:


# 6
# Create a function to plot histogram of column values
def plot_histogram(coaster_data, column_name):
    plt.hist(coaster_data[column_name].dropna())
    plt.title('Histogram of Roller Coaster {}'.format(column_name))
    plt.xlabel(column_name)
    plt.ylabel('Count')
    plt.show()
    plt.close()
    
# Create histogram of roller coaster speed
plot_histogram(roller_coasters, 'speed')
plt.clf()
plt.close()

# Create histogram of roller coaster length
plot_histogram(roller_coasters, 'length')
plt.clf()
plt.close()

# Create histogram of roller coaster number of inversions
plot_histogram(roller_coasters, 'num_inversions')
plt.clf()
plt.close()

# Create a function to plot histogram of height values
def plot_histogram(coaster_data):
    plt.hist(coaster_data['height'][coaster_data['height'] < 200])
    plt.title('Histogram of Roller Coaster Height')
    plt.xlabel('Height')
    plt.ylabel('Count')
    plt.show()
    plt.close()

# Create a histogram of roller coaster height
plot_histogram(roller_coasters)


# 7. Write a function that creates a bar chart showing the number of inversions for each roller coaster at an amusement park. Your function should take the roller coaster DataFrame and an amusement park name as arguments. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with the roller coaster DataFrame and amusement park name.

# In[72]:


# 7
# Create a function to plot inversions by coaster at park
def plot_inversions_by_coaster(coaster_data, park_name):
    park_coasters = coaster_data[coaster_data['park'] == park_name]
    plt.bar(range(len(park_coasters['num_inversions'])), park_coasters['num_inversions'])
    
    ax = plt.subplot()
    ax.set_xticks(range(len(park_coasters['name'])))
    ax.set_xticklabels(park_coasters['name'], rotation=60)
    plt.xlabel('Park Name')
    plt.ylabel('Number of Inversions')
    plt.title("Number of Inversions Per Coaster at {}".format(park_name))    
    plt.show()
    plt.close()
    
# Create barplot of inversions by roller coasters
plot_inversions_by_coaster(roller_coasters, 'Parc Asterix')


# 8. Write a function that creates a pie chart that compares the number of operating roller coasters (`'status.operating'`) to the number of closed roller coasters (`'status.closed.definitely'`). Your function should take the roller coaster DataFrame as an argument. Make sure to include informative labels that describe your visualization.
# 
#    Call your function with the roller coaster DataFrame.

# In[80]:


# 8
# Create a function to plot a pie chart of status.operating
def pie_chart_status(coaster_data):
    operating_coasters = coaster_data[coaster_data['status'] == 'status.operating']
    closed_coasters = coaster_data[coaster_data['status'] == 'status.closed.definitely']
    num_operating_coasters = len(operating_coasters)
    num_closed_coasters = len(closed_coasters)    
    status_counts = [num_operating_coasters, num_closed_coasters]
    plt.pie(status_counts, autopct='%0.1f%%', labels=['Operating','Closed'])
    plt.axis('equal')
    plt.show()
    plt.close()
    
# Create pie chart of roller coasters
pie_chart_status(roller_coasters)


# 9. `.scatter()` is another useful function in matplotlib that you might not have seen before. `.scatter()` produces a scatter plot, which is similar to `.plot()` in that it plots points on a figure. `.scatter()`, however, does not connect the points with a line. This allows you to analyze the relationship between two variables. Find [`.scatter()`'s documentation here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html).
# 
#    Write a function that creates a scatter plot of two numeric columns of the roller coaster DataFrame. Your function should take the roller coaster DataFrame and two-column names as arguments. Make sure to include informative labels that describe your visualization.
#    
#    Call your function with the roller coaster DataFrame and two-column names.

# In[87]:


# 9
roller_coasters.head()
# Create a function to plot scatter of any two columns
def plot_scatter(coaster_df, column_x, column_y):
    plt.scatter(coaster_df[column_x], coaster_df[column_y])
    plt.title('Scatter Plot of {} vs. {}'.format(column_y,column_x))
    plt.xlabel(column_x)
    plt.ylabel(column_y)    
    plt.show()
    plt.close()
    
# Create a function to plot scatter of speed vs height
def plot_scatter_height_speed(coaster_df):
    coaster_df = coaster_df[coaster_df['height'] < 200]
    plt.scatter(coaster_df['speed'], coaster_df['height'])
    plt.title('Scatter Plot of Speed vs. Height')
    plt.xlabel('Speed')
    plt.ylabel('Height')    
    plt.show()
    plt.close()    
    
# Create a scatter plot of roller coaster height by speed
plot_scatter_height_speed(roller_coasters)


# 10. Part of the fun of data analysis and visualization is digging into the data you have and answering questions that come to your mind.
# 
#     Some questions you might want to answer with the datasets provided include:
#     - What roller coaster seating type is most popular? And do different seating types result in higher/faster/longer roller coasters?
#     - Do roller coaster manufactures have any specialties (do they focus on speed, height, seating type, or inversions)?
#     - Do amusement parks have any specialties?
#     
#     What visualizations can you create that answer these questions, and any others that come to you? Share the questions you ask and the accompanying visualizations you create on the Codecademy forums.

# In[ ]:





# ## Solution

# Great work! Visit [our forums](https://discuss.codecademy.com/t/roller-coaster-challenge-project-python-pandas/462378) or the file **Roller Coaster_Solution.ipynb** to compare your project to our sample solution code. You can also learn how to host your own solution on GitHub so you can share it with other learners! Your solution might look different from ours, and that's okay! There are multiple ways to solve these projects, and you'll learn more by seeing others' code.

# In[ ]:




