import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost',user='root',password='tkdals!0715',db='DS_hw1',charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)

sql = "select * FROM score"
cursor.execute(sql)

print(f"{'sno':>4}{'midterm':>9}{'final':>9}")
for i in cursor:
    if i['midterm'] >=20 and i['final'] >=20 :
        print(f"{i['sno']:>4}{i['midterm']:>9}{i['final']:>9}")
    

cursor.close()
conn.close()