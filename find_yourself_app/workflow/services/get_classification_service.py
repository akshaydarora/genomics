import pickle
import pandas as pd
import os
import warnings
from sklearn.naive_bayes import GaussianNB
from .utils import save_model,load_model
warnings.filterwarnings(action="ignore",category=DeprecationWarning)


def get_classification(data, target):
    naive_bayes = GaussianNB()
    model_dir="model"
    naive_bayes.fit(data, target)
    save_model(naive_bayes,model_dir,"model_nb")


def get_classification_test(data,df):
   model_dir="model"
   classifier = load_model(model_dir,"model_nb")
    # # Predict on test data
   y_predicted = classifier.predict_proba(data[["x","y","z"]])
   y_output=pd.DataFrame(y_predicted)
   return y_output
