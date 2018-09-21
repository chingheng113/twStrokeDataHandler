from tools import genral_utils as gu
from preprocessing import mRS_validator as mv
from preprocessing import clean_utils as clnUtil
from preprocessing import remove_missing_utils as nomissUtil
from preprocessing import denormalization_utils as deUtil
import pandas as pd
from functools import reduce


if __name__ == '__main__':
    # ===================== Dataset structure denormalization
    # deUtil.de_casedbmrs()
    # deUtil.de_casedctmr()
    # deUtil.de_casedfahi()
    # deUtil.de_casedrfur()
    # deUtil.de_casednihs()
    # =====================  Datasets cleaning
    # df_case = clnUtil.clean_case()
    # df_mcase = clnUtil.clean_mcase()
    # df_final_case = clnUtil.create_age(df_case, df_mcase)
    # df_dbmrs = clnUtil.clean_dbmrs()
    # df_ctmr = clnUtil.clean_ctmr()
    # df_dgfa = clnUtil.clean_dgfa()
    # df_fahi = clnUtil.clean_fahi()
    # df_nihs = clnUtil.clean_nihs()
    # df_rfur = clnUtil.clean_rfur()
    #  ===================== Join datasets
    # dfs = [df_final_case, df_dbmrs, df_ctmr, df_dgfa, df_fahi, df_nihs, df_rfur]
    # df_joined = reduce(lambda left, right: pd.merge(left, right, on=['ICASE_ID', 'IDCASE_ID']), dfs)
    #  ===================== convert feature
    # df_org = clnUtil.convert_features(df_joined)
    # gu.save_dataframe_to_csv(df_org, 'wholeset_Jim')

    #  ######################################################## 3-month mRS#############################################
    #  ===================== Remove high missing features
    # df_org = pd.read_csv(gu.get_file_path('wholeset_Jim.csv', under_raw=False), encoding='utf8')
    # df_3m = nomissUtil.remove_missing_intensive_features(df_org)
    #  nomissUtil.plot_missing(df_3m)
    #  ===================== only 3-month followup
    # df_3m.drop(['VERS_3', 'VERS_6', 'VERS_12', 'VEIHD_3', 'VEIHD_6', 'VEIHD_12', 'MRS_6', 'MRS_12'], axis=1, inplace=True)
    #  ===================== Remove NaN data
    # df_3m.dropna(inplace=True)
    #  ===================== not include dead subjects
    # df_3m.drop(df_3m[df_3m.OFF_ID == 2.].index, inplace=True)
    #  ===================== Make dummy variables
    # df_3m = clnUtil.make_dummy(df_3m)
    # gu.save_dataframe_to_csv(df_3m, 'wholeset_Jim_nomissing')
    #  ===================== validated mRS
    df_3m = pd.read_csv(gu.get_file_path('wholeset_Jim_nomissing.csv', under_raw=False), encoding='utf8')
    df_3m_validated = mv.mRS_validate(df_3m)
    # gu.save_dataframe_to_csv(df_3m_validated, 'wholeset_Jim_nomissing_validated')
    print("Done")