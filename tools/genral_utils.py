import os
import csv

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
    with open(write_file_path, 'w') as write_csv:
        w = csv.DictWriter(write_csv, title)
        w.writeheader()
        for d in patients_dic.keys():
            p_dic = patients_dic[d]
            w.writerow(p_dic)


def save_dataframe_to_csv(df, file_name):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, '..' + os.sep + data_source_path)
    df.to_csv(filepath + file_name + '.csv', sep=',', index=False)
