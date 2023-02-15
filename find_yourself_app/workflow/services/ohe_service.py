import pandas as pd
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import OneHotEncoder
import warnings
from .utils import save_model,load_model
warnings.filterwarnings(action="ignore",category=DeprecationWarning)


def get_one_hot_encoding(df):
    ncols = len(df.columns)
    ohe = OneHotEncoder(categories=[range(4)] * ncols, sparse=False)
    ohe_mod=ohe.fit(df.values)
    save_model(ohe_mod,"ohe","ohe")
    ohe_transformed=ohe_mod.transform(df.values)
    return ohe_transformed


def get_one_hot_encoding_test(df):
    ohe_mod=load_model("ohe","ohe")   
    ohe_transformed=ohe_mod.transform(df.values)
    return ohe_transformed
    