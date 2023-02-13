from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder


def get_one_hot_encoding(df):
    ncols = len(df.columns)
    ohe = OneHotEncoder(categories=[range(4)] * ncols, sparse=False)
    return ohe.fit_transform(df.values)
def reduce_dimension_service(df, algorithm='PCA', n_components=1):
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
    df_encoded = get_one_hot_encoding(df)
    if algorithm == 'PCA':
        transformed_df = PCA(n_components=n_components).fit_transform(df_encoded)
    return transformed_df
