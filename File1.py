#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func(a, b):
    if a == 0:
        return b
    else:
        return func(b % a, a)
    print(func(30,75))


# In[2]:


print(func(30,75))


# In[3]:


numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))


# In[4]:


set1 = {14, 3, 55}
set2 = {82, 49, 62}
set3 = {99,22,17}
print(len(set1 + set2 + set3))


# In[5]:


print(4**3 + (7 + 5)**(1 + 1))


# In[6]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
}

for ship, captain in captains.items():
    print(ship, captain)


# In[7]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",
}
for ship in captains:
    print(ship, captains[ship])


# In[8]:


captains = {}


# In[9]:


captains = {
 "Enterprise": "Picard",
 "Voyager": "Janeway",
 "Defiant": "Sisko",}


# In[10]:


print(captains)


# In[12]:


captains = {"Enterprise": "Picard","Voyager": "Janeway","Defiant": "Sisko","Discovery": "unknown",}


# In[13]:


for captain, ship in captains.items():
    print(f"The {ship} is captained by {captain}.")


# In[14]:


del captains["Discovery"]


# In[15]:


print(captains)


# In[ ]:




