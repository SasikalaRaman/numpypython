#!/usr/bin/env python
# coding: utf-8

# In[229]:



import matplotlib.pyplot as plt
import numpy as np


# In[230]:


arr=np.loadtxt("gdp_growth.csv", delimiter=',',usecols=np.arange(0,66) ,unpack=True,dtype= str)


# In[231]:


display(arr)


# In[232]:


x=arr[:,0]


# In[233]:


print(x)


# In[234]:


y=arr[:,2]
z=arr[:,3]
a=arr[:,1]
b=arr[:,4]
c=arr[:,5]
d=arr[:,6]


# In[235]:



x=x[4:66]
#y=y[4:66]
#z=z[4:66]
#a=a[4:66]


# In[236]:



plt.plot(x,y[4:66], label = 'America', marker='o', linewidth=3)
plt.plot(x,z[4:66],label= 'India', marker='o', linewidth=3)
plt.plot(x,a[4:66], label = 'Africa', marker='o', linewidth=3)
plt.xlabel('year')
plt.ylabel('GDP growth')
plt.title('over all GDP')
#plt.xticks(np.arange(14), ['1960','1965','1970','1975','1980','1985','1990','1995','2000','2005','2010','2015','2020','2025'])
#plt.yticks([21290811194,31290811194, 41290811194,51290811194, 61290811194, 71290811194])


# In[152]:


plt.show()


# In[122]:


plt


# In[ ]:




