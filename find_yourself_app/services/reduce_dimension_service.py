from sklearn.decomposition import PCA


def reduce_dimen(X, algorithm='PCA', n_components=1):
    """Reduce the dimensionality of the 55 AISNPs
    :param X: One-hot encoded 1kG 55 AISNPs.
    :type X: array
    :param algorithm: The type of dimensionality reduction to perform.
        One of {PCA, UMAP, TSNE}
    :type algorithm: str
    :param n_components: The number of components to return in X_red
    :type n_components: int
    :returns: The transformed X[m, n] array, reduced to X[m, n_components] by algorithm.
    """
    if algorithm == 'PCA':
        X_red = PCA(n_components=n_components).fit_transform(X)
    return X_red
