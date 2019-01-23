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
    # print(df_final_case.shape)
    # print(df_dbmrs.shape)
    # print(df_ctmr.shape)
    # print(df_dgfa.shape)
    # print(df_fahi.shape)
    # print(df_nihs.shape)
    # print(df_rfur.shape)
    # df_joined = reduce(lambda left, right: pd.merge(left, right, how='outer', on=['ICASE_ID', 'IDCASE_ID']), dfs)
    # print(df_joined.shape)
    #  ===================== convert feature
    # df_org = clnUtil.convert_features(df_joined)
    # gu.save_dataframe_to_csv(df_org, 'TSR_2018_withMissing')

    #  ######################################################## 3-month mRS#############################################
    #  ===================== Remove high missing features
    # df_withMissing = pd.read_csv(gu.get_file_path('TSR_2018_withMissing.csv', under_raw=False), encoding='utf8')
    # df_remove_hing_missing_columns = nomissUtil.remove_missing_intensive_features(df_withMissing)
    #  nomissUtil.plot_missing(df_remove_hing_missing_columns)
    #  ===================== only 3-month followup
    # df_3m = df_remove_hing_missing_columns.drop(['VERS_3', 'VERS_6', 'VERS_12', 'VEIHD_3', 'VEIHD_6', 'VEIHD_12', 'MRS_6', 'MRS_12'], axis=1)
    #  ===================== Remove NaN observations
    # df_3m.dropna(inplace=True)
    #  ===================== Remove dead cases
    # df_3m.drop(df_3m[df_3m.OFF_ID == 2.].index, inplace=True)
    #  ===================== Make dummy variables
    # df_3m = clnUtil.make_dummy(df_3m)
    # gu.save_dataframe_to_csv(df_3m, 'TSR_2018_3m_noMissing')
    #  ===================== validated mRS
    df_3m = pd.read_csv(gu.get_file_path('TSR_2018_3m_noMissing.csv', under_raw=False), encoding='utf8')
    df_3m_validated = mv.mRS_validate(df_3m)
    gu.save_dataframe_to_csv(df_3m_validated, 'TSR_2018_3m_noMissing_validated')
    print("Done")