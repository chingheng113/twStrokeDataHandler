from cleaning import dataset_denormalization_utils as deUtil


if __name__ == '__main__':
    # Dataset structure denormalization
    deUtil.de_casedbmrs()
    deUtil.de_casedctmr()
    deUtil.de_casedfahi()
    deUtil.de_casedrfur()
    print("Done")