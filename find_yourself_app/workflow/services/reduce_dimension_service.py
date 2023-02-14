import pandas as pd
import os
from sklearn.decomposition import PCA
from .utils import load_model,save_model
import warnings
warnings.filterwarnings(action="ignore",category=DeprecationWarning)


def reduce_dimension_service(df,ohe, algorithm='PCA', n_components=1):
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
    color_lookup={"EAS":"#FFBF00","AFR":"#40E0D0","AMR":"#DE3163","EUR":"#6495ED","SAS":"#AF7AC5"}
    super_pop_lookup={"EAS":"EAST ASIA","AFR":"AFRICA","AMR":"AMERICA","EUR":"EUROPE","SAS":"SOUTH ASIA"}
    df_encoded = ohe
    if algorithm == 'PCA':
        pca_mod = PCA(n_components=n_components).fit(df_encoded)
        save_model(pca_mod,"pca","pca")
        transformed = pca_mod.transform(df_encoded)
    transformed_df=pd.DataFrame(transformed)
    transformed_df.columns=["x","y","z"]
    pca_df=pd.concat([transformed_df,df],axis=1)
    pca_df["color"]=pca_df["super_pop"].map(color_lookup)
    pca_df["pop_zone"]=pca_df["super_pop"].map(super_pop_lookup)
    return pca_df

def reduce_dimension_service_test(ohe,algorithm,genome_test):
    color_lookup={"EAS":"#FFBF00","AFR":"#40E0D0","AMR":"#DE3163","EUR":"#6495ED","SAS":"#AF7AC5"}
    super_pop_lookup={"EAS":"EAST ASIA","AFR":"AFRICA","AMR":"AMERICA","EUR":"EUROPE","SAS":"SOUTH ASIA"}
    if algorithm=="PCA":
        pca_mod=load_model("pca","pca")   
        pca_transformed=pca_mod.transform(ohe)
        transformed_df=pd.DataFrame(pca_transformed)
        transformed_df.columns=["x","y","z"]
        pca_df=pd.concat([transformed_df,genome_test],axis=1)
        pca_df["color"]=pca_df["super_pop"].map(color_lookup)
        pca_df["pop_zone"]=pca_df["super_pop"].map(super_pop_lookup)
    return pca_df

    
