from flask import Flask, render_template
import json
import pandas as pd
import numpy as np

app = Flask(__name__,static_folder="static")

@app.route('/dashboard')
def dashboard():
    return render_template('index.html',scatter_data=scatter_data,pca_data=df_pca_json)
    
@app.route('/')
def test():
    return "test"

if __name__ == '__main__':
    with open("data/scatter.json","r") as f:
        scatter_data=json.load(f)
    with open("data/pca_data.json","r") as f:
        pca_data=json.load(f) 
    df_pca=pd.read_csv("data/dim_reduce.csv")
    randi=[np.random.choice(df_pca.shape[0]) for i in range(df_pca.shape[0])]
    df_pca=df_pca.loc[randi]
    df_pca=df_pca.head(500)
    df_pca_json=df_pca.to_dict(orient="records")
    with open("pca_data_red.json","w") as f:
        json.dump(df_pca_json,f,indent=1)
    app.run(host="localhost", port=5100, debug=True)    