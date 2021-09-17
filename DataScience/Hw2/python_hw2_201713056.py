import pandas as pd
from sqlalchemy import create_engine
import pymysql 

xl_file = 'score.xlsx'
df = pd.read_excel(xl_file)

engine = create_engine("mysql+pymysql://root:tkdals!0715@localhost:3306/DS_hw1", encoding='utf-8')
conn = engine.connect()

df.to_sql(name='score', con=conn, if_exists='replace',index=False)  