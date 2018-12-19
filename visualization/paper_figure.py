from tools import genral_utils as gu
import numpy as np
from visualization import plot_utils as pu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# t-SNE
# df = pd.read_csv(gu.get_file_path('reduced_dimension_30_2c.csv', under_raw=False), encoding='utf8')
# df_0 = df[df['p'] == 0]
# df_1 = df[df['p'] == 1]
# plt.figure()
# plt.scatter(df_0.ix[:,0], df_0.ix[:,1], c='blue', s=0.1, label='Good')
# plt.scatter(df_1.ix[:,0], df_1.ix[:,1], c='red', s=0.1, label='Poor')
# # plt.title('t-SNE 2D visualization of 90-day stroke mRS outcome')
# plt.rcParams["legend.markerscale"] = 10
# plt.legend()
# plt.xlabel('t-SNE 1')
# plt.ylabel('t-SNE 2')
# plt.savefig("t-sne.png", dpi=300)
# plt.show()

# BI v.s NIHSS
b = 'bi_total'
n = 'nihss_total'
m = 'discharged_mrs'
# TSR data
df_3m = pd.read_csv(gu.get_file_path('wholeset_Jim_nomissing.csv', under_raw=False),
                    encoding='utf8')
df_3m[b] = pd.DataFrame(np.sum(df_3m[['Feeding', 'Transfers', 'Bathing', 'Toilet_use', 'Grooming', 'Mobility',
                                      'Stairs', 'Dressing', 'Bowel_control', 'Bladder_control']], axis=1))
df_3m[n] = pd.DataFrame(np.sum(df_3m[['NIHS_1a_out', 'NIHS_1b_out', 'NIHS_1c_out', 'NIHS_2_out', 'NIHS_3_out', 'NIHS_4_out',
                                      'NIHS_5aL_out', 'NIHS_5bR_out', 'NIHS_6aL_out', 'NIHS_6bR_out', 'NIHS_7_out',
                                      'NIHS_8_out',
                                      'NIHS_9_out', 'NIHS_10_out', 'NIHS_11_out']], axis=1))
# TSR data validate
df_3m_validated = pd.read_csv(gu.get_file_path('wholeset_Jim_nomissing_validated.csv', under_raw=False), encoding='utf8')
df_3m_validated[b] = pd.DataFrame(np.sum(df_3m_validated[['Feeding', 'Transfers', 'Bathing', 'Toilet_use', 'Grooming', 'Mobility',
                                                                   'Stairs', 'Dressing', 'Bowel_control', 'Bladder_control']], axis=1))
df_3m_validated[n] = pd.DataFrame(np.sum(df_3m_validated[['NIHS_1a_out', 'NIHS_1b_out', 'NIHS_1c_out', 'NIHS_2_out', 'NIHS_3_out', 'NIHS_4_out',
                                                                      'NIHS_5aL_out', 'NIHS_5bR_out', 'NIHS_6aL_out', 'NIHS_6bR_out', 'NIHS_7_out', 'NIHS_8_out',
                                                                      'NIHS_9_out', 'NIHS_10_out', 'NIHS_11_out']], axis=1))
# NIH data
n_nih = 'Discharge: NIHSS Total'
b_nih = 'Discharge: Barthel Scale Total'
m_nih = 'Discharge: Rankin Score'
df_nih = pd.read_csv(gu.get_file_path('NIH_data.csv', under_raw=False), encoding='utf8')
df_nih_nbm = df_nih[[n_nih, b_nih, m_nih]]
df_nih_nbm = df_nih_nbm[df_nih_nbm[m_nih] != 6]


fig, (ax11, ax12) = plt.subplots(nrows=1, ncols=2, figsize=(15,5))
# fig, (ax11, ax12, ax13) = plt.subplots(nrows=1, ncols=3, figsize=(15,5))
a1 = ax11.scatter(df_3m[[n,b,m]].ix[:,0], df_3m[[n,b,m]].ix[:,1], c=df_3m[[n,b,m]].ix[:,2], cmap=plt.cm.Spectral)
# plt.title()
ax11.set_title('Raw Taiwan stroke registry data')
ax11.set_xlabel('Total discharge NIHSS')
ax11.set_ylabel('Total discharge Barthel Index')

ax12.scatter(df_3m_validated[[n,b,m]].ix[:,0], df_3m_validated[[n,b,m]].ix[:,1], c=df_3m_validated[[n,b,m]].ix[:,2], cmap=plt.cm.Spectral)
# plt.title()
ax12.set_title('Validated Taiwan stroke registry data')
ax12.set_xlabel('Total discharge NIHSS')
ax12.set_ylabel('Total discharge Barthel Index')

# ax13.scatter(df_nih_nbm.ix[:,0], df_nih_nbm.ix[:,1], c=df_nih_nbm.ix[:,2], cmap=plt.cm.Spectral)
# plt.title('NIH clinical trial data')
# ax13.set_title('NIH clinical trial dataa')
# ax13.set_xlabel('Total discharge NIHSS')
# ax13.set_ylabel('Total discharge Barthel Index')
#
fig.colorbar(a1).ax.set_ylabel('Discharge mRS')
fig.savefig("BIandNIHSS.png", dpi=600)
plt.show()