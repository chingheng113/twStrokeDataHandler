from sklearn.manifold import TSNE
import numpy as np
import pandas as pd
from tools import genral_utils
import matplotlib.pyplot as plt


if __name__ == '__main__':
    seed = 7
    n_class = 2

    if n_class == 2:
        id_data, x_data, y_data = genral_utils.get_poor_god('wholeset_Jim_nomissing_validated.csv')
        fn = 'reduced_dimension_2c'
    else:
        id_data, x_data, y_data = genral_utils.get_individual('wholeset_Jim_nomissing_validated.csv')
        fn = 'reduced_dimension_individual'
    # calculation
    x_data_train = genral_utils.scale(x_data)
    t_sne = TSNE(n_components=2, perplexity=50).fit_transform(x_data_train)
    df = pd.DataFrame(t_sne, columns=['x', 'y'])
    df['p'] = y_data.values
    genral_utils.save_dataframe_to_csv(df, fn)

    df = pd.read_csv(genral_utils.get_file_path(fn+'.csv', under_raw=False), encoding='utf8')
    plt.figure()
    plt.scatter(df.ix[:,0], df.ix[:,1], c=df.ix[:, 2], s=0.1, cmap=plt.cm.get_cmap("jet", n_class))
    plt.colorbar(ticks=range(n_class))
    plt.show()