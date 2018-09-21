from sklearn.manifold import TSNE
import numpy as np
import pandas as pd
from tools import genral_utils
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == '__main__':
    seed = 7
    n_class = 2

    if n_class == 2:
        id_data, x_data, y_data = genral_utils.get_poor_god('wholeset_Jim_nomissing_validated.csv')
        fn = 'reduced_dimension_30_2c_3D'
    else:
        id_data, x_data, y_data = genral_utils.get_individual('wholeset_Jim_nomissing_validated.csv')
        fn = 'reduced_dimension_30_individual_3D'
    # calculation
    # x_data_train = genral_utils.scale(x_data)
    # t_sne = TSNE(n_components=3, perplexity=30).fit_transform(x_data_train)
    # df = pd.DataFrame(t_sne, columns=['x', 'y', 'z'])
    # df['p'] = y_data.values
    # genral_utils.save_dataframe_to_csv(df, fn)

    df = pd.read_csv(genral_utils.get_file_path(fn+'.csv', under_raw=False), encoding='utf8')
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(df.ix[:,0], df.ix[:,1], df.ix[:,2], c=df.ix[:, 3], s = 0.1, cmap=plt.cm.get_cmap("jet", n_class))
    plt.title('t-SNE 3D visualization')
    plt.show()