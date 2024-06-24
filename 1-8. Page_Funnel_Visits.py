#!/usr/bin/env python
# coding: utf-8

# In[80]:


import pandas as pd


# Import all the files

# In[81]:


visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
                   
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])


# Step 1: Inspect the DataFrames using `print` and `head`

# In[82]:


print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())


# Step 2: Left merging visits and cart

# In[84]:


visits_cart = pd.merge(visits, cart, how='left')
print(visits_cart)


# Step 3: How long is `visits_cart`?

# In[86]:


total_visits = len(visits_cart)
print(total_visits)


# Step 4: How many timestamps are null for `cart_time`?

# In[88]:


null_cart_times = len(visits_cart[visits_cart.cart_time.isnull()])
print(null_cart_times)


# Step 5: What percentage only visited?

# In[90]:


visited_not_cart = float(null_cart_times) / float(total_visits)
print(visited_not_cart)


# Step 6: What percentage placed a t-shirt in their cart but did not checkout?

# In[95]:


cart_checkout = pd.merge(cart, checkout, how='left')
print(cart_checkout)

null_checkout_times = len(cart_checkout[cart_checkout.checkout_time.isnull()])
cart_not_checkout = float(null_checkout_times) / float(len(cart_checkout))

print("Cart but not checkout:", cart_not_checkout)


# Step 7: Merge it all together

# In[97]:


all_data = visits_cart.merge(cart_checkout, how='left').merge(purchase, how='left')
print(all_data)


# Step 8: % of users who got to checkout but did not purchase

# In[103]:


reached_checkout = pd.merge(checkout, purchase, how='left')
checkout_not_purchase = reached_checkout[reached_checkout.purchase_time.isnull()]
checkout_not_purchase_percent = float(len(checkout_not_purchase)) / float(len(reached_checkout))

print("Cart but not checkout:", checkout_not_purchase_percent)


# Step 9: check each part of the funnel, let's print all 3 of them again

# In[105]:


print("{} percent of users who visited the page did not add a t-shirt to their cart".format(round(visited_not_cart*100, 2)))
print("{} percent of users who added a t-shirt to their cart did not checkout".format(round(cart_not_checkout * 100, 2)))
print("{} percent of users who made it to checkout  did not purchase a shirt".format(round( checkout_not_purchase_percent*100, 2)))


# *The weakest part of the funnel is clearly getting a person who visited the site to add a tshirt to their cart. Once they've added a t-shirt to their cart it is fairly likely they end up purchasing it. A suggestion could be to make the add-to-cart button more prominent on the front page.*
# 
# 
# Step 10: adding new column

# In[107]:


all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data)


# Step 11: examine the results

# In[108]:


print(all_data.time_to_purchase)


# Step 12: average time to purchase

# In[109]:


print(all_data.time_to_purchase.mean())


# In[ ]:




