from sqlalchemy import create_engine

# credentials to be stored in config
engine = create_engine('postgresql://akshay:seguinbenn@0.0.0.0:5432/genome')
conn=engine.connect()

def data_loader_db(table_name,df):
    df.to_sql(table_name, conn, if_exists='append', index=False, schema="public")
    status = "successfully loaded data into table :{} with rows:{}".format(table_name, df.shape[0])
    return status