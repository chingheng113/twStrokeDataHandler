from tools import genral_utils as gu
import numpy as np
from visualization import plot_utils as pu
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if __name__ == '__main__':
    # -- Load Data
    df_3m = pd.read_csv(gu.get_file_path('wholeset_Jim_nomissing.csv', under_raw=False),
                                  encoding='utf8')
    df_3m['bi_total'] = pd.DataFrame(
        np.sum(df_3m[['Feeding', 'Transfers', 'Bathing', 'Toilet_use', 'Grooming', 'Mobility',
                                'Stairs', 'Dressing', 'Bowel_control', 'Bladder_control']], axis=1))
    df_3m['nihss_total'] = pd.DataFrame(
        np.sum(df_3m[['NIHS_1a_out', 'NIHS_1b_out', 'NIHS_1c_out', 'NIHS_2_out', 'NIHS_3_out', 'NIHS_4_out',
                                'NIHS_5aL_out', 'NIHS_5bR_out', 'NIHS_6aL_out', 'NIHS_6bR_out', 'NIHS_7_out',
                                'NIHS_8_out',
                                'NIHS_9_out', 'NIHS_10_out', 'NIHS_11_out']], axis=1))
    bi_mrs = df_3m[['discharged_mrs', 'bi_total']]
    nih_mrs = df_3m[['nihss_total', 'bi_total']]
    # -- Load validated Data
    df_3m_validated = pd.read_csv(gu.get_file_path('wholeset_Jim_nomissing_validated.csv', under_raw=False), encoding='utf8')
    df_3m_validated['bi_total'] = pd.DataFrame(np.sum(df_3m_validated[['Feeding', 'Transfers', 'Bathing', 'Toilet_use', 'Grooming', 'Mobility',
                                             'Stairs', 'Dressing', 'Bowel_control', 'Bladder_control']], axis=1))
    df_3m_validated['nihss_total'] = pd.DataFrame(
        np.sum(df_3m_validated[['NIHS_1a_out', 'NIHS_1b_out', 'NIHS_1c_out', 'NIHS_2_out', 'NIHS_3_out', 'NIHS_4_out',
                   'NIHS_5aL_out', 'NIHS_5bR_out', 'NIHS_6aL_out', 'NIHS_6bR_out', 'NIHS_7_out', 'NIHS_8_out',
                   'NIHS_9_out', 'NIHS_10_out', 'NIHS_11_out']], axis=1))

    bi_mrs_validated = df_3m_validated[['discharged_mrs', 'bi_total']]
    nih_mrs_validated = df_3m_validated[['nihss_total', 'bi_total']]

    # -- Plot
    fig = plt.figure(figsize=(15, 5))
    pu.bubble_plot(bi_mrs, ['discharged_mrs', 'bi_total'])
    # pu.violin_plot(nih_mrs)
    # pu.violin_plot(bi_mrs_validated)
    # nih_mrs.boxplot(column=['bi_total'], by='nihss_total')
    # nih_mrs_validated.boxplot(column=['bi_total'], by='nihss_total')
    plt.show()