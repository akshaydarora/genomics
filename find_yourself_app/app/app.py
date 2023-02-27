from flask import Flask, render_template
import json
import pandas as pd
import numpy as np
import os
from sqlalchemy import create_engine

app = Flask(__name__,static_folder="static")

def get_sql_conn():
    # credentials to be stored in config
    engine = create_engine('postgresql://akshay:seguinbenn@0.0.0.0:5432/genome')
    conn=engine.connect()
    return conn

def get_dim_red_data(dim_red_sql,conn):
    dim_red_series=[]
    dim_red_series_data={}
    df_dim_red=pd.read_sql(dim_red_sql,conn)
    uni_pop=df_dim_red["pop_zone"].unique()
    for pop in uni_pop:
        df_pop=df_dim_red[df_dim_red["pop_zone"]==pop].reset_index(drop=True)
        randi=[np.random.choice(df_pop.shape[0]) for i in range(df_pop.shape[0])]
        df_pop=df_pop.loc[randi]
        df_pop=df_pop.head(100)
        df_pop_color=df_pop["color"].values[0]
        df_pop_json=df_pop.to_dict(orient="records")
        dim_red_series_data["data"]=df_pop_json
        dim_red_series_data["name"]=pop
        dim_red_series_data["colorByPoint"]="true"
        dim_red_series_data["accessibility"]= {"exposeAsGroupOnly": "true"}
        dim_red_series_data["marker"]={"symbol":"circle","fillColor":"{}".format(df_pop_color)}
        dim_red_series.append(dim_red_series_data)
        dim_red_series_data={}
    return dim_red_series


@app.route('/dashboard')
def dashboard():
    return render_template('index.html',pca_data=df_pca_json,wheel_data=df_wheel_json)
    
@app.route('/')
def test():
    return "test"

if __name__ == '__main__':
    # conn=get_sql_conn()
    # dim_red_sql="select * from dim_reduce" 
    # df_pca_json=get_dim_red_data(dim_red_sql,conn)   
    # dep_wheel_sql='''
    # with tbl as (
    #     SELECT gf.variant,gs.super_pop,count(gf.genotype_enc) as sg FROM public.genome_sample_fact gf
	# 	Inner Join public.genome_samples gs
    #     On gf.sample=gs.sample
	# 	Where gf.genotype_enc in (1,2)
    #     Group by gf.variant,gs.super_pop
    #     Order by sg desc,gf.variant desc
		
    #     )	
    #     select * from (
    #         select super_pop as from,variant as to,sg as weight, 
    #             row_number() over (partition by super_pop order by sg desc) as super_pop_rank 
    #         from tbl) ranks
    #     where super_pop_rank <= 5
    #     order by weight desc;
    # '''
    # df_wheel=pd.read_sql(dep_wheel_sql,conn)
    # df_wheel_json=df_wheel.to_dict(orient="records")
    # with open("data/df_wheel.json","w") as f:
    #     json.dump(df_wheel_json,f,indent=1)
    # with open("data/pca_data.json","w") as f:
    #     json.dump(df_pca_json,f,indent=1)    
    with open("data/df_wheel.json","r") as f:
        df_wheel_json=json.load(f)
    with open("data/pca_data.json","r") as f:
        df_pca_json=json.load(f)
    app.run(host="0.0.0.0", port=80, debug=True)    