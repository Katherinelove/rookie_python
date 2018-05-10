import pymysql

# 2.插入操作
db = pymysql.connect(host="localhost", user="katherine",
                     password="123456", db="db_kate", port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

sql_insert = """insert into ingredients(title,amount,description) values("aple",'liu','1234')"""

try:
    cur.execute(sql_insert)
    # 提交
    db.commit()
except Exception as e:
    # 错误回滚
    print("sb")
    db.rollback()
finally:
    db.close()