import pickle
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def save_classifier(classifier):
   f = open('my_classifier.pickle', 'wb')
   pickle.dump(classifier, f, -1)
   f.close()

def load_classifier():
   f = open('my_classifier.pickle', 'rb')
   classifier = pickle.load(f)
   f.close()
   return classifier
def get_classification(data, target):
    # X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data["class"], test_size=0.2,
    #                                                     random_state=20)

    # Calling the Class
    naive_bayes = GaussianNB()

    # Fitting the data to the classifier
    naive_bayes.fit(data, target)

    save_classifier(naive_bayes)

    classifier = load_classifier()
    print(classifier)
    data = pd.DataFrame([[-5.65685425e-01, 8.37382645e-17 ,-3.16936872e-33]], columns=["a","b","c"])


    # # Predict on test data
    y_predicted = naive_bayes.predict(data)
    print(y_predicted)
    #
    # naive_bayes.predict_proba(X_test)
