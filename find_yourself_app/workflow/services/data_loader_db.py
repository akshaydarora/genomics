from sqlalchemy import create_engine



def get_sql_conn():
    # credentials to be stored in config
    engine = create_engine('postgresql://akshay:seguinbenn@0.0.0.0:5432/genome')
    conn=engine.connect()
    return conn

def data_loader_db(table_name,df):
    conn=get_sql_conn()
    df.to_sql(table_name, conn, if_exists='replace', index=False, schema="public")
    status = "successfully loaded data into table :{} with rows:{}".format(table_name, df.shape[0])
    conn.close()
    return status
