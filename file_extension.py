#!/usr/bin/env python
# coding: utf-8

# In[9]:


import math
r=float(input("enter the radius of circle:"))
area= math.pi * r**2
print("the area of circle with radius","%0.2f"%r, "is:","%f"%area)


# In[16]:


import os
file_name=input("enter the filename")
extension=file_name.split(".")
if extension[-1]=='py':
    print("python")
elif extension[-1]=='txt':
    print("text")
elif extension[-1]=='png':
    print("portable network graphics")
else:
    print("none")


# In[ ]:




