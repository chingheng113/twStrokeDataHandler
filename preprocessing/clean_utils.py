from tools import genral_utils as gu
import pandas as pd
import numpy as np
import math

def outliers_iqr(ys):
    '''
    http://colingorrie.github.io/outlier-detection.html
    '''
    ys = ys.apply(pd.to_numeric, errors='coerce')
    quartile_1 = ys.quantile(0.25)
    quartile_3 = ys.quantile(0.75)
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return (ys > upper_bound) | (ys < lower_bound)


def out_of_range(ys, r):
    ys = ys.apply(pd.to_numeric, errors='coerce')
    r = np.asarray(r).astype(float)
    return ~ys.isin(r)


def replace_flg(df, cols):
    df[cols] = df[cols].replace({'N': '0', 'Y': '1'})
    df[cols] = df[cols].replace(to_replace=r"[^0-1]", value=np.NaN, regex=True)
    return df


def not_icd(ys):
    icds = ['434', '431', '435', '436', '433', '430', '437']
    code = str(ys)
    parent = code.split('.')[0]
    if len(parent) != 3:
        return True
    else:
        if parent in icds:
            return False
        else:
            return True


def clean_case():
    fn = 'CASEDCASE-2016-05-2.csv'
    read_file_path = gu.get_file_path(fn, under_raw=True)
    df_case = pd.read_csv(read_file_path, encoding='utf8')
    # Dropping unused column
    df_case = df_case.drop(
        ['IPROTOCOL_ID', 'IPROTOCOL_ID', 'ORG_ID', 'CSTATUS_ID', 'DCTYPE24_ID', 'PATIENT_ID', 'INPUT_NM', 'AGE_NM',
         'EDU_ID', 'PRO_ID', 'PROOT_TX', 'ITOWN_ID', 'ADDR_TX', 'TELH_TX', 'TELP_TX', 'TELF_TX', 'FTITLE_TX',
         'CASEMEMO_TX', 'IH_FL', 'IH_DT', 'OH_DT', 'ONSETH_NM', 'ONSETM_NM', 'ONSET_FL', 'OT_DT', 'OTTIH_NM', 'OTTIM_NM',
         'OT_FL', 'FLOOK_DT', 'FLOOKH_NM', 'FLOOKM_NM', 'FLOOK_FL', 'FCT_DT', 'FCTH_NM', 'FCTM_NM', 'FCTOH_FL',
         'IVTPATH_ID', 'IVTPATH_FL', 'IVTPAAH_FL', 'IVTPA_DT', 'IVTPAH_NM', 'IVTPAM_NM', 'NIVTPA1_FL', 'NIVTPA2_FL',
         'NIVTPA3_FL', 'NIVTPA4_FL', 'NIVTPA5_FL', 'NIVTPA6_FL', 'NIVTPA7_FL', 'NIVTPA8_FL', 'NIVTPA9_FL', 'NIVTPA10_FL',
         'NIVTPA11_FL', 'NIVTPA99_FL', 'NIVTPA99_TX', 'ICDO_TX', 'TOASTSCAT_TX', 'TOASTSO_FL', 'TOASTSO_TX', 'CSAHO_TX',
         'THD_ID', 'THDO_FL', 'THDOO_FL', 'THDOO_TX', 'TRM_ID', 'TRMEN_ID', 'TRMOT_FL', 'TRMOT_TX', 'OM_ID', 'OM_FL',
         'OMAND_ID', 'OMLI_ID', 'OMLIOT_FL', 'OMLIOT_TX', 'OMLIOT2_FL', 'OMLIOT2_TX', 'AM_FL', 'AMLIOT_FL', 'AMLIOT_TX',
         'AMLIOT2_FL', 'AMLIOT2_TX', 'COM_ID', 'COMO_TX', 'DET_ID', 'DETO_TX', 'DETO_FL', 'OFFD_DT', 'OFFD_ID', 'OFFD_TX',
         'OFFDTORG_ID', 'OFFDTORG_TX', 'OFFRE_DT', 'NIHSIN_DT', 'NIHSINTI_TX', 'NIHSINH_NM', 'NIHSINM_NM', 'NIHSOT_DT',
         'NIHSOTTI_TX', 'NIHSOTH_NM', 'NIHSOTM_NM', 'BRS_DT', 'CT_DT', 'CTTI_TX', 'CTH_NM', 'CTM_NM', 'CTO_TX', 'MRI_DT',
         'MRITI_TX', 'MRIH_NM', 'MRIM_NM', 'MRIO_TX', 'ECG_ID', 'ECGO_FL', 'ECGO_TX', 'CREATE_DT', 'CREATESTAFF_ID',
         'SYSUPD_DT', 'SYSUPDSTAFF_ID', 'MODIFY_NM', 'IGUID_FT', 'DETHOH_FL', 'OMAD_FL', 'OMAD_ID'],
        axis=1)
    # Replace NULL to NaN
    df_case.replace('NULL', np.nan)
    # Replace outlier to NAN
    outlier_cols = ['HEIGHT_NM', 'WEIGHT_NM', 'SBP_NM', 'DBP_NM', 'BT_NM', 'HR_NM', 'RR_NM', 'HB_NM', 'HCT_NM',
                    'PLATELET_NM', 'WBC_NM', 'PTT1_NM', 'PTT2_NM', 'PTINR_NM', 'ER_NM', 'BUN_NM', 'CRE_NM', 'ALB_NM',
                    'CRP_NM', 'HBAC_NM', 'AC_NM', 'UA_NM', 'TCHO_NM', 'TG_NM', 'HDL_NM', 'LDL_NM', 'GOT_NM', 'GPT_NM',
                    'HB_NM', 'HCT_NM', 'PLATELET_NM', 'WBC_NM', 'PTT1_NM', 'PTT2_NM', 'PTINR_NM', 'ER_NM', 'BUN_NM',
                    'CRE_NM', 'ALB_NM', 'CRP_NM', 'HBAC_NM', 'AC_NM', 'UA_NM', 'TCHO_NM', 'TG_NM', 'HDL_NM', 'LDL_NM',
                    'GOT_NM', 'GPT_NM', 'OMWA_TX']
    df_case[outlier_cols] = df_case[outlier_cols].replace(999.9, np.nan)
    for col in outlier_cols:
        df_case.loc[outliers_iqr(df_case[col]), col] = np.nan
    df_case[outlier_cols] = df_case[outlier_cols].apply(pd.to_numeric, errors='coerce')
    # Replace un-coded value to Nan
    df_case.loc[out_of_range(df_case['OPC_ID'], ['1', '2', '3']), 'OPC_ID'] = np.nan
    df_case.loc[out_of_range(df_case['GCSE_NM'], ['1', '2', '3', '4', '5', '6']), 'GCSE_NM'] = np.nan
    df_case.loc[out_of_range(df_case['GCSV_NM'], ['1', '2', '3', '4', '5', '6']), 'GCSV_NM'] = np.nan
    df_case.loc[out_of_range(df_case['GCSM_NM'], ['1', '2', '3', '4', '5', '6']), 'GCSM_NM'] = np.nan
    df_case.loc[out_of_range(df_case['ICD_ID'], ['1', '2', '3', '4']), 'ICD_ID'] = np.nan
    df_case.loc[out_of_range(df_case['ICDTIA_ID'], ['1', '2']), 'ICDTIA_ID'] = np.nan
    df_case.loc[out_of_range(df_case['TOAST_ID'], ['1', '2', '3', '4', '5']), 'TOAST_ID'] = np.nan
    df_case.loc[out_of_range(df_case['TOASTU_ID'], ['1', '2', '3']), 'TOASTU_ID'] = np.nan
    df_case.loc[out_of_range(df_case['CICH_ID'], ['1', '2']), 'CICH_ID'] = np.nan
    df_case.loc[out_of_range(df_case['CSAH_ID'], ['1', '2', '3', '4']), 'CSAH_ID'] = np.nan
    df_case.loc[out_of_range(df_case['TRMOP_ID'], ['1', '2', '3', '4', '5']), 'TRMOP_ID'] = np.nan
    df_case.loc[out_of_range(df_case['OFF_ID'], ['1', '2', '3']), 'OFF_ID'] = np.nan
    df_case.loc[out_of_range(df_case['OFFDT_ID'], ['1', '2', '3', '4', '5']), 'OFFDT_ID'] = np.nan
    df_case.loc[out_of_range(df_case['CD_ID'], ['0', '1', '2']), 'CD_ID'] = np.nan
    df_case.loc[out_of_range(df_case['CDR_ID'], ['1', '2', '3', '4']), 'CDR_ID'] = np.nan
    df_case.loc[out_of_range(df_case['CDL_ID'], ['1', '2', '3', '4']), 'CDL_ID'] = np.nan
    df_case.loc[out_of_range(df_case['TCCS_ID'], ['0', '1']), 'TCCS_ID'] = np.nan
    df_case.loc[out_of_range(df_case['TCCSR_ID'], ['1', '2', '3']), 'TCCSR_ID'] = np.nan
    df_case.loc[out_of_range(df_case['TCCSL_ID'], ['1', '2', '3']), 'TCCSL_ID'] = np.nan
    df_case.loc[out_of_range(df_case['TCCSBA_ID'], ['1', '2', '3']), 'TCCSBA_ID'] = np.nan
    df_case.loc[out_of_range(df_case['MCDR_ID'], ['1', '2', '3']), 'MCDR_ID'] = np.nan
    df_case.loc[out_of_range(df_case['MCDL_ID'], ['1', '2', '3']), 'MCDL_ID'] = np.nan
    df_case.loc[out_of_range(df_case['MCDBA_ID'], ['1', '2', '3']), 'MCDBA_ID'] = np.nan
    df_case.loc[out_of_range(df_case['MCDRI_ID'], ['1', '2', '3']), 'MCDRI_ID'] = np.nan
    df_case.loc[out_of_range(df_case['MCDLI_ID'], ['1', '2', '3']), 'MCDLI_ID'] = np.nan
    #
    df_case.loc[df_case['ICD_TX'].apply(not_icd), 'ICD_TX'] = np.nan
    #
    toas_cols = ['TOASTLE_FL', 'TOASTLI_FL', 'TOASTSCE_FL', 'TOASTSMO_FL', 'TOASTSRA_FL', 'TOASTSDI_FL', 'TOASTSMI_FL',
                 'TOASTSANTIP_FL', 'TOASTSAU_FL', 'TOASTSHY_FL', 'TOASTSPR_FL', 'TOASTSANTIT_FL', 'TOASTSHO_FL',
                 'TOASTSHYS_FL', 'TOASTSCA_FL']
    thd_cols = ['THDA_FL', 'THDH_FL', 'THDI_FL', 'THDAM_FL', 'THDV_FL', 'THDE_FL', 'THDM_FL', 'THDR_FL', 'THDP_FL']
    trm_cols = ['TRMAN_FL', 'TRMAS_FL', 'TRMTI_FL', 'TRMHE_FL', 'TRMWA_FL', 'TRMIA_FL', 'TRMFO_FL', 'TRMTA_FL',
                'TRMSD_FL', 'TRMRE_FL', 'TRMEN_FL', 'TRMAG_FL', 'TRMCL_FL', 'TRMPL_FL', 'TRMLM_FL',
                'TRMIV_FL', 'TRMVE_FL', 'TRMNG_FL', 'TRMDY_FL', 'TRMICU_FL', 'TRMSM_FL', 'TRMED_FL', 'TRMOP_FL']
    om_cols = ['OMAS_FL', 'OMAG_FL', 'OMTI_FL', 'OMCL_FL', 'OMWA_FL', 'OMPL_FL', 'OMANH_FL', 'OMAND_FL', 'OMORA_FL',
               'OMINS_FL', 'OMLI_FL', 'OMST_FL', 'OMNS_FL']
    am_cols = ['AMAS_FL', 'AMAG_FL', 'AMTI_FL', 'AMCL_FL', 'AMWA_FL', 'AMPL_FL', 'AMANH_FL', 'AMAND_FL', 'AMLI_FL']
    com_cols = ['COMPN_FL', 'COMUT_FL', 'COMUG_FL', 'COMPR_FL', 'COMPU_FL', 'COMAC_FL', 'COMSE_FL', 'COMDE_FL', 'COMO_FL']
    det_cols = ['DETST_FL', 'DETHE_FL', 'DETHO_FL', 'DETHA_FL', 'DETVA_FL', 'DETRE_FL', 'DETME_FL']
    cm_cols = ['CT_FL', 'MRI_FL']
    ecg_cols = ['ECGL_FL', 'ECGA_FL', 'ECGQ_FL']
    mcd_cold = ['MCD_ID', 'MRA_FL', 'CTA_FL', 'DSA_FL']
    all_cols = toas_cols+thd_cols+trm_cols+om_cols+am_cols+com_cols+det_cols+cm_cols+ecg_cols+mcd_cold
    df_case[all_cols] = replace_flg(df_case[all_cols], all_cols)
    return df_case


def clean_dbmrs():
    fn = 'CASEDBMRS(denormalized).csv'
    read_file_path = gu.get_file_path(fn, under_raw=True)
    df_dbmrs = pd.read_csv(read_file_path, encoding='utf8')
    df_dbmrs.loc[out_of_range(df_dbmrs['Feeding'], ['0', '5', '10']), 'Feeding'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Transfers'], ['0', '5', '10', '15']), 'Transfers'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Bathing'], ['0', '5']), 'Bathing'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Toilet_use'], ['0', '5', '10']), 'Toilet_use'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Grooming'], ['0', '5']), 'Grooming'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Mobility'], ['0', '5', '10', '15']), 'Mobility'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Stairs'], ['0', '5', '10']), 'Stairs'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Dressing'], ['0', '5', '10']), 'Dressing'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Bowel_control'], ['0', '5', '10']), 'Bowel_control'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['Bladder_control'], ['0', '5', '10']), 'Bladder_control'] = np.nan
    df_dbmrs.loc[out_of_range(df_dbmrs['discharged_mrs'], ['0', '1', '2', '3', '4', '5', '6']), 'discharged_mrs'] = np.nan
    return df_dbmrs


def clean_ctmr():
    fn = 'CASEDCTMR(denormalized).csv'
    read_file_path = gu.get_file_path(fn, under_raw=True)
    df_ctmr = pd.read_csv(read_file_path, encoding='utf8')
    df_ctmr.iloc[:, 2:df_ctmr.shape[1]] = df_ctmr.iloc[:, 2:df_ctmr.shape[1]].replace({'N': '0', 'Y': '1'})
    return df_ctmr


def clean_dgfa():
    fn = 'CASEDDGFA.csv'
    read_file_path = gu.get_file_path(fn, under_raw=True)
    df_dgfa = pd.read_csv(read_file_path, encoding='utf8')
    df_dgfa = df_dgfa.drop('IPROTOCOL_ID', axis=1)
    df_dgfa = df_dgfa.drop(['HDMT_ID', 'PCVAMT_ID', 'POMT_ID', 'UA_ID', 'UAMT_ID', 'URMT_ID',
                            'SMC_NM', 'SMY_NM', 'SMCP_ID', 'PTIAMT_ID', 'HCY_NM', 'HCMT_ID',
                            'HTY_NM', 'HTMT_ID', 'DMY_NM', 'DMMT_ID', 'PADMT_ID',
                            'CA_TX', 'OT_ID', 'OT_TX', 'THISHC_ID', 'THISHY_ID', 'THISDI_ID', 'IGUID_FT'], axis=1)
    df_dgfa.loc[out_of_range(df_dgfa['HD_ID'], ['0', '1']), 'HD_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['PCVA_ID'], ['0', '1']), 'PCVA_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['PCVACI_ID'], ['0', '1']), 'PCVACI_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['PCVACH_ID'], ['0', '1']), 'PCVACH_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['PO_ID'], ['0', '1']), 'PO_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['UR_ID'], ['0', '1']), 'UR_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['SM_ID'], ['0', '1']), 'SM_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['PTIA_ID'], ['0', '1']), 'PTIA_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['HC_ID'], ['0', '1']), 'HC_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['HCHT_ID'], ['0', '1']), 'HCHT_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['HCHC_ID'], ['0', '1']), 'HCHC_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['HT_ID'], ['0', '1']), 'HT_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['DM_ID'], ['0', '1']), 'DM_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['PAD_ID'], ['0', '1']), 'PAD_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['AL_ID'], ['0', '1']), 'AL_ID'] = np.nan
    df_dgfa.loc[out_of_range(df_dgfa['CA_ID'], ['0', '1']), 'CA_ID'] = np.nan
    return df_dgfa


def clean_fahi():
    fn = 'CASEDFAHI(denormalized).csv'
    read_file_path = gu.get_file_path(fn, under_raw=True)
    df_fahi = pd.read_csv(read_file_path, encoding='utf8')
    return df_fahi


def clean_nihs():
    fn = 'CASEDNIHS(denormalized).csv'
    read_file_path = gu.get_file_path(fn, under_raw=True)
    df_nihs = pd.read_csv(read_file_path, encoding='utf8')
    df_nihs.loc[out_of_range(df_nihs['NIHS_1a_in'], ['0', '1', '2', '3']), 'NIHS_1a_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_1a_out'], ['0', '1', '2', '3']), 'NIHS_1a_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_1b_in'], ['0', '1', '2']), 'NIHS_1b_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_1b_out'], ['0', '1', '2']), 'NIHS_1b_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_1c_in'], ['0', '1', '2']), 'NIHS_1c_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_1c_out'], ['0', '1', '2']), 'NIHS_1c_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_2_in'], ['0', '1', '2']), 'NIHS_2_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_2_out'], ['0', '1', '2']), 'NIHS_2_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_3_in'], ['0', '1', '2', '3']), 'NIHS_3_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_3_out'], ['0', '1', '2', '3']), 'NIHS_3_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_4_in'], ['0', '1', '2', '3']), 'NIHS_4_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_4_out'], ['0', '1', '2', '3']), 'NIHS_4_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_5aL_in'], ['0', '1', '2', '3', '4']), 'NIHS_5aL_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_5aL_out'], ['0', '1', '2', '3', '4']), 'NIHS_5aL_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_5bR_in'], ['0', '1', '2', '3', '4']), 'NIHS_5bR_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_5bR_out'], ['0', '1', '2', '3', '4']), 'NIHS_5bR_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_6aL_in'], ['0', '1', '2', '3', '4']), 'NIHS_6aL_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_6aL_out'], ['0', '1', '2', '3', '4']), 'NIHS_6aL_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_6bR_in'], ['0', '1', '2', '3', '4']), 'NIHS_6bR_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_6bR_out'], ['0', '1', '2', '3', '4']), 'NIHS_6bR_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_7_in'], ['0', '1', '2']), 'NIHS_7_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_7_out'], ['0', '1', '2']), 'NIHS_7_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_8_in'], ['0', '1', '2']), 'NIHS_8_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_8_out'], ['0', '1', '2']), 'NIHS_8_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_9_in'], ['0', '1', '2', '3']), 'NIHS_9_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_9_out'], ['0', '1', '2', '3']), 'NIHS_9_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_10_in'], ['0', '1', '2']), 'NIHS_10_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_10_out'], ['0', '1', '2']), 'NIHS_10_out'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_11_in'], ['0', '1', '2']), 'NIHS_11_in'] = np.nan
    df_nihs.loc[out_of_range(df_nihs['NIHS_11_out'], ['0', '1', '2']), 'NIHS_11_out'] = np.nan
    return df_nihs


def clean_rfur():
    fn = 'CASEDRFUR(denormalized).csv'
    read_file_path = gu.get_file_path(fn, under_raw=True)
    df_rfur = pd.read_csv(read_file_path, encoding='utf8')
    rfur_cols = ['VERS_1', 'VERS_3', 'VERS_6', 'VERS_12', 'VEIHD_1', 'VEIHD_3', 'VEIHD_6', 'VEIHD_12']
    df_rfur[rfur_cols] = df_rfur[rfur_cols].replace({'N': '0', 'Y': '1'})
    df_rfur.loc[out_of_range(df_rfur['MRS_1'], ['0', '1', '2', '3', '4', '5', '6']), 'MRS_1'] = np.nan
    df_rfur.loc[out_of_range(df_rfur['MRS_3'], ['0', '1', '2', '3', '4', '5', '6']), 'MRS_3'] = np.nan
    df_rfur.loc[out_of_range(df_rfur['MRS_6'], ['0', '1', '2', '3', '4', '5', '6']), 'MRS_6'] = np.nan
    df_rfur.loc[out_of_range(df_rfur['MRS_12'], ['0', '1', '2', '3', '4', '5', '6']), 'MRS_12'] = np.nan
    return df_rfur


def clean_mcase():
    fn = 'CASEMCASE.csv'
    read_file_path = gu.get_file_path(fn, under_raw=True)
    df_mcase = pd.read_csv(read_file_path, encoding='utf8')
    df_mcase = df_mcase.drop(['IPROTOCOL_ID', 'CNAME_TX', 'CID_ID'], axis=1)
    df_mcase['GENDER_TX'] = df_mcase['GENDER_TX'].replace({'F': '0', 'M': '1'})
    df_mcase['GENDER_TX'] = df_mcase['GENDER_TX'].replace(to_replace=r"[^0-1]", value=np.NaN, regex=True)
    return df_mcase


def create_age(df_case, df_mcase):
    df = pd.merge(df_case, df_mcase, on='ICASE_ID')
    b_day = pd.to_datetime(df['BIRTH_DT'], format='%m/%d/%y', errors='coerce')
    for i, b in b_day.items():
        if b.year > 2000:
            b_day[i] = b_day[i].replace(year=b.year-100)
    onset_day = pd.to_datetime(df['ONSET_DT'], format='%m/%d/%y', errors='coerce')
    AGE = np.floor((onset_day - b_day) / pd.Timedelta(days=365))
    df['onset_age'] = AGE
    df = df.drop(['BIRTH_DT', 'ONSET_DT'], axis=1)
    return df


def convert_features(df):
    tpa_flg = {}
    icd = {}
    cdr_id = {}
    cdl_id = {}
    tccsr_id = {}
    tccsl_id = {}
    mcdr_id = {}
    mcdl_id = {}
    mcdba_id = {}
    mcdri_id = {}
    mcdli_id = {}
    for i, row in df.iterrows():
        tpa_g = row['IVTPAMG_NM']
        tpa_i = row['NIVTPA_ID']
        if not pd.isna(tpa_g):
            tpa_flg[i] = True
        elif not pd.isna(tpa_i):
            tpa_flg[i] = False
        else:
            tpa_flg[i] = np.nan
        # -----------------------------------
        if ~pd.isna(row['ICD_TX']):
            icd_t = str(row['ICD_TX'])
            parent = icd_t.split('.')[0]
            if parent != 'nan':
                icd[i] = parent
            else:
                icd[i] = np.nan
        # -----------------------------------
        if row['CD_ID'] == 0.:
            cdr_id[i] = 0.
            cdl_id[i] = 0.
        else:
            cdr_id[i] = row['CDR_ID']
            cdl_id[i] = row['CDL_ID']
        # -----------------------------------
        if row['TCCS_ID'] == 0.:
            tccsr_id[i] = 0.
            tccsl_id[i] = 0.
        else:
            tccsr_id[i] = row['TCCSR_ID']
            tccsl_id[i] = row['TCCSL_ID']
        # -----------------------------------
        if row['MCD_ID'] == 0.:
            mcdr_id[i] = 0.
            mcdl_id[i] = 0.
            mcdba_id[i] = 0.
            mcdri_id[i] = 0.
            mcdli_id[i] = 0.
        else:
            mcdr_id[i] = row['MCDR_ID']
            mcdl_id[i] = row['MCDL_ID']
            mcdba_id[i] = row['MCDBA_ID']
            mcdri_id[i] = row['MCDRI_ID']
            mcdli_id[i] = row['MCDLI_ID']

    df.insert(loc=df.columns.get_loc("NIVTPA_ID")+1, column='TPA_FL', value=tpa_flg.values())
    df.insert(loc=df.columns.get_loc("ICD_TX")+1, column='ICD_CODE', value=icd.values())
    df = df.drop(['IVTPAMG_NM', 'NIVTPA_ID', 'ICD_TX', 'CD_ID'], axis=1)

    df['CDR_ID'] = cdr_id.values()
    df['CDL_ID'] = cdl_id.values()
    df['TCCSR_ID'] = tccsr_id.values()
    df['TCCSL_ID'] = tccsl_id.values()
    df['MCDR_ID'] = mcdr_id.values()
    df['MCDL_ID'] = mcdl_id.values()
    df['MCDBA_ID'] = mcdba_id.values()
    df['MCDRI_ID'] = mcdri_id.values()
    df['MCDLI_ID'] = mcdli_id.values()
    return df


def make_dummy(df):
    category_features = ['OPC_ID', 'ICD_ID', 'ICD_CODE', 'OFF_ID', 'OFFDT_ID']
    for fe in category_features:
        dummies = pd.get_dummies(df[fe], prefix=fe)
        for i, dummy in enumerate(dummies):
            df.insert(loc=df.columns.get_loc(fe)+i+1, column=dummy, value=dummies[dummy].values)
    df.drop(category_features, axis=1, inplace=True)
    return df
