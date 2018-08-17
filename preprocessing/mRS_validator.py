import numpy as np
import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn import metrics
import matplotlib.pyplot as plt
import math
from scipy.spatial import distance
from scipy.spatial.distance import cdist
from collections import Counter
from sklearn.preprocessing import MinMaxScaler
from scipy.optimize import curve_fit
import scipy as sp
from biofits import fit_hyperbola, hyperbola
from preprocessing import clean_utils as clnUtil




def mRS_validate(df):
    df['bi_total'] = pd.DataFrame(np.sum(df[['Feeding', 'Transfers', 'Bathing', 'Toilet_use', 'Grooming', 'Mobility',
                                             'Stairs', 'Dressing', 'Bowel_control', 'Bladder_control']], axis=1))
    df['nihss_total'] = pd.DataFrame(np.sum(df[['NIHS_1a_out', 'NIHS_1b_out', 'NIHS_1c_out', 'NIHS_2_out', 'NIHS_3_out', 'NIHS_4_out',
                                            'NIHS_5aL_out', 'NIHS_5bR_out', 'NIHS_6aL_out', 'NIHS_6bR_out', 'NIHS_7_out', 'NIHS_8_out',
                                            'NIHS_9_out', 'NIHS_10_out', 'NIHS_11_out']], axis=1))
    df['nihss_total_in'] = pd.DataFrame(
                                        np.sum(df[['NIHS_1a_in', 'NIHS_1b_in', 'NIHS_1c_in', 'NIHS_2_in', 'NIHS_3_in', 'NIHS_4_in',
                                                   'NIHS_5aL_in', 'NIHS_5bR_in', 'NIHS_6aL_in', 'NIHS_6bR_in', 'NIHS_7_in', 'NIHS_8_in',
                                                   'NIHS_9_in', 'NIHS_10_in', 'NIHS_11_in']], axis=1))
    df_valied = logic_validate(df)
    df_valied = clust_validation(df_valied)
    df_valied = nihss_bi_iqr(df_valied)
    df_valied = curve_validation(df_valied)
    df_valied = df_valied.drop(['bi_total', 'nihss_total', 'nihss_total_in'], axis=1)
    return df_valied


def logic_validate(df):
    # print(df.shape)
    df = df[~((df['Mobility'] == 0) & (df['Stairs'] != 0))]
    # print(df.shape)
    df = df[~((df['Stairs'] == 10) & (df['NIHS_6aL_out'] == 4) & (df['NIHS_6bR_out'] == 4))]
    # print(df.shape)
    df = df[~((df['discharged_mrs'] != 5) & (df['NIHS_1a_out'] == 3))]
    # print(df.shape)
    df = df[~(df['nihss_total'] > 39)]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_1b_out'] != 2))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_1c_out'] != 2))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_4_out'] != 3))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_5aL_out'] != 4))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_5bR_out'] != 4))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_6aL_out'] != 4))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_6bR_out'] != 4))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_7_out'] != 0))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_8_out'] != 2))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_9_out'] != 3))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_10_out'] != 2))]
    # print(df.shape)
    df = df[~((df['NIHS_1a_out'] == 3) & (df['NIHS_11_out'] != 0))]
    # print(df.shape)
    df = df[~((df['bi_total'] == 0) & (df['discharged_mrs'] == 0))]
    # print(df.shape)
    return df


def clust_validation(df):
    # http://scikit-learn.org/stable/auto_examples/cluster/plot_dbscan.html
    # https://stackoverflow.com/questions/12893492/choosing-eps-and-minpts-for-dbscan-r
    print(df.shape)
    scaler = MinMaxScaler()
    for i in range(0, 6, 1):
        df_temp = df[df['discharged_mrs'] == i]
        df_temp_inx = pd.DataFrame(df_temp.index.values, columns=['indx'])
        bi_mrs = df_temp[['discharged_mrs', 'bi_total']]
        # Compute DBSCAN
        mSample = round(bi_mrs.shape[0]/5, 0)
        db = DBSCAN(eps=5, min_samples=mSample).fit(bi_mrs)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        # Noise
        labels = db.labels_
        df_temp_inx['clust'] = labels
        df_temp_inx_noise = df_temp_inx[df_temp_inx['clust'] == -1]
        print(df_temp_inx_noise.shape)
        df = df.drop(df_temp_inx_noise['indx'])
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        print('Estimated number of clusters: %d' % n_clusters_)
        # print("Silhouette Coefficient: %0.3f" % metrics.silhouette_score(bi_mrs, labels))
        # Plot
        # plot_dbscan(db, bi_mrs)
        print(df.shape)
    plt.show()
    return df


def plot_dbscan(db, df_xy):
    # Plot result
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    # Black removed and is used for noise instead.
    unique_labels = set(labels)
    colors = [plt.cm.Spectral(each)
              for each in np.linspace(0, 1, len(unique_labels))]
    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)

        xy = df_xy[class_member_mask & core_samples_mask]
        plt.plot(xy.iloc[:, 0], xy.iloc[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)

        xy = df_xy[class_member_mask & ~core_samples_mask]
        plt.plot(xy.iloc[:, 0], xy.iloc[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)


def dbscan_parameter(X):
    # eps过大，则更多的点会落在核心对象的ϵ - 邻域，此时我们的类别数可能会减少， 本来不应该是一类的样本也会被划为一类。反之则类别数可能会增大，本来是一类的样本却被划分开。
    # min_samples 通常和eps一起调参。在eps一定的情况下，min_samples过大，则核心对象会过少，此时簇内部分本来是一类的样本可能会被标为噪音点，类别数也会变多。反之min_samples过小的话，则会产生大量的核心对象，可能会导致类别数过少。
    # ns = 2
    # nbrs = NearestNeighbors(n_neighbors=ns).fit(X)
    # distances, indices = nbrs.kneighbors(X)
    # distanceDec = sorted(distances[:, ns - 1], reverse=True)
    # plt.plot(list(range(1, X.shape[0] + 1)), distanceDec, 'bx')

    # distortions = []
    # K = range(1, 20)
    # for k in K:
    #     kmeanModel = KMeans(n_clusters=k).fit(X)
    #     kmeanModel.fit(X)
    #     distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, 'euclidean'), axis=1)) / X.shape[0])
    # # Plot the elbow
    # fig = plt.figure(figsize=(15, 5))
    # plt.grid(True)
    # plt.plot(K, distortions,  'bx-')
    # plt.xlabel('k')
    # plt.ylabel('Distortion')
    # plt.title('The Elbow Method showing the optimal k')

    # min_samples
    # labels, values = zip(*Counter(X['bi_total']).items())
    labels, values = zip(*Counter(X['bi_total']).most_common())
    indexes = np.arange(len(labels))
    width = 0.5
    fig = plt.figure(figsize=(15, 5))
    plt.bar(indexes, values, width)


def curve_validation(df):
    # -- Polyfit
    # https: // www.scipy - lectures.org / intro / numpy / auto_examples / plot_polyfit.html
    p = np.poly1d(np.polyfit(df['nihss_total'], df['bi_total'], 2))
    t = np.linspace(min(df['nihss_total']), max(df['nihss_total']), len(df['nihss_total']) * 1000)
    plt.plot(df['nihss_total'], df['bi_total'], 'o', t, p(t), '-')
    plt.xlabel("nihss_total")
    plt.ylabel("bi_total")
    plt.show()
    # ----- Curve Fit
    # popt, pcov = curve_fit(func, df['nihss_total'], df['bi_total'])
    # plt.plot(df['nihss_total'], df['bi_total'], 'o')
    # y2 = [func(i, popt[0], popt[1], popt[2]) for i in df['nihss_total']]
    # plt.plot(df['nihss_total'], y2, 'o')
    # plt.xlabel("nihss_total")
    # plt.ylabel("bi_total")
    # plt.show()
    # --- Hyperbolic Fit
    # https: // github.com / jimrybarski / biofits
    # perform the fit
    x_data = df['nihss_total']
    y_data = df['bi_total']
    yint, yint_stddev, delta_y, delta_y_stddev, kd, kd_stddev = fit_hyperbola(x_data, y_data)
    x = np.linspace(min(x_data), max(x_data), len(x_data) * 1000)
    y = hyperbola(x, yint, delta_y, kd)
    plt.figure(figsize=(5, 5))
    plt.plot(x, y, label='fit', zorder=0)
    plt.plot(x_data, y_data, 'o', label='data', markersize=4)
    plt.xlabel("nihss_total")
    plt.ylabel("bi_total")
    plt.show()
    return df


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def nihss_bi_iqr(df):
    # nih_mrs = df[['nihss_total', 'bi_total']]
    s = int(min(df['nihss_total']))
    e = int(max(df['nihss_total']))
    for i in range(s, e, 1):
        df_partial = df[df['nihss_total']==i]
        is_outlier = clnUtil.outliers_iqr(df_partial["bi_total"])
        df.drop(df_partial[is_outlier].index, inplace=True)
    return df