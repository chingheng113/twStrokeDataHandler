import os
import csv
import pandas as pd
import numpy as np
from sklearn import preprocessing as sp



data_source_path = 'data_source'+os.sep
raw_data_source_path = data_source_path+'raw'+os.sep


def get_file_path(file_name, under_raw):
    dirname = os.path.dirname(__file__)
    if(under_raw):
        filepath = os.path.join(dirname, '..' + os.sep + raw_data_source_path)
    else:
        filepath = os.path.join(dirname, '..' + os.sep + data_source_path)
    return os.path.join(filepath + file_name)


def save_array_to_csv(file_name, title, patients_dic, under_raw):
    write_file_path = get_file_path(file_name+'.csv', under_raw)
    with open(write_file_path, 'w', encoding="utf_8_sig", newline='') as write_csv:
        w = csv.DictWriter(write_csv, title)
        w.writeheader()
        for d in patients_dic.keys():
            p_dic = patients_dic[d]
            w.writerow(p_dic)


def save_dataframe_to_csv(df, file_name):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, '..' + os.sep + data_source_path)
    df.to_csv(filepath + file_name + '.csv', sep=',', index=False)


def load_all(fn):
    read_file_path = get_file_path(fn, under_raw=False)
    df = pd.read_csv(read_file_path, encoding='utf8')
    # df = df.ix[:100]
    return df.sample(frac=1)


def get_x_y_data(df):
    id_data = df[['ICASE_ID', 'IDCASE_ID']]
    y_data = df[['MRS_3']]
    x_data = df.drop(['ICASE_ID', 'IDCASE_ID', 'MRS_3'], axis=1)
    return id_data, x_data, y_data


def get_individual(fn):
    df = load_all(fn)
    id_data, x_data, y_data = get_x_y_data(df)
    return id_data, x_data, y_data


def get_poor_god(fn):
    df = load_all(fn)
    id_data, x_data, y_data = get_x_y_data(df)
    # Good < 3, Poor >= 3
    start = min(df['MRS_3'].values) - 1.0
    end = max(df['MRS_3'].values) + 1.0
    y_data = pd.cut(df['MRS_3'], [start, 3, end], labels=[0, 1], right=False)
    return id_data, x_data, y_data


def scale(x_data):
    # x_data = np.round(sp.MinMaxScaler(feature_range=(0, 1)).fit_transform(x_data), 3)
    x_data = np.round(sp.StandardScaler().fit_transform(x_data), 3)
    return x_data