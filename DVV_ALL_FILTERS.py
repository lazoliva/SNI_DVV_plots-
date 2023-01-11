#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import ConnectionPatch 


# In[29]:


# UPLOADING THE DATASET CONTAINING DV/V FOR THE 10 FILTERS USED.

Data = pd.read_csv (r'/Users/seismo_reynier/Documents/LocalPlotsData.csv', index_col=0, parse_dates=True)
Data.head()


# In[32]:


fig, axs = plt.subplots(10, figsize=(30, 30), sharex=True, sharey=True, facecolor = 'white', gridspec_kw={'hspace': 0})

# Filter 6 / 0.2-0.4 Hz
axs[0].plot(Data["TT_M0_6"], color = 'b', linewidth = 1.3, label='TT   (0.2-0.4 Hz)')
axs[0].plot(Data["ZZ_M0_6"], color = 'g', linewidth = 1.3, label='ZZ')
axs[0].grid() 
axs[0].legend()
axs[0].set_ylabel('dv/v(%)', fontsize=12)
axs[0].set_xlabel('Date', fontsize=12)
axs[0].set(ylim = (-0.3,0.15))
axs[0].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[0].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[0].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[0].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 7 / 0.4-0.6 Hz
axs[1].plot(Data["TT_M0_7"], color = 'b', linewidth = 1.3, label='TT   (0.4-0.6 Hz)')
axs[1].plot(Data["ZZ_M0_7"], color = 'g', linewidth = 1.3, label='ZZ')
axs[1].grid() 
axs[1].legend()
axs[1].set_ylabel('dv/v(%)', fontsize=12)
axs[1].set_xlabel('Date', fontsize=12)
axs[1].set(ylim = (-0.3,0.15))
axs[1].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[1].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[1].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[1].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 8 / 0.6-0.8 Hz
axs[2].plot(Data["TT_M0_8"], color = 'b', linewidth = 1.3, label='TT   (0.6-0.8 Hz)')
axs[2].plot(Data["ZZ_M0_8"], color = 'g', linewidth = 1.3, label='ZZ')
axs[2].grid() 
axs[2].legend()
axs[2].set_ylabel('dv/v(%)', fontsize=12)
axs[2].set_xlabel('Date', fontsize=12)
axs[2].set(ylim = (-0.3,0.15))
axs[2].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[2].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[2].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[2].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 9 / 0.8-1.0 Hz
axs[3].plot(Data["TT_M0_9"], color = 'b', linewidth = 1.3, label='TT   (0.8-1.0 Hz)')
axs[3].plot(Data["ZZ_M0_9"], color = 'g', linewidth = 1.3, label='ZZ')
axs[3].grid() 
axs[3].legend()
axs[3].set_ylabel('dv/v(%)', fontsize=12)
axs[3].set_xlabel('Date', fontsize=12)
axs[3].set(ylim = (-0.3,0.15))
axs[3].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[3].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[3].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[3].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 10 / 1.0-1.2 Hz
axs[4].plot(Data["TT_M0_10"], color = 'b', linewidth = 1.3, label='TT   (1.0-1.2 Hz)')
axs[4].plot(Data["ZZ_M0_10"], color = 'g', linewidth = 1.3, label='ZZ')
axs[4].grid() 
axs[4].legend()
axs[4].set_ylabel('dv/v(%)', fontsize=12)
axs[4].set_xlabel('Date', fontsize=12)
axs[4].set(ylim = (-0.3,0.15))
axs[4].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[4].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[4].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[4].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 11 / 1.2-2 Hz
axs[5].plot(Data["TT_M0_11"], color = 'b', linewidth = 1.3, label='TT   (1.2-2.0 Hz)')
axs[5].plot(Data["ZZ_M0_11"], color = 'g', linewidth = 1.3, label='ZZ')
axs[5].grid() 
axs[5].legend()
axs[5].set_ylabel('dv/v(%)', fontsize=12)
axs[5].set_xlabel('Date', fontsize=12)
axs[5].set(ylim = (-0.3,0.15))
axs[5].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[5].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[5].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[5].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 12 / 1.2-1.4 Hz
axs[6].plot(Data["TT_M0_12"], color = 'b', linewidth = 1.3, label='TT   (1.2-1.4 Hz)')
axs[6].plot(Data["ZZ_M0_12"], color = 'g', linewidth = 1.3, label='ZZ')
axs[6].grid() 
axs[6].legend()
axs[6].set_ylabel('dv/v(%)', fontsize=12)
axs[6].set_xlabel('Date', fontsize=12)
axs[6].set(ylim = (-0.3,0.15))
axs[6].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[6].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[6].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[6].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 13 / 1.4-1.6 Hz
axs[7].plot(Data["TT_M0_13"], color = 'b', linewidth = 1.3, label='TT   (1.2-1.6 Hz)')
axs[7].plot(Data["ZZ_M0_13"], color = 'g', linewidth = 1.3, label='ZZ')
axs[7].grid() 
axs[7].legend()
axs[7].set_ylabel('dv/v(%)', fontsize=12)
axs[7].set_xlabel('Date', fontsize=12)
axs[7].set(ylim = (-0.3,0.15))
axs[7].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[7].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[7].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[7].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 14 / 1.6-1.8 Hz
axs[8].plot(Data["TT_M0_14"], color = 'b', linewidth = 1.3, label='TT   (1.6-1.8 Hz)')
axs[8].plot(Data["ZZ_M0_14"], color = 'g', linewidth = 1.3, label='ZZ')
axs[8].grid() 
axs[8].legend()
axs[8].set_ylabel('dv/v(%)', fontsize=12)
axs[8].set_xlabel('Date', fontsize=12)
axs[8].set(ylim = (-0.3,0.15))
axs[8].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[8].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[8].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[8].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 15 / 1.8-2.0 Hz
axs[9].plot(Data["TT_M0_15"], color = 'b', linewidth = 1.3, label='TT   (1.8-2.0 Hz)')
axs[9].plot(Data["ZZ_M0_15"], color = 'g', linewidth = 1.3, label='ZZ')
axs[9].grid() 
axs[9].legend()
axs[9].set_ylabel('dv/v(%)', fontsize=12)
axs[9].set_xlabel('Date', fontsize=12)
axs[9].set(ylim = (-0.3,0.15))
axs[9].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[9].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[9].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[9].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Putting x-labels in the bottom plot 
for ax in axs:
    ax.label_outer()

# Saving figure
fig.savefig(r'/Users/seismo_reynier/Documents/zoomLocalStat.png', dpi = 50, bbox_inches = 'tight', pad_inches = 0.1)



# In[30]:


fig, axs = plt.subplots(5, figsize=(25, 18), sharex=True, sharey=True, facecolor = 'white', gridspec_kw={'hspace': 0})

# Filter 6 / 0.2-0.4 Hz
axs[0].plot(Data["TT_M0_6"], color = 'b', linewidth = 1.3, label='TT   (0.2-0.4 Hz)')
axs[0].plot(Data["ZZ_M0_6"], color = 'g', linewidth = 1.3, label='ZZ')
axs[0].grid() 
axs[0].legend()
axs[0].set_ylabel('dv/v(%)', fontsize=12)
axs[0].set_xlabel('Date', fontsize=12)
axs[0].set(ylim = (-0.3,0.15))
axs[0].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[0].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[0].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[0].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 7 / 0.4-0.6 Hz
axs[1].plot(Data["TT_M0_7"], color = 'b', linewidth = 1.3, label='TT   (0.4-0.6 Hz)')
axs[1].plot(Data["ZZ_M0_7"], color = 'g', linewidth = 1.3, label='ZZ')
axs[1].grid() 
axs[1].legend()
axs[1].set_ylabel('dv/v(%)', fontsize=12)
axs[1].set_xlabel('Date', fontsize=12)
axs[1].set(ylim = (-0.3,0.15))
axs[1].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[1].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[1].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[1].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 8 / 0.6-0.8 Hz
axs[2].plot(Data["TT_M0_8"], color = 'b', linewidth = 1.3, label='TT   (0.6-0.8 Hz)')
axs[2].plot(Data["ZZ_M0_8"], color = 'g', linewidth = 1.3, label='ZZ')
axs[2].grid() 
axs[2].legend()
axs[2].set_ylabel('dv/v(%)', fontsize=12)
axs[2].set_xlabel('Date', fontsize=12)
axs[2].set(ylim = (-0.3,0.15))
axs[2].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[2].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[2].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[2].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 9 / 0.8-1.0 Hz
axs[3].plot(Data["TT_M0_9"], color = 'b', linewidth = 1.3, label='TT   (0.8-1.0 Hz)')
axs[3].plot(Data["ZZ_M0_9"], color = 'g', linewidth = 1.3, label='ZZ')
axs[3].grid() 
axs[3].legend()
axs[3].set_ylabel('dv/v(%)', fontsize=12)
axs[3].set_xlabel('Date', fontsize=12)
axs[3].set(ylim = (-0.3,0.15))
axs[3].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[3].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[3].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[3].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')

# Filter 10 / 1.0-1.2 Hz
axs[4].plot(Data["TT_M0_10"], color = 'b', linewidth = 1.3, label='TT   (1.0-1.2 Hz)')
axs[4].plot(Data["ZZ_M0_10"], color = 'g', linewidth = 1.3, label='ZZ')
axs[4].grid() 
axs[4].legend()
axs[4].set_ylabel('dv/v(%)', fontsize=12)
axs[4].set_xlabel('Date', fontsize=12)
axs[4].set(ylim = (-0.3,0.15))
axs[4].axvspan(Data.index[335], Data.index[336], facecolor='red', alpha=0.9)
axs[4].axvspan(Data.index[122], Data.index[275], facecolor='yellow', alpha=0.2)
axs[4].text(Data.index[337], 0.055, "$M_w$ 5.5", fontsize=15, color='black')  
axs[4].text(Data.index[150], 0.055, "Reference period", fontsize=18, color='black')




plt.show()


# In[ ]:




