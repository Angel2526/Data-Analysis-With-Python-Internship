#!/usr/bin/env python
# coding: utf-8

# # Understanding Python Data Types 

# # Description:

# In[ ]:


This task involves understanding the basic datatypes in Python such as lists, dictionaries, and sets.


# # Write a Python program to create a list, a dictionary, and a set. Perform basic operations like adding, removing, and modifying elements.

# # LIST

# In[ ]:


# A list is an ordered collection of items which can be of any type.
# mutable
# Allow duplicates


# In[6]:


# Creating a List

my_list = ["apple", "banana", "cherry", "Grapes", "mango"]

# Adding an element to the list using append

my_list.append("blueberry") 

# Removing an element from the list using remove

my_list.remove("cherry")

#Modifying an element in the list 

my_list[2] = "kiwi"

print("Updated List : ", my_list)
    


# # DICTIONARY

# In[ ]:


# A dictionary is an unordered collection of items where each item is a key-value pair.
# Mutable


# In[10]:


# Creating a  Dictionary

my_dict = {"name": "Angel", "age": 22, "city": "Kochi"}

#Adding an item to the dictionary

my_dict["gender"] = "Female"

# Removing an item from dictionary using del

del my_dict["age"]

# modifying an element in dictionary

my_dict["city"] ="Ernakulam"

print("Updated Dictionary : " , my_dict)


# # SET

# In[ ]:


# A set is an unordered collection of unique items. 
# Mutable
# cannot contain duplicate elements


# In[16]:


# Creating a set

my_set = {'apple', 'banana', 'cherry' ,'Blueberry', 'orange' ,'stawberry'}

# Adding  an element to the set  using add

my_set.add('kiwi')

# Removing an element from the set using remove

my_set.remove('banana')

# Modifying an element in the set
 
my_set.add('watermelon')
my_set.discard('orange')
 
print("Updated Set : ", my_set)

