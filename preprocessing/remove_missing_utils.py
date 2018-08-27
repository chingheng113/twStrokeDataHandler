import missingno as msno
# conda install -c conda-forge missingno
import pandas as pd
import matplotlib.pyplot as plt


def show_missing_missing_intensive_features(df):
    num_NaN = df.isna().sum().sort_values(ascending=False)
    print(num_NaN[0:60])
    '''
    CSAH_ID      71057
    TRMOP_ID     69081
    ICDTIA_ID    67046
    CICH_ID      63084
    TOASTU_ID    62475
    MCDLI_ID     60531
    MCDRI_ID     59840
    FH_HBP       56265
    FH_DB        56148
    FH_HD        55939
    FH_ST        55653
    TPA_FL       52474
    OMNS_FL      47860
    OMST_FL      47767
    OMINS_FL     47756
    OMORA_FL     47641
    MCD_ID       45683
    MCDR_ID      43165
    MCDL_ID      42367
    MCDBA_ID     42242
            MRS_12       40486
            TCCSBA_ID    38721
            VEIHD_12     37348
            VERS_12      37341
            TCCSR_ID     36090
            TCCSL_ID     36045
            TCCS_ID      26478
            CDR_ID       25459
            CDL_ID       24133
            MRS_6        20924
            TOAST_ID     19056
            VEIHD_6      17754
            VERS_6       17732
                    MRS_3        13868
    '''


def remove_missing_intensive_features(df):
    return df.drop(['CSAH_ID',
                    'TRMOP_ID',
                    'ICDTIA_ID',
                    'CICH_ID',
                    'TOASTU_ID',
                    'MCDLI_ID',
                    'MCDRI_ID',
                    'FH_HBP',
                    'FH_DB',
                    'FH_HD',
                    'FH_ST',
                    'TPA_FL',
                    'OMNS_FL',
                    'OMST_FL',
                    'OMINS_FL',
                    'OMORA_FL',
                    'MCD_ID',
                    'MCDR_ID',
                    'MCDL_ID',
                    'MCDBA_ID',
                    'TCCSBA_ID',
                    'TCCSR_ID',
                    'TCCSL_ID',
                    'TCCS_ID',
                    'CDR_ID',
                    'CDL_ID',
                    'TOAST_ID'],
                   axis=1)


def plot_missing(df):
    msno.matrix(df)
    msno.bar(df)
    plt.show()