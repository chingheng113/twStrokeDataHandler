import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def scatt_plot(data):
    data.plot.scatter(x=data.columns[0], y=data.columns[1], c=data.columns[2], cmap=plt.cm.Spectral)
    plt.show()


def bubble_plot(data, group_names):
    data_size = data.groupby(group_names).size()
    keys = data.groupby(group_names).groups.keys()
    x =[]
    y =[]
    for key in keys:
        x.append(key[0])
        y.append(key[1])
    plt.scatter(x, y, s=data_size, alpha=.5)
    plt.xlabel(data.columns[0])
    plt.ylabel(data.columns[1])
    plt.show()


def violin_plot(data):
    sns.violinplot(data.iloc[: ,0], data.iloc[:, 1], orient='v')
    sns.despine()
    plt.show()


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


def plot_dbscan_group(db, df_xy, n_color=0):
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