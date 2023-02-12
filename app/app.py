from flask import Flask, render_template
import json

app = Flask(__name__,static_folder="static")

@app.route('/dashboard')
def dashboard():
    return render_template('index.html',scatter_data=scatter_data,pca_data=pca_data)
    
@app.route('/')
def test():
    return "test"

if __name__ == '__main__':
    with open("data/scatter.json","r") as f:
        scatter_data=json.load(f)
    with open("data/test_pca.json","r") as f:
        pca_data=json.load(f)    
    app.run(host="localhost", port=5000, debug=True)    