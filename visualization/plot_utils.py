import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def scatt_plot(data):
    data.plot.scatter(x=data.columns[0], y=data.columns[1])
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
