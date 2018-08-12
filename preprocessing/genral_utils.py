import os
import csv

data_source_path = 'data_source'
raw_data_source_path = data_source_path+os.sep+'raw'+os.sep


def get_file_path(file_name):
    dirname = os.path.dirname(__file__)
    filepath = os.path.join(dirname, '..' + os.sep + raw_data_source_path)
    return os.path.join(filepath + file_name)


def save_file(file_name, title, patients_dic):
    write_file_path = get_file_path(file_name+'.csv')
    with open(write_file_path, 'w') as write_csv:
        w = csv.DictWriter(write_csv, title)
        w.writeheader()
        for d in patients_dic.keys():
            p_dic = patients_dic[d]
            w.writerow(p_dic)