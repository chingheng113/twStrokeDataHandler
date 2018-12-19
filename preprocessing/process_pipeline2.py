from tools import genral_utils as gu
from preprocessing import mRS_validator as mv
from preprocessing import clean_utils2 as clnUtil
from preprocessing import remove_missing_utils as nomissUtil
from preprocessing import denormalization_utils as deUtil
import pandas as pd
from functools import reduce


if __name__ == '__main__':

    # change 'raw_data_source_path' to raw2 !!!

    # ===================== Dataset structure denormalization
    deUtil.de_casedbmrs()
    deUtil.de_casednihs()
    # =====================  Datasets cleaning
    df_case = clnUtil.clean_case()
    df_mcase = clnUtil.clean_mcase()
    df_final_case = clnUtil.create_age(df_case, df_mcase)
    df_dbmrs = clnUtil.clean_dbmrs()
    df_nihs = clnUtil.clean_nihs()
    # =====================  Merge
    dfs = [df_final_case, df_dbmrs, df_nihs]
    df_joined = reduce(lambda left, right: pd.merge(left, right, on=['ICASE_ID', 'IDCASE_ID']), dfs)
    df_org = clnUtil.convert_features(df_joined)
    df_f = clnUtil.make_dummy(df_org)
    df_f = df_f[['IDCASE_ID', 'onset_age', 'GENDER_TX', 'Feeding', 'Transfers', 'Bathing', 'Toilet_use', 'Grooming', 'Mobility', 'Stairs', 'Dressing', 'Bowel_control', 'Bladder_control', 'discharged_mrs', 'NIHS_1a_out', 'NIHS_1b_out', 'NIHS_1c_out', 'NIHS_2_out', 'NIHS_3_out', 'NIHS_4_out', 'NIHS_5aL_out', 'NIHS_5bR_out', 'NIHS_6aL_out', 'NIHS_6bR_out', 'NIHS_7_out', 'NIHS_8_out', 'NIHS_9_out', 'NIHS_10_out', 'NIHS_11_out', 'ICD_ID_1.0', 'ICD_ID_2.0', 'ICD_ID_3.0', 'ICD_ID_4.0']]
    df_f.dropna(inplace=True)
    gu.save_dataframe_to_csv(df_f, 'tsr_mbn')
    print("Done")