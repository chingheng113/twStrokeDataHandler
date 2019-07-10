from tools import genral_utils as gu
import csv


def de_casedbmrs():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID', 'GUID_TSYM', 'Feeding', 'Transfers', 'Bathing', 'Toilet_use', 'Grooming',
             'Mobility', 'Stairs', 'Dressing', 'Bowel_control', 'Bladder_control', 'discharged_mrs']
    bid_code = {'1': 'Feeding',
                '2': 'Transfers',
                '3': 'Bathing',
                '4': 'Toilet_use',
                '5': 'Grooming',
                '6': 'Mobility',
                '7': 'Stairs',
                '8': 'Dressing',
                '9': 'Bowel_control',
                '10': 'Bladder_control',
                '11': 'discharged_mrs'}
    read_file_path = gu.get_file_path('CASEDBMRS_1.csv', under_raw=True)
    with open(read_file_path, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            guid = row['GUID_TSYM']
            bid_nm = row['BID_NM']
            botv_nm = row['BOTV_NM']
            if combind_id in patients_dic.keys():
                key = bid_code.get(bid_nm)
                patients_dic.get(combind_id)[key] = botv_nm
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id, 'GUID_TSYM': guid,
                         'Feeding': '', 'Transfers': '', 'Bathing': '',
                         'Toilet_use': '', 'Grooming': '', 'Mobility': '',
                         'Stairs': '', 'Dressing': '', 'Bowel_control': '',
                         'Bladder_control': '', 'discharged_mrs': ''}
                key = bid_code.get(bid_nm)
                p_dic[key] = botv_nm
                patients_dic[combind_id] = p_dic
    gu.save_array_to_csv('CASEDBMRS_1(denormalized)', title, patients_dic, under_raw=True)


def de_casedctmr():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID', 'GUID_TSYM', 'cortical_ACA_ctr', 'cortical_MCA_ctr', 'subcortical_ACA_ctr', 'subcortical_MCA_ctr',
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

    read_file_path = gu.get_file_path('CASEDCTMR_1.csv', under_raw=True)
    with open(read_file_path, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            guid = row['GUID_TSYM']
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
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id, 'GUID_TSYM': guid,
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
    gu.save_array_to_csv('CASEDCTMR_1(denormalized)', title, patients_dic, under_raw=True)


def de_casedfahi():
    patients_dic_1 = {}
    patients_dic_2 = {}
    title_1 = ['ICASE_ID', 'IDCASE_ID', 'GUID_TSYM', 'FAHIID_PARENTS_1', 'FAHIID_PARENTS_2', 'FAHIID_PARENTS_3', 'FAHIID_PARENTS_4']
    diseace_code = {
                    '1': 'FAHIID_PARENTS_1',
                    '2': 'FAHIID_PARENTS_2',
                    '3': 'FAHIID_PARENTS_3',
                    '4': 'FAHIID_PARENTS_4'}
    read_file_path = gu.get_file_path('CASEDFAHI_1.csv', under_raw=True)
    with open(read_file_path, 'r', encoding='utf8', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            fahiid_id = row['FAHIID_ID']
            parents_v = row['PARENTS_CD']
            guid = row['GUID_TSYM']
            if combind_id in patients_dic_1.keys():
                key = diseace_code.get(fahiid_id)
                patients_dic_1.get(combind_id)[key] = parents_v
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id, 'GUID_TSYM': guid,
                         'FAHIID_PARENTS_1': '', 'FAHIID_PARENTS_2': '', 'FAHIID_PARENTS_3': '', 'FAHIID_PARENTS_4': ''}
                key = diseace_code.get(fahiid_id)
                p_dic[key] = parents_v
                patients_dic_1[combind_id] = p_dic
    # ==
    title_2 = ['ICASE_ID', 'IDCASE_ID', 'GUID_TSYM', 'FAHIID_BRSI_1', 'FAHIID_BRSI_2', 'FAHIID_BRSI_3', 'FAHIID_BRSI_4']
    diseace_code = {
        '1': 'FAHIID_BRSI_1',
        '2': 'FAHIID_BRSI_2',
        '3': 'FAHIID_BRSI_3',
        '4': 'FAHIID_BRSI_4'}
    read_file_path = gu.get_file_path('CASEDFAHI_1.csv', under_raw=True)
    with open(read_file_path, 'r', encoding='utf8', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            fahiid_id = row['FAHIID_ID']
            brsi_v = row['BRSI_CD']
            guid = row['GUID_TSYM']
            if combind_id in patients_dic_2.keys():
                key = diseace_code.get(fahiid_id)
                patients_dic_2.get(combind_id)[key] = brsi_v
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id, 'GUID_TSYM': guid,
                         'FAHIID_BRSI_1': '', 'FAHIID_BRSI_2': '', 'FAHIID_BRSI_3': '', 'FAHIID_BRSI_4': ''}
                key = diseace_code.get(fahiid_id)
                p_dic[key] = brsi_v
                patients_dic_2[combind_id] = p_dic

    title = ['ICASE_ID', 'IDCASE_ID', 'GUID_TSYM', 'FAHIID_PARENTS_1', 'FAHIID_PARENTS_2', 'FAHIID_PARENTS_3',
               'FAHIID_PARENTS_4', 'FAHIID_BRSI_1', 'FAHIID_BRSI_2', 'FAHIID_BRSI_3', 'FAHIID_BRSI_4']
    patients_dic = {}
    if len(patients_dic_1) == len(patients_dic_2):
        for k in patients_dic_1.keys():
            dic_1 = patients_dic_1[k]
            dic_2 = patients_dic_2[k]
            patients_dic[k] = {**dic_1, **dic_2}
    gu.save_array_to_csv('CASEDFAHI_1(denormalized)', title, patients_dic, under_raw=True)


def de_casedrfur():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID', 'GUID_TSYM',
              'FSTATUS_ID_1', 'RFUR_DT_1', 'LOCATION_ID_1', 'TORG_ID_1', 'FLU_ID_1', 'FLUORG_ID_1', 'FLUORG_TX_1', 'FLURESULT_TX_1', 'DEATH_DT_1', 'DEATH_ID_1', 'DEATHSK_ID_1', 'DEATHO_TX_1', 'VE_ID_1', 'VERS_FL_1', 'VERSCICH_ID_1', 'VERS_DT_1', 'VERSORG_ID_1', 'VEIHD_FL_1', 'VEIHD_ID_1', 'VEIHD_DT_1', 'VEIHDORG_ID_1', 'MRS_TX_1', 'TORG_TX_1', 'VERSORG_TX_1', 'VEIHDORG_TX_1',
              'FSTATUS_ID_3', 'RFUR_DT_3', 'LOCATION_ID_3', 'TORG_ID_3', 'FLU_ID_3', 'FLUORG_ID_3', 'FLUORG_TX_3', 'FLURESULT_TX_3', 'DEATH_DT_3', 'DEATH_ID_3', 'DEATHSK_ID_3', 'DEATHO_TX_3', 'VE_ID_3', 'VERS_FL_3', 'VERSCICH_ID_3', 'VERS_DT_3', 'VERSORG_ID_3', 'VEIHD_FL_3', 'VEIHD_ID_3', 'VEIHD_DT_3', 'VEIHDORG_ID_3', 'MRS_TX_3', 'TORG_TX_3', 'VERSORG_TX_3', 'VEIHDORG_TX_3',
             'FSTATUS_ID_6', 'RFUR_DT_6', 'LOCATION_ID_6', 'TORG_ID_6', 'FLU_ID_6', 'FLUORG_ID_6', 'FLUORG_TX_6', 'FLURESULT_TX_6', 'DEATH_DT_6', 'DEATH_ID_6', 'DEATHSK_ID_6', 'DEATHO_TX_6', 'VE_ID_6', 'VERS_FL_6', 'VERSCICH_ID_6', 'VERS_DT_6', 'VERSORG_ID_6', 'VEIHD_FL_6', 'VEIHD_ID_6', 'VEIHD_DT_6', 'VEIHDORG_ID_6', 'MRS_TX_6', 'TORG_TX_6', 'VERSORG_TX_6', 'VEIHDORG_TX_6',
             'FSTATUS_ID_12', 'RFUR_DT_12', 'LOCATION_ID_12', 'TORG_ID_12', 'FLU_ID_12', 'FLUORG_ID_12', 'FLUORG_TX_12', 'FLURESULT_TX_12', 'DEATH_DT_12', 'DEATH_ID_12', 'DEATHSK_ID_12', 'DEATHO_TX_12', 'VE_ID_12', 'VERS_FL_12', 'VERSCICH_ID_12', 'VERS_DT_12', 'VERSORG_ID_12', 'VEIHD_FL_12', 'VEIHD_ID_12', 'VEIHD_DT_12', 'VEIHDORG_ID_12', 'MRS_TX_12', 'TORG_TX_12', 'VERSORG_TX_12', 'VEIHDORG_TX_12'
             ]
    read_file_path = gu.get_file_path('CASEDRFUR_1.csv', under_raw=True)
    with open(read_file_path, 'r', encoding='utf8', errors='replace') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            guid = row['GUID_TSYM']
            rfur_nm = row['RFUR_NM']
            fstatus_id = row['FSTATUS_ID']
            rfur_dt = row['RFUR_DT']
            location_id = row['LOCATION_ID']
            torg_id = row['TORG_ID']
            flu_id = row['FLU_ID']
            fluorg_id = row['FLUORG_ID']
            fluorg_tx = row['FLUORG_TX']
            fluresult_tx = row['FLURESULT_TX']
            death_dt = row['DEATH_DT']
            death_id = row['DEATH_ID']
            deathsk_id = row['DEATHSK_ID']
            deatho_tx = row['DEATHO_TX']
            ve_id = row['VE_ID']
            vers_fl = row['VERS_FL']
            verscich_id = row['VERSCICH_ID']
            vers_dt = row['VERS_DT']
            versorg_id = row['VERSORG_ID']
            veihd_fl = row['VEIHD_FL']
            veihd_id = row['VEIHD_ID']
            veihd_dt = row['VEIHD_DT']
            veihdorg_id = row['VEIHDORG_ID']
            mrs_tx = row['MRS_TX']
            torg_tx = row['TORG_TX']
            versorg_tx = row['VERSORG_TX']
            veihdorg_tx = row['VEIHDORG_TX']

            if combind_id in patients_dic.keys():
                patients_dic.get(combind_id)['FSTATUS_ID_' + rfur_nm] = fstatus_id
                patients_dic.get(combind_id)['RFUR_DT_' + rfur_nm] = rfur_dt
                patients_dic.get(combind_id)['LOCATION_ID_' + rfur_nm] = location_id
                patients_dic.get(combind_id)['TORG_ID_' + rfur_nm] = torg_id
                patients_dic.get(combind_id)['FLU_ID_' + rfur_nm] = flu_id
                patients_dic.get(combind_id)['FLUORG_ID_' + rfur_nm] = fluorg_id
                patients_dic.get(combind_id)['FLUORG_TX_' + rfur_nm] = fluorg_tx
                patients_dic.get(combind_id)['FLURESULT_TX_' + rfur_nm] = fluresult_tx
                patients_dic.get(combind_id)['DEATH_DT_' + rfur_nm] = death_dt
                patients_dic.get(combind_id)['DEATH_ID_' + rfur_nm] = death_id
                patients_dic.get(combind_id)['DEATHSK_ID_' + rfur_nm] = deathsk_id
                patients_dic.get(combind_id)['DEATHO_TX_' + rfur_nm] = deatho_tx
                patients_dic.get(combind_id)['VE_ID_' + rfur_nm] = ve_id
                patients_dic.get(combind_id)['VERS_FL_' + rfur_nm] = vers_fl
                patients_dic.get(combind_id)['VERSCICH_ID_' + rfur_nm] = verscich_id
                patients_dic.get(combind_id)['VERS_DT_' + rfur_nm] = vers_dt
                patients_dic.get(combind_id)['VERSORG_ID_' + rfur_nm] = versorg_id
                patients_dic.get(combind_id)['VEIHD_FL_' + rfur_nm] = veihd_fl
                patients_dic.get(combind_id)['VEIHD_ID_' + rfur_nm] = veihd_id
                patients_dic.get(combind_id)['VEIHD_DT_' + rfur_nm] = veihd_dt
                patients_dic.get(combind_id)['VEIHDORG_ID_' + rfur_nm] = veihdorg_id
                patients_dic.get(combind_id)['MRS_TX_' + rfur_nm] = mrs_tx
                patients_dic.get(combind_id)['TORG_TX_' + rfur_nm] = torg_tx
                patients_dic.get(combind_id)['VERSORG_TX_' + rfur_nm] = versorg_tx
                patients_dic.get(combind_id)['VEIHDORG_TX_' + rfur_nm] = veihdorg_tx
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id, 'GUID_TSYM': guid,
                         'FSTATUS_ID_1': '', 'RFUR_DT_1': '', 'LOCATION_ID_1': '', 'TORG_ID_1': '', 'FLU_ID_1': '', 'FLUORG_ID_1': '', 'FLUORG_TX_1': '', 'FLURESULT_TX_1': '', 'DEATH_DT_1': '', 'DEATH_ID_1': '', 'DEATHSK_ID_1': '', 'DEATHO_TX_1': '', 'VE_ID_1': '', 'VERS_FL_1': '', 'VERSCICH_ID_1': '', 'VERS_DT_1': '', 'VERSORG_ID_1': '', 'VEIHD_FL_1': '', 'VEIHD_ID_1': '', 'VEIHD_DT_1': '', 'VEIHDORG_ID_1': '', 'MRS_TX_1': '', 'TORG_TX_1': '', 'VERSORG_TX_1': '', 'VEIHDORG_TX_1': '',
                         'FSTATUS_ID_3': '', 'RFUR_DT_3': '', 'LOCATION_ID_3': '', 'TORG_ID_3': '', 'FLU_ID_3': '', 'FLUORG_ID_3': '', 'FLUORG_TX_3': '', 'FLURESULT_TX_3': '', 'DEATH_DT_3': '', 'DEATH_ID_3': '', 'DEATHSK_ID_3': '', 'DEATHO_TX_3': '', 'VE_ID_3': '', 'VERS_FL_3': '', 'VERSCICH_ID_3': '', 'VERS_DT_3': '', 'VERSORG_ID_3': '', 'VEIHD_FL_3': '', 'VEIHD_ID_3': '', 'VEIHD_DT_3': '', 'VEIHDORG_ID_3': '', 'MRS_TX_3': '', 'TORG_TX_3': '', 'VERSORG_TX_3': '', 'VEIHDORG_TX_3': '',
                         'FSTATUS_ID_6': '', 'RFUR_DT_6': '', 'LOCATION_ID_6': '', 'TORG_ID_6': '', 'FLU_ID_6': '', 'FLUORG_ID_6': '', 'FLUORG_TX_6': '', 'FLURESULT_TX_6': '', 'DEATH_DT_6': '', 'DEATH_ID_6': '', 'DEATHSK_ID_6': '', 'DEATHO_TX_6': '', 'VE_ID_6': '', 'VERS_FL_6': '', 'VERSCICH_ID_6': '', 'VERS_DT_6': '', 'VERSORG_ID_6': '', 'VEIHD_FL_6': '', 'VEIHD_ID_6': '', 'VEIHD_DT_6': '', 'VEIHDORG_ID_6': '', 'MRS_TX_6': '', 'TORG_TX_6': '', 'VERSORG_TX_6': '', 'VEIHDORG_TX_6': '',
                         'FSTATUS_ID_12': '', 'RFUR_DT_12': '', 'LOCATION_ID_12': '', 'TORG_ID_12': '', 'FLU_ID_12': '', 'FLUORG_ID_12': '', 'FLUORG_TX_12': '', 'FLURESULT_TX_12': '', 'DEATH_DT_12': '', 'DEATH_ID_12': '', 'DEATHSK_ID_12': '', 'DEATHO_TX_12': '', 'VE_ID_12': '', 'VERS_FL_12': '', 'VERSCICH_ID_12': '', 'VERS_DT_12': '', 'VERSORG_ID_12': '', 'VEIHD_FL_12': '', 'VEIHD_ID_12': '', 'VEIHD_DT_12': '', 'VEIHDORG_ID_12': '', 'MRS_TX_12': '', 'TORG_TX_12': '', 'VERSORG_TX_12': '', 'VEIHDORG_TX_12': ''
                         }
                p_dic['FSTATUS_ID_' + rfur_nm] = fstatus_id
                p_dic['RFUR_DT_' + rfur_nm] = rfur_dt
                p_dic['LOCATION_ID_' + rfur_nm] = location_id
                p_dic['TORG_ID_' + rfur_nm] = torg_id
                p_dic['FLU_ID_' + rfur_nm] = flu_id
                p_dic['FLUORG_ID_' + rfur_nm] = fluorg_id
                p_dic['FLUORG_TX_' + rfur_nm] = fluorg_tx
                p_dic['FLURESULT_TX_' + rfur_nm] = fluresult_tx
                p_dic['DEATH_DT_' + rfur_nm] = death_dt
                p_dic['DEATH_ID_' + rfur_nm] = death_id
                p_dic['DEATHSK_ID_' + rfur_nm] = deathsk_id
                p_dic['DEATHO_TX_' + rfur_nm] = deatho_tx
                p_dic['VE_ID_' + rfur_nm] = ve_id
                p_dic['VERS_FL_' + rfur_nm] = vers_fl
                p_dic['VERSCICH_ID_' + rfur_nm] = verscich_id
                p_dic['VERS_DT_' + rfur_nm] = vers_dt
                p_dic['VERSORG_ID_' + rfur_nm] = versorg_id
                p_dic['VEIHD_FL_' + rfur_nm] = veihd_fl
                p_dic['VEIHD_ID_' + rfur_nm] = veihd_id
                p_dic['VEIHD_DT_' + rfur_nm] = veihd_dt
                p_dic['VEIHDORG_ID_' + rfur_nm] = veihdorg_id
                p_dic['MRS_TX_' + rfur_nm] = mrs_tx
                p_dic['TORG_TX_' + rfur_nm] = torg_tx
                p_dic['VERSORG_TX_' + rfur_nm] = versorg_tx
                p_dic['VEIHDORG_TX_' + rfur_nm] = veihdorg_tx
                patients_dic[combind_id] = p_dic
    gu.save_array_to_csv('CASEDRFUR_1(denormalized)', title, patients_dic, under_raw=True)


def de_casednihs():
    patients_dic = {}
    title = ['ICASE_ID', 'IDCASE_ID', 'GUID_TSYM',
             'NIHS_1a_in', 'NIHS_1b_in', 'NIHS_1c_in', 'NIHS_2_in', 'NIHS_3_in', 'NIHS_4_in', 'NIHS_5aL_in',
             'NIHS_5bR_in', 'NIHS_6aL_in', 'NIHS_6bR_in', 'NIHS_7_in', 'NIHS_8_in', 'NIHS_9_in', 'NIHS_10_in',
             'NIHS_11_in', 'NIHS_1a_out', 'NIHS_1b_out', 'NIHS_1c_out', 'NIHS_2_out', 'NIHS_3_out', 'NIHS_4_out',
             'NIHS_5aL_out', 'NIHS_5bR_out', 'NIHS_6aL_out', 'NIHS_6bR_out', 'NIHS_7_out', 'NIHS_8_out', 'NIHS_9_out',
             'NIHS_10_out', 'NIHS_11_out']
    test_code = {
        '1.1': 'NIHS_1a',
        '1.2': 'NIHS_1b',
        '1.3': 'NIHS_1c',
        '2': 'NIHS_2',
        '3': 'NIHS_3',
        '4': 'NIHS_4',
        '5.1': 'NIHS_5aL',
        '5.2': 'NIHS_5bR',
        '6.1': 'NIHS_6aL',
        '6.2': 'NIHS_6bR',
        '7': 'NIHS_7',
        '8': 'NIHS_8',
        '9': 'NIHS_9',
        '10': 'NIHS_10',
        '11': 'NIHS_11'}
    read_file_path = gu.get_file_path('CASEDNIHS_1.csv', under_raw=True)
    with open(read_file_path, 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            icase_id = row['ICASE_ID']
            idcase_id = row['IDCASE_ID']
            combind_id = icase_id + idcase_id
            guid = row['GUID_TSYM']
            nid_nm = row['NID_NM']
            ninv_nm = row['NINV_NM']
            notv_nm = row['NOTV_NM']
            if combind_id in patients_dic.keys():
                key = test_code.get(nid_nm)
                patients_dic.get(combind_id)[key + '_in'] = ninv_nm
                patients_dic.get(combind_id)[key + '_out'] = notv_nm
            else:
                # initial a patient's dictionary
                p_dic = {'ICASE_ID': icase_id, 'IDCASE_ID': idcase_id, 'GUID_TSYM': guid,
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
    gu.save_array_to_csv('CASEDNIHS_1(denormalized)', title, patients_dic, under_raw=True)


if __name__ == '__main__':
    de_casedrfur()
