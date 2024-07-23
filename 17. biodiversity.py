#!/usr/bin/env python
# coding: utf-8

# In[350]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[351]:


species = pd.read_csv('species_info.csv')
observations = pd.read_csv('observations.csv')

species


# In[352]:


species['conservation_status'].unique()


# In[353]:


species.fillna('No Intervention', inplace=True)


# In[354]:


species['category'].unique()


# In[355]:


# The Vascular Plants category has the highest number of non-endangered species (4469), followed by Birds (517). 
# Amphibians, Birds, Fish, Mammals, and Vascular Plants have at least one endangered species, with Mammals having the highest number of endangered species (7).

species_status = species.groupby(['category', 'conservation_status'])['conservation_status'].count()
species_status


# In[356]:


# Data preparation
conservation_status = ['Endangered', 'In Recovery', 'No Intervention', 'Species of Concern', 'Threatened']
categories = ['Amphibian', 'Bird', 'Fish', 'Mammal', 'Nonvascular Plant', 'Reptile', 'Vascular Plant']

data = {
    'Endangered': [1, 4, 3, 7, 0, 0, 1],
    'In Recovery': [0, 3, 0, 1, 0, 0, 0],
    'No Intervention': [73, 442, 116, 176, 328, 74, 4424],
    'Species of Concern': [4, 72, 4, 28, 5, 5, 43],
    'Threatened': [2, 0, 4, 2, 0, 0, 2]
}

# Bar width
bar_width = 0.5

# Positions of the bars on the x-axis
r = np.arange(len(conservation_status))

# Create the bars for each category
bottom = np.zeros(len(conservation_status))
for category in categories:
    counts = [data[status][categories.index(category)] for status in conservation_status]
    plt.bar(r, counts, bottom=bottom, width=bar_width, label=category)
    bottom += counts

# Adding labels and title
plt.xlabel('Conservation Status', fontweight='bold')
plt.ylabel('Number of Species (log scale)', fontweight='bold')
plt.title('Number of Species by Conservation Status and Category')
plt.xticks(r, conservation_status, rotation=45, ha="right")
plt.yscale('log')  # Set y-axis to log scale

# Adding the legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()


# In[357]:


observations


# In[358]:


species['is_protected'] = species['conservation_status'] != 'No Intervention'
uni_species = species.drop_duplicates(subset=['scientific_name'])
uni_species


# In[359]:


merged_data = pd.merge(observations, uni_species, on='scientific_name', how='left')
protected_merged = merged_data[merged_data['is_protected'] == True]
protected_merged


# In[360]:


pivoted_data = protected_merged.pivot_table(index='park_name', columns='category', values='observations')
pivoted_data['Total'] = pivoted_data.sum(axis=1)
pivoted_data.loc['Total'] = pivoted_data.sum(numeric_only=True)
pivoted_data = pivoted_data.astype(int)
pivoted_data


# In[361]:


#Yellowstone National Park has the highest number of protected species including 'Species of Concern', 'Endangered', 'Threatened', and 'In Recovery' followed by Yosemite National Park
# Nonvascular Plant consistently has the highest observation scores for protected species in Bryce, Great Smoky Mountains, and Yellowstone parks.
# Reptile has the highest observation score in Yosemite.

# Create the DataFrame
data = {
    'park_name': [
        'Bryce National Park', 
        'Great Smoky Mountains National Park', 
        'Yellowstone National Park', 
        'Yosemite National Park'
    ],
    'Amphibian': [71, 47, 166, 107],
    'Bird': [87, 60, 212, 128],
    'Fish': [56, 44, 150, 87],
    'Mammal': [79, 51, 190, 111],
    'Nonvascular Plant': [97, 74, 233, 135],
    'Reptile': [77, 73, 220, 136],
    'Vascular Plant': [91, 64, 211, 130]
}
df = pd.DataFrame(data).set_index('park_name')

# Plot the stacked bar chart
df.plot(kind='bar', stacked=True, figsize=(12, 8))

# Customize the plot
plt.title('Average Scores by Category and Park')
plt.xlabel('Park Name')
plt.ylabel('Observations')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Category')
plt.tight_layout()

# Show the plot
plt.show()


# In[ ]:




