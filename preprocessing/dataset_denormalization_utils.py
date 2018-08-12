from preprocessing import genral_utils as gu
import csv

def get_hist_value(parents_v, brsi_v):
        # 0-no; 1-yes; 2-down't know; 9-no sibling
        if parents_v == '0' and (brsi_v == '0' or brsi_v == '9'):
            return 0
        elif parents_v == '0' and brsi_v == '1':
            return 1
        elif parents_v == '1' and (brsi_v == '0' or brsi_v == '9'):
            return 2
        elif parents_v == '1' and brsi_v == '1':
            return 3
        else:
            return ""


def de_casedbmrs():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID', 'Feeding', 'Transfers', 'Bathing', 'Toilet_use', 'Grooming',
             'Mobility', 'Stairs', 'Dressing', 'Bowel_control', 'Bladder_control', 'discharged_mrs']
    bid_code = {'1.00': 'Feeding',
                '2.00': 'Transfers',
                '3.00': 'Bathing',
                '4.00': 'Toilet_use',
                '5.00': 'Grooming',
                '6.00': 'Mobility',
                '7.00': 'Stairs',
                '8.00': 'Dressing',
                '9.00': 'Bowel_control',
                '10.00': 'Bladder_control',
                '11.00': 'discharged_mrs'}
    read_file_path = gu.get_file_path('CASEDBMRS.csv')
    with open(read_file_path, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            bid_nm = row['BID_NM']
            botv_nm = row['BOTV_NM']
            if combind_id in patients_dic.keys():
                key = bid_code.get(bid_nm)
                patients_dic.get(combind_id)[key] = botv_nm
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id,
                         'Feeding': '', 'Transfers': '', 'Bathing': '',
                         'Toilet_use': '', 'Grooming': '', 'Mobility': '',
                         'Stairs': '', 'Dressing': '', 'Bowel_control': '',
                         'Bladder_control': '', 'discharged_mrs': ''}
                key = bid_code.get(bid_nm)
                p_dic[key] = botv_nm
                patients_dic[combind_id] = p_dic
    gu.save_file('CASEDBMRS(denormalized)', title, patients_dic)


def de_casedctmr():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID', 'cortical_ACA_ctr', 'cortical_MCA_ctr', 'subcortical_ACA_ctr', 'subcortical_MCA_ctr',
             'PCA_cortex_ctr', 'thalamus_ctr', 'brainstem_ctr', 'cerebellum_ctr', 'Watershed_ctr', 'Hemorrhagic_infarct_ctr',
             'Old_stroke_ctci', 'cortical_ACA_ctl', 'cortical_MCA_ctl', 'subcortical_ACA_ctl', 'subcortical_MCA_ctl',
             'PCA_cortex_ctl', 'thalamus_ctl', 'brainstem_ctl', 'cerebellum_ctl', 'Watershed_ctl', 'Hemorrhagic_infarct_ctl',
             'Old_stroke_ctch', 'cortical_ACA_mrir', 'cortical_MCA_mrir', 'subcortical_ACA_mrir', 'subcortical_MCA_mrir',
             'PCA_cortex_mrir', 'thalamus_mrir', 'brainstem_mrir', 'cerebellum_mrir', 'Watershed_mrir', 'Hemorrhagic_infarct_mrir',
             'Old_stroke_mrici', 'cortical_ACA_mril', 'cortical_MCA_mril', 'subcortical_ACA_mril', 'subcortical_MCA_mril',
             'PCA_cortex_mril', 'thalamus_mril', 'brainstem_mril', 'cerebellum_mril', 'Watershed_mril', 'Hemorrhagic_infarct_mril',
             'Old_stroke_mrich']
    cm_code = {
                '1': 'cortical_ACA',
                '2': 'cortical_MCA',
                '3': 'subcortical_ACA',
                '4': 'subcortical_MCA',
                '5': 'PCA_cortex',
                '6': 'thalamus',
                '7': 'brainstem',
                '8': 'cerebellum',
                '9': 'Watershed',
                '10': 'Hemorrhagic_infarct',
                '11': 'Old_stroke'}

    read_file_path = gu.get_file_path('CASEDCTMR.csv')
    with open(read_file_path, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            ctmriid_nm = row['CTMRIID_NM']
            ctright_fl = row['CTRIGHT_FL']
            ctleft_fl = row['CTLEFT_FL']
            mriright_fl = row['MRIRIGHT_FL']
            mrileft_fl = row['MRILEFT_FL']
            if combind_id in patients_dic.keys():
                key = cm_code.get(ctmriid_nm)
                if ctmriid_nm != '11':
                    patients_dic.get(combind_id)[key + '_ctr'] = ctright_fl
                    patients_dic.get(combind_id)[key + '_ctl'] = ctleft_fl
                    patients_dic.get(combind_id)[key + '_mrir'] = mriright_fl
                    patients_dic.get(combind_id)[key + '_mril'] = mrileft_fl
                else:
                    patients_dic.get(combind_id)[key + '_ctci'] = ctright_fl
                    patients_dic.get(combind_id)[key + '_ctch'] = ctleft_fl
                    patients_dic.get(combind_id)[key + '_mrici'] = mriright_fl
                    patients_dic.get(combind_id)[key + '_mrich'] = mrileft_fl
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id,
                         'cortical_ACA_ctr': '', 'cortical_MCA_ctr': '', 'subcortical_ACA_ctr': '',
                         'subcortical_MCA_ctr': '', 'PCA_cortex_ctr': '',
                         'thalamus_ctr': '', 'brainstem_ctr': '', 'cerebellum_ctr': '', 'Watershed_ctr': '',
                         'Hemorrhagic_infarct_ctr': '', 'Old_stroke_ctci': '',
                         'cortical_ACA_ctl': '', 'cortical_MCA_ctl': '', 'subcortical_ACA_ctl': '',
                         'subcortical_MCA_ctl': '', 'PCA_cortex_ctl': '',
                         'thalamus_ctl': '', 'brainstem_ctl': '', 'cerebellum_ctl': '', 'Watershed_ctl': '',
                         'Hemorrhagic_infarct_ctl': '', 'Old_stroke_ctch': '',
                         'cortical_ACA_mrir': '', 'cortical_MCA_mrir': '', 'subcortical_ACA_mrir': '',
                         'subcortical_MCA_mrir': '', 'PCA_cortex_mrir': '',
                         'thalamus_mrir': '', 'brainstem_mrir': '', 'cerebellum_mrir': '', 'Watershed_mrir': '',
                         'Hemorrhagic_infarct_mrir': '', 'Old_stroke_mrici': '',
                         'cortical_ACA_mril': '', 'cortical_MCA_mril': '', 'subcortical_ACA_mril': '',
                         'subcortical_MCA_mril': '', 'PCA_cortex_mril': '',
                         'thalamus_mril': '', 'brainstem_mril': '', 'cerebellum_mril': '', 'Watershed_mril': '',
                         'Hemorrhagic_infarct_mril': '', 'Old_stroke_mrich': ''
                         }
                key = cm_code.get(ctmriid_nm)
                if ctmriid_nm != '11':
                    p_dic[key + '_ctr'] = ctright_fl
                    p_dic[key + '_ctl'] = ctleft_fl
                    p_dic[key + '_mrir'] = mriright_fl
                    p_dic[key + '_mril'] = mrileft_fl
                else:
                    p_dic[key + '_ctci'] = ctright_fl
                    p_dic[key + '_ctch'] = ctleft_fl
                    p_dic[key + '_mrici'] = mriright_fl
                    p_dic[key + '_mrich'] = mrileft_fl
                patients_dic[combind_id] = p_dic
    gu.save_file('CASEDCTMR(denormalized)', title, patients_dic)


def de_casedfahi():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID', 'FH_HBP', 'FH_DB', 'FH_HD', 'FH_ST']
    diseace_code = {
                    '1': 'FH_HBP',
                    '2': 'FH_DB',
                    '3': 'FH_HD',
                    '4': 'FH_ST'}
    read_file_path = gu.get_file_path('CASEDFAHI.csv')
    with open(read_file_path, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            fahiid_id = row['FAHIID_ID']
            parents_v = row['PARENTS_CD']
            brsi_v = row['BRSI_CD']
            if combind_id in patients_dic.keys():
                key = diseace_code.get(fahiid_id)
                patients_dic.get(combind_id)[key] = get_hist_value(parents_v, brsi_v)
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id, 'FH_HBP': '', 'FH_DB': '', 'FH_HD': '',
                         'FH_ST': ''}
                key = diseace_code.get(fahiid_id)
                p_dic[key] = get_hist_value(parents_v, brsi_v)
                patients_dic[combind_id] = p_dic
    gu.save_file('CASEDFAHI(denormalized)', title, patients_dic)


def de_casedrfur():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID',
             'VERS_1', 'VERS_3', 'VERS_6', 'VERS_12',
             'VEIHD_1', 'VEIHD_3', 'VEIHD_6', 'VEIHD_12',
             'MRS_1', 'MRS_3', 'MRS_6', 'MRS_12']
    read_file_path = gu.get_file_path('CASEDRFUR-2016-05-23.csv')
    with open(read_file_path, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            rfur_nm = row['RFUR_NM']
            vers_fl = row['VERS_FL']
            veihd_fl = row['VEIHD_FL']
            mrs_tx = row['MRS_TX']
            if combind_id in patients_dic.keys():
                patients_dic.get(combind_id)['VERS_' + rfur_nm] = vers_fl
                patients_dic.get(combind_id)['VEIHD_' + rfur_nm] = veihd_fl
                patients_dic.get(combind_id)['MRS_' + rfur_nm] = mrs_tx
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id, 'VERS_1': '',
                         'VERS_3': '', 'VERS_6': '', 'VERS_12': '','VEIHD_1': '',
                         'VEIHD_3': '', 'VEIHD_6': '', 'VEIHD_12': '',
                         'MRS_1': '', 'MRS_3': '', 'MRS_6': '', 'MRS_12': ''}
                p_dic['VERS_' + rfur_nm] = vers_fl
                p_dic['VEIHD_' + rfur_nm] = veihd_fl
                p_dic['MRS_' + rfur_nm] = mrs_tx
                patients_dic[combind_id] = p_dic
    gu.save_file('CASEDRFUR(denormalized)', title, patients_dic)


def de_casednihs():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID',
             'NIHS_1a_in', 'NIHS_1b_in', 'NIHS_1c_in', 'NIHS_2_in', 'NIHS_3_in', 'NIHS_4_in', 'NIHS_5aL_in',
             'NIHS_5bR_in', 'NIHS_6aL_in', 'NIHS_6bR_in', 'NIHS_7_in', 'NIHS_8_in', 'NIHS_9_in', 'NIHS_10_in',
             'NIHS_11_in', 'NIHS_1a_out', 'NIHS_1b_out', 'NIHS_1c_out', 'NIHS_2_out', 'NIHS_3_out', 'NIHS_4_out',
             'NIHS_5aL_out', 'NIHS_5bR_out', 'NIHS_6aL_out', 'NIHS_6bR_out', 'NIHS_7_out', 'NIHS_8_out', 'NIHS_9_out',
             'NIHS_10_out', 'NIHS_11_out']
    test_code = {
        '1.10': 'NIHS_1a',
        '1.20': 'NIHS_1b',
        '1.30': 'NIHS_1c',
        '2.00': 'NIHS_2',
        '3.00': 'NIHS_3',
        '4.00': 'NIHS_4',
        '5.10': 'NIHS_5aL',
        '5.20': 'NIHS_5bR',
        '6.10': 'NIHS_6aL',
        '6.20': 'NIHS_6bR',
        '7.00': 'NIHS_7',
        '8.00': 'NIHS_8',
        '9.00': 'NIHS_9',
        '10.00': 'NIHS_10',
        '11.00': 'NIHS_11'}
    read_file_path = gu.get_file_path('CASEDNIHS.csv')
    with open(read_file_path, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            nid_nm = row['NID_NM']
            ninv_nm = row['NINV_NM']
            notv_nm = row['NOTV_NM']
            if combind_id in patients_dic.keys():
                key = test_code.get(nid_nm)
                patients_dic.get(combind_id)[key + '_in'] = ninv_nm
                patients_dic.get(combind_id)[key + '_out'] = notv_nm
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id,
                         'NIHS_1a_in': '', 'NIHS_1b_in': '', 'NIHS_1c_in': '', 'NIHS_2_in': '', 'NIHS_3_in': '',
                         'NIHS_4_in': '', 'NIHS_5aL_in': '', 'NIHS_5bR_in': '', 'NIHS_6aL_in': '', 'NIHS_6bR_in': '',
                         'NIHS_7_in': '', 'NIHS_8_in': '', 'NIHS_9_in': '', 'NIHS_10_in': '', 'NIHS_11_in': '',
                         'NIHS_1a_out': '', 'NIHS_1b_out': '', 'NIHS_1c_out': '', 'NIHS_2_out': '', 'NIHS_3_out': '',
                         'NIHS_4_out': '', 'NIHS_5aL_out': '', 'NIHS_5bR_out': '', 'NIHS_6aL_out': '',
                         'NIHS_6bR_out': '', 'NIHS_7_out': '', 'NIHS_8_out': '', 'NIHS_9_out': '', 'NIHS_10_out': '',
                         'NIHS_11_out': ''
                         }
                key = test_code.get(nid_nm)
                p_dic[key + '_in'] = ninv_nm
                p_dic[key + '_out'] = notv_nm
                patients_dic[combind_id] = p_dic
    gu.save_file('CASEDNIHS(denormalized)', title, patients_dic)
