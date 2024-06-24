#!/usr/bin/env python
# coding: utf-8

# # Working with Python Lists: Medical Insurance Costs Project

# You are a doctor sorting through medical insurance cost data for some patients.
# 
# Using your knowledge of Python lists, you will store medical data and see what valuable insights you can gain from that data.
# 
# Let's get started!

# ## Exploring List Data

# 1. First, take a look at the two lists in the code block below.
# 
#    The list `names` stores the names of ten individuals, and `insurance_costs` stores their medical insurance costs.
#    
#    Let's add additional data to these lists:
#    - Append a new individual, `"Priscilla"`, to `names`.
#    - Append her insurance cost, `8320.0` to `insurance_costs`.

# In[2]:


names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]


# 2. Currently, the `names` and `insurance_costs` lists are separate, but we want each insurance cost to be paired with a name.
# 
#    Create a new variable called `medical_records` that combines `insurance_costs` and `names` into a list using the `zip()` function.
#    
#    The list should have the following structure:
#    
#    ```py
#    [(cost_0, name_0), (cost_1, name_1), (cost_2, name_2), ...]
#    ```

# In[3]:


medical_records = list(zip(insurance_costs, names))


# 3. Print out `medical_records` below, and make sure the output is what you expected.

# In[4]:


print(medical_records)


# 4. Let's explore our medical data.
# 
#    We want to see how many medical records we are dealing with. Create a variable called `num_medical_records` that stores the length of `medical_records`.

# In[5]:


num_medical_records = len(medical_records)


# 5. Print `num_medical_records` with the following message:
# 
#    ```
#    There are {number of medical records} medical records.
#    ```

# In[6]:


print("There are " + str(num_medical_records) + " medical records.")


# ## Selecting List Elements

# 6. Select the first medical record in `medical_records`, and save it to a variable called `first_medical_record`.

# In[7]:


first_medical_record = medical_records[0]


# 7. Print `first_medical_record` with the following message:
# 
#    ```
#    Here is the first medical record: {first medical record}
#    ```

# In[8]:


print("Here is the first medical record: " + str(first_medical_record))


# ## Sorting Lists

# 8. Sort `medical_records` so that the individuals with the lowest insurance costs appear at the start of the list.
# 
#    Print the sorted `medical_records` with the following message:
#    
#    ```
#    Here are the medical records sorted by insurance cost: {sorted list}
#    ```

# In[10]:


medical_records.sort()
print("Here are the medical records sorted by insurance cost: " + str(medical_records))


# ## Slicing Lists

# 9. Let's look at the three cheapest insurance costs in our medical records.
# 
#    Slice the `medical_records` list, and store the three cheapest insurance costs in a list called `cheapest_three`.

# In[11]:


cheapest_three = medical_records[:3]


# 10. Print `cheapest_three` with the following message:
# 
#     ```py
#     Here are the three cheapest insurance costs in our medical records: {cheapest three}
#     ```

# In[12]:


print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))


# 11. Let's look at the three most expensive insurance costs in our medical records.
# 
#     Slice the `medical_records` list, and store the three most expensive insurance costs in a list called `priciest_three`.

# In[13]:


priciest_three = medical_records[-3:]


# 12. Print `priciest_three` with the following message:
# 
#     ```
#     Here are the three most expensive insurance costs in our medical records: {priciest three}
#     ```

# In[14]:


print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))


# ## Counting Elements in a List

# 13. Some individuals in our medical records have the same name. For example, the name "Paul" shows up twice.
# 
#     Count the number of occurrences of "Paul" in the `names` list, and store the result in a variable called `occurrences_paul`.
#     
#     Print `occurrences_paul` with the following message:
#     
#     ```
#     There are {occurrences Paul} individuals with the name Paul in our medical records.
#     ```

# In[16]:


occurrences_paul = names.count("Paul")
print("There are " +  str(occurrences_paul) + " individuals with the name Paul in our medical records.")


# ## Extra

# 14. Great job! In this project, you worked with Python lists to store medical insurance cost data and then gained meaningful insight into that data.
# 
#     You now have a better understanding of how to interact with data in lists - an important skill for a data scientist to have.
#     
#     Our dataset in this project was pretty small - we only dealt with 11 medical records. However, as you progress in your data science journey, you will encounter larger and more complex datasets. You are now better prepared to work with data in lists moving forward.
#     
#     If you'd like additional practice on lists, here are some ways you might extend this project:
#     - Sort the medical records alphabetically by name. You'll have to create a new list using `zip()` to do this.
#     - Select the medical records starting at index `3` and ending at index `7` and save it to a variable called `middle_five_records`.
#     
#     Happy coding!

# In[ ]:





# In[ ]:




