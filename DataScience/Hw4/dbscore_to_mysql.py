#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pymysql
import pandas as pd

def load_score_data():
    xlsx_file = 'db_score_3_labels.xlsx'
    score = pd.read_excel(xlsx_file)

    conn = pymysql.connect(host='localhost', user='root', password='tkdals!0715', db='classification')
    curs = conn.cursor(pymysql.cursors.DictCursor)
        
    drop_sql = """drop table if exists score """
    curs.execute(drop_sql)
    conn.commit()
    
    import sqlalchemy
    database_username = 'root'
    database_password = 'tkdals!0715'
    database_ip       = 'localhost'
    database_name     = 'classification'
    database_connection = sqlalchemy.create_engine('mysql+pymysql://{0}:{1}@{2}/{3}'.
                                                   format(database_username, database_password, 
                                                          database_ip, database_name))
    score.to_sql(con=database_connection, name='score', if_exists='replace')  
    
load_score_data()


# In[ ]:




