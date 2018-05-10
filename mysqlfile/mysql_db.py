# -*- coding: utf-8 -*-
import pymysql
db=pymysql.connect("localhost","katherine","123456","db_kate" ,charset="utf8")
cursor=db.cursor()
sql="""select * from t_student"""
try:
    cursor.execute(sql)
    results=cursor.fetchall()
    for items in results:
        print(items)
except:
    print("error:unable to fetch data!")
db.close()
