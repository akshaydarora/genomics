import pickle
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import warnings
warnings.filterwarnings(action="ignore",category=DeprecationWarning)

def save_classifier(classifier,model_dir):
   if not os.path.exists(model_dir):
      os.makedirs(model_dir)
   f = open(os.path.join(model_dir,'my_classifier.pickle'), 'wb')
   pickle.dump(classifier, f, -1)
   f.close()

def load_classifier():
   f = open('model/my_classifier.pickle', 'rb')
   classifier = pickle.load(f)
   f.close()
   return classifier
def get_classification(data, target):
    naive_bayes = GaussianNB()
    model_dir="model"
    naive_bayes.fit(data, target)
    save_classifier(naive_bayes,model_dir)

    # classifier = load_classifier()
    # print(classifier)
    # data = pd.DataFrame([[-5.65685425e-01, 8.37382645e-17 ,-3.16936872e-33]], columns=["a","b","c"])
    #
    #
    # # # Predict on test data
    # y_predicted = naive_bayes.predict(data)
    # print(y_predicted)

