import pandas as pd
import os

data = pd.read_csv(os.path.join('..', 'data_source', 'raw', 'CASEDCTMR.csv'))
a = data[data.CTMRIID_NM > 11.0]

print('done')