import missingno as msno
# conda install -c conda-forge missingno
import pandas as pd
import matplotlib.pyplot as plt


def show_missing_missing_intensive_features(df):
    num_NaN = df.isna().sum().sort_values(ascending=False)
    print(num_NaN[0:60])
    '''
    CSAH_ID                     71057
    TRMOP_ID                    69081
    OMWA_TX                     68460
    ICDTIA_ID                   67046
    CICH_ID                     63084
    TOASTU_ID                   62475
    MCDLI_ID                    60531
    MCDRI_ID                    59840
    FH_HBP                      56265
    FH_DB                       56148
    FH_HD                       55939
    FH_ST                       55653
    tpa_fl                      52474
    CRP_NM                      51954
    OMNS_FL                     47860
    OMST_FL                     47767
    OMINS_FL                    47756
    OMORA_FL                    47641
    MCD_ID                      45683
    ALB_NM                      44099
    HBAC_NM                     43811
    MCDR_ID                     43165
    MCDL_ID                     42367
    MCDBA_ID                    42242
    MRS_12                 40486
    TCCSBA_ID              38721
    AC_NM                  37645
    VEIHD_12               37348
    VERS_12                37341
    TCCSR_ID               36090
    TCCSL_ID               36045
    UA_NM                  30963
    GOT_NM                 30104
    GPT_NM                 27263
    PTT1_NM                26712
    TCCS_ID                26478
    HDL_NM                 26421
    CDR_ID                 25459
    CDL_ID                 24133
    PTT2_NM                23685
    ER_NM                  21863
    LDL_NM                 21212
    MRS_6          20924
    PTINR_NM       20064
    TOAST_ID       19056
    VEIHD_6        17754
    VERS_6         17732
    TCHO_NM        16640
    BUN_NM         16036
    TG_NM          15665
    MRS_3     13868
    '''


def remove_missing_intensive_features(df):
    return df.drop(['CSAH_ID',
                    'TRMOP_ID',
                    'OMWA_TX',
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
                    'CRP_NM',
                    'OMNS_FL',
                    'OMST_FL',
                    'OMINS_FL',
                    'OMORA_FL',
                    'MCD_ID',
                    'ALB_NM',
                    'HBAC_NM',
                    'MCDR_ID',
                    'MCDL_ID',
                    'MCDBA_ID',
                    'TCCSBA_ID',
                    'AC_NM',
                    'TCCSR_ID',
                    'TCCSL_ID',
                    'UA_NM',
                    'GOT_NM',
                    'GPT_NM',
                    'PTT1_NM',
                    'TCCS_ID',
                    'HDL_NM',
                    'CDR_ID',
                    'CDL_ID',
                    'PTT2_NM',
                    'ER_NM',
                    'LDL_NM',
                    'PTINR_NM',
                    'TOAST_ID',
                    'TCHO_NM',
                    'BUN_NM',
                    'TG_NM'],
                   axis=1)

def plot_missing(df):
    msno.matrix(df)
    msno.bar(df)
    plt.show()