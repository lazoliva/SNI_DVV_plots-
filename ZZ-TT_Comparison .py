#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[178]:


ZZ = pd.read_csv (r'/Users/seismo_reynier/Documents/All_dvvZZ.csv', index_col=0, parse_dates=True)
TT = pd.read_csv (r'/Users/seismo_reynier/Documents/All_dvvTT.csv', index_col=0, parse_dates=True)
M = pd.read_csv (r'/Users/seismo_reynier/Documents/All_M.csv', index_col=0, parse_dates=True)
M0 = pd.read_csv (r'/Users/seismo_reynier/Documents/ALL-TT-ZZ-M0.csv', index_col=0, parse_dates=True)
Sept29_16 = pd.read_csv (r'/Users/seismo_reynier/Documents/20160929.csv', index_col=0) 


# In[49]:


M0.head()


# In[109]:


#M0.plot(figsize=(14, 4), ylabel='dv/v(%)')   


# In[42]:


#M.head()


# In[75]:



#plt.figure(1)
#axs = M.plot(figsize=(14, 4), ylabel='dv/v(%)') 
       


# In[2]:


#axs = M.plot(figsize=(14, 4), ylabel='dv/v(%)', subplots=True)  


# In[110]:


plt.figure(2)
axs = M0["TT_M0"].plot(figsize=(14, 4), ylabel='dv/v(%)', legend=True)    #dvv values for TT/ZZ forcing it through 0
axs = M0["ZZ_M0"].plot(figsize=(14, 4), ylabel='dv/v(%)', legend=True, color='Red')  


# In[193]:


#plt.figure(3)
axs = M0["TT_EM0"].plot(figsize=(14, 4), ylabel='dv/v(Errors)', legend=True) #dvv error pattem during the two years data 
axs = M0["ZZ_EM0"].plot(figsize=(14, 4), ylabel='dv/v(Errors)', legend=True) 


# In[113]:


#All dv/v for the two years database in the TT component forcing through the origin with their errobars.  
axs = M0["TT_M0"].plot(figsize=(20, 6), ylabel='dv/v(%)', legend=True, yticks=(0.05,0.00,-0.05,-0.10,-0.15)) 
axs.errorbar(M0.index, M0["TT_M0"], yerr = M0["TT_EM0"], linewidth = 1.5, color = "black", alpha = 0.4, capsize = 4)  
plt.tight_layout(h_pad=5, w_pad=0.5) 
  


# In[114]:


#All dv/v for the two years database in the ZZ component forcing through the origin with their errobars.
axs = M0["ZZ_M0"].plot(figsize=(20, 6), ylabel='dv/v(%)', legend=True, color='Red', yticks=(0.05,0.00,-0.05,-0.10,-0.15))  
axs.errorbar(M0.index, M0["ZZ_M0"], yerr = M0["ZZ_EM0"], linewidth = 1.5, color = "black", alpha = 0.4, capsize = 4)
plt.tight_layout(h_pad=5, w_pad=0.5) 


# In[99]:


#Visually comparing the errors computed for the two components. 
M0.plot.scatter(x="TT_EM0", y="ZZ_EM0", alpha=0.5, figsize=(12,4))


# In[180]:


#Station pair information for Sept 29, 2016 (During the last part of the REF)
Sept29_16.head()
Sept29_16.plot()
#print(Sept29_16) 
#axs=Sept29_16.plot(x="Pairs", y="TT_M0", figsize=(20,6)) 


# In[170]:


#x = np.arange(0,105,1)
#print(x) 
#values = Sept29_16[['Pairs']].to_numpy()
#print(values)

#plt.figure(1)
#plt.subplot(2,2,1)
#plt.figure(figsize=(10, 10))
#plt.plot(x,Sept29_16["TT_M0"],'--bd',linewidth=1) 
#plt.plot(Pairs,ZZ_M0,'--rs',linewidth=1) 
#plt.plot(Pairs,ALL,'-y',linewidth=1) 
#xticks=np.arange(0,105,5)
#plt.xticks(xticks)
#plt.xlabel('Pairs')
#plt.ylabel('M0') 
#plt.title('M0 of all station pairs for TT/ZZ in Sept 29, 2016') 


# In[195]:


plt.figure(1)
plt.figure(figsize=(20,6))
plt.plot(Sept29_16["TT_M0"],'--bd',linewidth=1) 
plt.plot(Sept29_16["ZZ_M0"],'--rs',linewidth=1)
plt.plot(Sept29_16["ALL"],'-k',linewidth=1) 
xticks=np.arange(0,105,5)
plt.xticks(xticks)
plt.xlabel('Pair number',fontsize=15, color='k')
plt.ylabel('Pair number M0',fontsize=15, color='k')
plt.legend(['TT','ZZ'],fontsize=15)  
plt.title('M0 for each station pair during Sept 29, 2016', fontsize=15, color='k')
plt.tight_layout(h_pad=5, w_pad=0.5)


# In[201]:


plt.figure(2)
plt.figure(figsize=(20,7))
plt.plot(Sept29_16["TT_M0"],'bd',linewidth=1) 
plt.plot(Sept29_16["ZZ_M0"],'rs',linewidth=1)
plt.plot(Sept29_16["ALL"],'-k',linewidth=1) 
xticks=np.arange(0,105,5)
plt.xticks(xticks)
plt.xlabel('Pair number',fontsize=15, color='k')
plt.ylabel('Pair number M0 and errors',fontsize=15, color='k')
plt.legend(['TT','ZZ'],fontsize=15)  
plt.title('M0 and error bars for each station pair during Sept 29, 2016', fontsize=15, color='k')
plt.errorbar(Sept29_16.index,Sept29_16['TT_M0'],Sept29_16['TT_EM0'],color='blue',linewidth=1.5,alpha=0.6,
             capthick=2, capsize=5)
plt.errorbar(Sept29_16.index,Sept29_16['ZZ_M0'],Sept29_16['ZZ_EM0'],color='red',linewidth=1.5,alpha=0.6,
             capthick=2, capsize=5)
plt.tight_layout(h_pad=5, w_pad=0.5) 


# In[ ]:




