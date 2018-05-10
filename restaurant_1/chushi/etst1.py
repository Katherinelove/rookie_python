import  pymysql

db=pymysql.connect("localhost","katherine","123456","db_kate",charset="utf8")
cursor=db.cursor()
ingredient = input("name of ingredient:")
num = input("number in storage:")
description = input("description:")
sql="""insert into ingredients(title,amount,description) values ("{title}","{amount}","{desc}")"""
sql=sql.format(title=ingredient,amount=num,desc=description)
try:
    cursor.execute(sql)
    db.commit()
except:
    print("sb")
db.close()