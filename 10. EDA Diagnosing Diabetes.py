#!/usr/bin/env python
# coding: utf-8

# # EDA: Diagnosing Diabetes

# In this project, you'll imagine you are a data scientist interested in exploring data that looks at how certain diagnostic factors affect the diabetes outcome of women patients.
# 
# You will use your EDA skills to help inspect, clean, and validate the data.
# 
# **Note**: This [dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database) is from the National Institute of Diabetes and Digestive and Kidney Diseases. It contains the following columns:
# 
# - `Pregnancies`: Number of times pregnant
# - `Glucose`: Plasma glucose concentration per 2 hours in an oral glucose tolerance test
# - `BloodPressure`: Diastolic blood pressure
# - `SkinThickness`: Triceps skinfold thickness
# - `Insulin`: 2-Hour serum insulin
# - `BMI`: Body mass index
# - `DiabetesPedigreeFunction`: Diabetes pedigree function
# - `Age`: Age (years)
# - `Outcome`: Class variable (0 or 1)
# 
# Let's get started!

# ## Initial Inspection

# 1. First, familiarize yourself with the dataset [here](https://www.kaggle.com/uciml/pima-indians-diabetes-database).
# 
#    Look at each of the nine columns in the documentation.
#    
#    What do you expect each data type to be?

# Expected data type for each column:
# 
# - `Pregnancies`: 
# - `Glucose`: 
# - `BloodPressure`: 
# - `SkinThickness`: 
# - `Insulin`: 
# - `BMI`: 
# - `DiabetesPedigreeFunction`: 
# - `Age`: 
# - `Outcome`: 

# 2. Next, let's load in the diabetes data to start exploring.
# 
#    Load the data in a variable called `diabetes_data` and print the first few rows.
#    
#    **Note**: The data is stored in a file called `diabetes.csv`.

# In[1]:


import pandas as pd
import numpy as np

# load in data
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())


# 3. How many columns (features) does the data contain?

# In[2]:


# print number of columns
print(len(diabetes_data.columns))


# 4. How many rows (observations) does the data contain?

# In[4]:


# print number of rows
print(len(diabetes_data))


# ## Further Inspection

# 5. Let's inspect `diabetes_data` further.
# 
#    Do any of the columns in the data contain null (missing) values?

# In[10]:


# find whether columns contain null values
print(diabetes_data.info())


# 6. If you answered no to the question above, not so fast!
# 
#    While it's technically true that none of the columns contain null values, that doesn't necessarily mean that the data isn't missing any values.
#    
#    When exploring data, you should always question your assumptions and try to dig deeper.
#    
#    To investigate further, calculate summary statistics on `diabetes_data` using the `.describe()` method.

# In[11]:


# perform summary statistics
print(diabetes_data.describe())


# 7. Looking at the summary statistics, do you notice anything odd about the following columns?
# 
#    - `Glucose`
#    - `BloodPressure`
#    - `SkinThickness`
#    - `Insulin`
#    - `BMI`

# **Your response to question 7**:

# 8. Do you spot any other outliers in the data?

# **Your response to question 8**:

# 9. Let's see if we can get a more accurate view of the missing values in the data.
# 
#    Use the following code to replace the instances of `0` with `NaN` in the five columns mentioned:
#    
#    ```py
#    diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)
#    ```

# In[12]:


# replace instances of 0 with NaN
diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)


# 10. Next, check for missing (null) values in all of the columns just like you did in Step 5.
# 
#     Now how many missing values are there?

# In[13]:


# find whether columns contain null values after replacements are made
print(diabetes_data.info())


# 11. Let's take a closer look at these rows to get a better idea of _why_ some data might be missing.
# 
#     Print out all the rows that contain missing (null) values.

# In[17]:


# print rows with missing values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])


# 12. Go through the rows with missing data. Do you notice any patterns or overlaps between the missing data?

# **Your response to question 12**:

# 13. Next, take a closer look at the data types of each column in `diabetes_data`.
# 
#     Does the result match what you would expect?

# In[18]:


# print data types using .info() method
print(diabetes_data.info())


# 14. To figure out why the `Outcome` column is of type `object` (string) instead of type `int64`, print out the unique values in the `Outcome` column.

# In[20]:


# print unique values of Outcome column
print(diabetes_data['Outcome'].unique())


# 15. How might you resolve this issue?

# **Your response to question 15**:

# ## Next Steps:

# 16. Congratulations! In this project, you saw how EDA can help with the initial data inspection and cleaning process. This is an important step as it helps to keep your datasets clean and reliable.
# 
#     Here are some ways you might extend this project if you'd like:
#     - Use `.value_counts()` to more fully explore the values in each column.
#     - Investigate other outliers in the data that may be easily overlooked.
#     - Instead of changing the `0` values in the five columns to `NaN`, try replacing the values with the median or mean of each column.

# In[ ]:




