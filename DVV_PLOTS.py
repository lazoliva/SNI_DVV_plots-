#!/usr/bin/env python
# coding: utf-8

# Script used to plot the dv/v time series results after running MSNoise.  

# In[22]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import ConnectionPatch 


# In[23]:


Data = pd.read_csv (r'/Users/seismo_reynier/Documents/Data.csv', index_col=0, parse_dates=True)


# In[24]:


Data.head()


# In[74]:


fig, (ax1, ax2) = plt.subplots(2,1, figsize = (18, 10), facecolor = 'white')
fig.subplots_adjust(hspace = 0.5)
ax1.plot(Data["TT_M0_8"], color = 'b', linewidth = 1.5, label='TT dv/v(0.6-0.8 Hz)') #alpha = 0.8 
ax1.set(ylim = (-0.15,0.10)) #yticks = np.arange(-0.15,0.10,0.02))
ax1.legend()
ax1.grid()
#ax1.set_title('Velocity variations in the TT component', fontsize=20)
ax1.set_ylabel('dv/v(%)', fontsize=15)
#ax1.set_xlabel('Date', fontsize=15)
#ax1.errorbar(M0.index, M0["TT_M0"], yerr = M0["TT_EM0"], linewidth = 1, color = "black", 
#             capthick = 2, capsize = 5, alpha = 0.3)
ax1.fill_between(Data.index, Data["TT_M0_8"] - Data["TT_EM0_8"], Data["TT_M0_8"] + Data["TT_EM0_8"], alpha = 0.3, 
                 color = 'royalblue') 
ax1.axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
ax1.axvspan(Data.index[32], Data.index[275], facecolor='yellow', alpha=0.2)
ax1.text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
ax1.text(Data.index[50], 0.055, "Reference period", fontsize=18, color='black')  

ax2.plot(Data["ZZ_M0_8"], color = 'g', linewidth = 1.5, label='ZZ dv/v(0.6-0.8 Hz)')
ax2.set(ylim = (-0.15,0.10)) #yticks = np.arange(-0.15,0.10,0.02))
ax2.legend()
ax2.grid()
#ax2.set_title('Velocity variations in the ZZ component', fontsize=20)
ax2.set_ylabel('dv/v(%)', fontsize=15)
ax2.set_xlabel('Date', fontsize=15)
#ax2.errorbar(M0.index, M0["ZZ_M0"], yerr = M0["ZZ_EM0"], linewidth = 1, color = "black", capsize = 3, alpha = 0.3)
#fig.tight_layout() #h_pad=5, w_pad=0.5 
#yerr = M0["ZZ_EM0"] 
ax2.fill_between(Data.index, Data["ZZ_M0_8"] - Data["ZZ_EM0_8"], Data["ZZ_M0_8"] + Data["ZZ_EM0_8"], alpha = 0.3, 
                 color = 'forestgreen') 
ax2.axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
ax2.axvspan(Data.index[32], Data.index[275], facecolor='yellow', alpha=0.2)
ax2.text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')
ax2.text(Data.index[50], 0.055, "Reference Period", fontsize=18, color='black')  
fig.tight_layout() #h_pad=5, w_pad=0.5 
plt.show()
fig.savefig(r'/Users/seismo_reynier/Documents/zoomP1.png', dpi = 300, bbox_inches = 'tight', pad_inches = 0.1)



# In[73]:


fig, axs = plt.subplots(3, figsize=(18, 12), sharex=True, sharey=True, facecolor = 'white', gridspec_kw={'hspace': 0})
#fig.suptitle('Velocity variations in three frequency bands')
axs[0].plot(Data["TT_M0_6"], color = 'b', linewidth = 1.3, label='TT_dv/v(0.2-0.4 Hz)')
axs[0].plot(Data["ZZ_M0_6"], color = 'g', linewidth = 1.3, label='ZZ_dv/v(0.2-0.4 Hz)')
axs[0].grid() 
axs[0].legend()
axs[0].set_ylabel('dv/v(%)', fontsize=12)
axs[0].set_xlabel('Date', fontsize=12)
axs[0].set(ylim = (-0.15,0.15))
axs[0].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[0].axvspan(Data.index[32], Data.index[275], facecolor='yellow', alpha=0.2)
axs[0].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[0].text(Data.index[50], 0.055, "Reference period", fontsize=18, color='black')  

axs[1].plot(Data["TT_M0_8"], color = 'b', linewidth = 1.3, label='TT_dv/v(0.6-0.8 Hz)')
axs[1].plot(Data["ZZ_M0_8"], color = 'g', linewidth = 1.3, label='ZZ_dv/v(0.6-0.8 Hz)')
axs[1].grid() 
axs[1].legend()
axs[1].set(ylim = (-0.15,0.15))
axs[1].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[1].set_ylabel('dv/v(%)', fontsize=12)
axs[1].set_xlabel('Date', fontsize=12)
axs[1].axvspan(Data.index[32], Data.index[275], facecolor='yellow', alpha=0.2)
axs[1].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[1].text(Data.index[50], 0.055, "Reference period", fontsize=18, color='black')  

axs[2].plot(Data["TT_M0_11"], color = 'b', linewidth = 1.3, label='TT_dv/v(1.2-2 Hz)')
axs[2].plot(Data["ZZ_M0_11"], color = 'g', linewidth = 1.3, label='ZZ_dv/v(1.2-2 Hz)')
axs[2].grid() 
axs[2].legend()
axs[2].set(ylim = (-0.15,0.15))
axs[2].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[2].set_ylabel('dv/v(%)', fontsize=12)
axs[2].set_xlabel('Date', fontsize=12)
axs[2].axvspan(Data.index[32], Data.index[275], facecolor='yellow', alpha=0.2)
axs[2].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[2].text(Data.index[50], 0.07, "Reference period", fontsize=18, color='black')  
#axs[2].text(339, 0.05, "earth")

# Hide x labels and tick labels for all but bottom plot.
for ax in axs:
    ax.label_outer()
fig.savefig(r'/Users/seismo_reynier/Documents/zoomP2.png', dpi = 300, bbox_inches = 'tight', pad_inches = 0.1)


# In[192]:



# Create main container with size of 6x5
fig = plt.figure(figsize=(6, 5), facecolor = 'white')
plt.subplots_adjust(bottom = 0., left = 0, top = 1., right = 1.2)
fig.subplots_adjust(hspace = 0.5)

# Create first axes, the top-left plot with green plot
sub1 = fig.add_subplot(2,2,1)# two rows, two columns, fist cell
sub1.plot(Data["TT_M0_8"], color = 'crimson', linewidth = 1.2)
sub1.plot(Data["ZZ_M0_8"], color = 'crimson', linewidth = 1.2)
sub1.set_xlim(Data.index[310],Data.index[344])
plt.xticks(rotation = 45, fontsize=10) 
sub1.set_ylim(-0.15,0.10)
sub1.set_ylabel('dv/v(%)', fontsize=15, labelpad = 15)
sub1.axvspan(Data.index[335],Data.index[335], color='black', alpha=0.9, linewidth= 1.9)

# Create second axes, the top-left plot with orange plot
sub2 = fig.add_subplot(2,2,2) # two rows, two columns, second cell
sub2.plot(Data["TT_M0_8"], color = 'cyan', linewidth = 1.2)
sub2.plot(Data["ZZ_M0_8"], color = 'cyan', linewidth = 1.2)
sub2.set_xlim(Data.index[348],Data.index[370])
plt.xticks(rotation = 45, fontsize=10) 
#sub2.set_ylim(-0.15,0.10)
#sub2.set_ylabel('dv/v(%)', fontsize=15, labelpad = 15)

#Create third axes, a combination of third and fourth cell
sub3 = fig.add_subplot(2,2,(3,4)) # two rows, two colums, combined third and fourth cell
sub3.plot(Data["TT_M0_8"], color = 'b', label='dv/v(0.6-0.8 Hz)', linewidth = 1.2) 
sub3.plot(Data["ZZ_M0_8"], color = 'g', label='dv/v(0.6-0.8 Hz)', linewidth = 1.2) 
sub3.legend() 
#sub3.set_xlim(0, 6.5)
sub3.set_ylim(-0.15,0.10)
sub3.set_xlabel('Date', fontsize = 15, labelpad = 15)
sub3.set_ylabel('dv/v(%)', fontsize=15, labelpad = 15)

# Create blocked area in third axes
sub3.axvspan(Data.index[335],Data.index[336], facecolor='black', alpha=0.9, linewidth= 1.9)
sub3.fill_between((Data.index[310],Data.index[344]), -0.15, 0.10, facecolor='red', alpha=0.4) # blocked area for first axes
sub3.fill_between((Data.index[348],Data.index[370]), -0.15, 0.10, facecolor='cyan', alpha=0.4) # blocked area for second axes

# Create left side of Connection patch for first axes
#con1 = ConnectionPatch(xyA= (1, -0.15), coordsA=sub1.transData, 
#                       xyB= (1, -0.04), coordsB=sub3.transData, color = 'red')
# Add left side to the figure
#fig.add_artist(con1)
#fig.savefig(r'/Users/seismo_reynier/Documents/zoom1.png', dpi = 300, bbox_inches = 'tight', pad_inches = 0.1)


# In[85]:


# Create main container with size of 6x5
fig = plt.figure(figsize=(6, 5), facecolor = 'white')
plt.subplots_adjust(bottom = 0., left = 0, top = 1., right = 1.2)
fig.subplots_adjust(hspace = 0.5)

# Create first axes, the top-left plot with green plot
sub1 = fig.add_subplot(2,2,1)# two rows, two columns, fist cell
sub1.plot(Data["ZZ_M0_8"], color = 'crimson', linewidth = 1.5)
sub1.set_xlim(Data.index[312],Data.index[348])
plt.xticks(rotation = 90, fontsize=10) 
sub1.set_ylim(-0.15,0.10)
sub1.set_ylabel('dv/v(%)', fontsize=15, labelpad = 15)
sub1.axvspan(Data.index[334],Data.index[334], color='black', alpha=0.9, linewidth= 1.2)
sub1.text(Data.index[335], 0.055, "$M_w$ 5.5", fontsize=13, color='black')  


# Create second axes, the top-left plot with orange plot
sub2 = fig.add_subplot(2,2,2) # two rows, two columns, second cell
sub2.plot(Data["ZZ_M0_8"], color = 'cyan', linewidth = 1.5)
sub2.set_xlim(Data.index[349],Data.index[375])
plt.xticks(rotation = 45, fontsize=10) 
sub2.set_ylim(-0.15,0.10)
#sub2.set_ylabel('dv/v(%)', fontsize=15, labelpad = 15)

#Create third axes, a combination of third and fourth cell
sub3 = fig.add_subplot(2,2,(3,4)) # two rows, two colums, combined third and fourth cell
sub3.plot(Data["ZZ_M0_8"], color = 'g', label='ZZ_dv/v(0.6-0.8 Hz)', linewidth = 1.3) 
sub3.legend()
#sub3.set_xlim(0, 6.5)
sub3.set_ylim(-0.15,0.10)
sub3.set_xlabel('Date', fontsize = 15, labelpad = 15)
sub3.set_ylabel('dv/v(%)', fontsize=15, labelpad = 15)
sub3.axvspan(Data.index[32], Data.index[275], facecolor='yellow', alpha=0.2)
sub3.text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=13, color='black')  
sub3.text(Data.index[50], -0.10, "Reference period", fontsize=12, color='black')  

# Create blocked area in third axes
sub3.axvspan(Data.index[335],Data.index[336], facecolor='black', alpha=0.9, linewidth= 1.9)
sub3.fill_between((Data.index[312],Data.index[348]), -0.15, 0.10, facecolor='red', alpha=0.4) # blocked area for first axes
sub3.fill_between((Data.index[349],Data.index[375]), -0.15, 0.10, facecolor='cyan', alpha=0.4) # blocked area for second axes

# Create left side of Connection patch for first axes
#con1 = ConnectionPatch(xyA= (1, -0.15), coordsA=sub1.transData, 
#                       xyB= (1, -0.04), coordsB=sub3.transData, color = 'red')
# Add left side to the figure
#fig.add_artist(con1)
fig.savefig(r'/Users/seismo_reynier/Documents/zoomP3.png', dpi = 300, bbox_inches = 'tight', pad_inches = 0.1)


# In[54]:


fig, (ax1, ax2) = plt.subplots(2,1, figsize = (18, 10), facecolor = 'white')
fig.subplots_adjust(hspace = 0.5)
ax1.plot(Data["TT_M0_8"], color = 'b', linewidth = 1.5, label='dv/v(0.6-0.8 Hz)')
ax1.text(Data.index[335], 0.02, "$M_w$ 5.5")
plt.show()


# In[ ]:




