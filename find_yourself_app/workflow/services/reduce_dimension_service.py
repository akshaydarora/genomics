import pandas as pd
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder
import warnings
warnings.filterwarnings(action="ignore",category=DeprecationWarning)

def get_one_hot_encoding(df):
    ncols = len(df.columns)
    ohe = OneHotEncoder(categories=[range(4)] * ncols, sparse=False)
    return ohe.fit_transform(df.values)


def reduce_dimension_service(genome_samples,pivot_df, algorithm='PCA', n_components=1):
    """Reduce the dimensionality of the 55 AISNPs
    :param genome_fact_pivot:
    :param X: One-hot encoded 1kG 55 AISNPs.
    :type X: array
    :param algorithm: The type of dimensionality reduction to perform.
        One of {PCA, UMAP, TSNE}
    :type algorithm: str
    :param n_components: The number of components to return in X_red
    :type n_components: int
    """
    color_lookup={"EAS":"#40E0D0","AFR":"#722F37","AMR":"#CC7722","EUR":"#1F51FF","SAS":"#CD7F32"}
    genome_dir="genome_data"
    df_encoded = get_one_hot_encoding(pivot_df)
    if algorithm == 'PCA':
        transformed = PCA(n_components=n_components).fit_transform(df_encoded)
    transformed_df=pd.DataFrame(transformed)
    transformed_df.columns=["x","y","z"]
    pca_df=pd.concat([transformed_df,genome_samples],axis=1)
    pca_df["color"]=pca_df["super_pop"].map(color_lookup)
    # print(pca_df.head())
    # print(pca_df.isnull().sum())
    if not os.path.exists(genome_dir):
      os.makedirs(genome_dir)
    pca_df.to_csv(os.path.join(genome_dir,"dim_reduce.csv"),index=False)
    return pca_df
