from tools import genral_utils as gu
import numpy as np
from visualization import plot_utils as pu
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, DBSCAN
from visualization import plot_utils as pu



if __name__ == '__main__':
    # -- Load Data
    df = pd.read_csv(gu.get_file_path('NIH_data.csv', under_raw=False), encoding='utf8')
    n = 'Discharge: NIHSS Total'
    b = 'Discharge: Barthel Scale Total'
    m = 'Discharge: Rankin Score'
    df_nbm = df[[n, b, m]]
    df_nbm = df_nbm[df_nbm[m] != 6]
    df_nbm = df_nbm.dropna()

    # -- Plot
    # df_nbm[[m, b]].boxplot(column=[b], by=m)
    # fig = plt.figure(figsize=(15, 5))
    # pu.bubble_plot(df_nbm[[m, b]], [m, b])
    # pu.violin_plot(df_nbm[[m, n]])
    # df_nbm[[n, b]].boxplot(column=[b], by=n)
    pu.scatt_plot(df_nbm)
    plt.show()

    # for i in range(3, 4, 1):
    #     df_temp = df_nbm[df_nbm[m] == i]
    #     df_temp[n] = MinMaxScaler().fit_transform(df_temp[n].values.reshape(-1,1))
    #     df_temp[b] = MinMaxScaler().fit_transform(df_temp[b].values.reshape(-1,1))
    #     mSample = round(df_temp.shape[0]*0.1, 0)
    #     db = DBSCAN(eps=0.1, min_samples=mSample).fit(df_temp[[n, b]])
    #     pu.plot_dbscan(db, df_temp[[n, b]])
    # plt.show()
