import pickle
import os

def save_model(model_obj,model_dir,model_name):
   if not os.path.exists(model_dir):
      os.makedirs(model_dir)
   f = open(os.path.join(model_dir,'{}.pickle'.format(model_name)), 'wb')
   pickle.dump(model_obj, f, -1)
   f.close()

def load_model(model_dir,model_name):
   f = open(os.path.join(model_dir,'{}.pickle'.format(model_name)), 'rb')
   model = pickle.load(f)
   f.close()
   return model


