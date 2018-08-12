from preprocessing import dataset_denormalization_utils as deUtil
from preprocessing import clean_utils as clnUtil
from functools import reduce
import pandas as pd

if __name__ == '__main__':
    # Dataset structure denormalization
    deUtil.de_casedbmrs()
    deUtil.de_casedctmr()
    deUtil.de_casedfahi()
    deUtil.de_casedrfur()
    deUtil.de_casednihs()
    # Datasets cleaning
    df_case = clnUtil.clean_case()
    df_mcase = clnUtil.clean_mcase()
    df_final_case = clnUtil.create_age(df_case, df_mcase)
    df_dbmrs = clnUtil.clean_dbmrs()
    df_ctmr = clnUtil.clean_ctmr()
    df_dgfa = clnUtil.clean_dgfa()
    df_fahi = clnUtil.clean_fahi()
    df_nihs = clnUtil.clean_nihs()
    df_rfur = clnUtil.clean_rfur()
    # join datasets
    dfs = [df_final_case, df_dbmrs, df_ctmr, df_dgfa, df_fahi, df_nihs, df_rfur]
    df_joined = reduce(lambda left, right: pd.merge(left, right, on=['ICASE_ID', 'IDCASE_ID']), dfs)
    # convert feature
    df_org = clnUtil.convert_features(df_joined)


    print(df_org.shape)

    print("Done")