# -*- coding: utf-8 -*-
import pymysql


def open_database():
    db=pymysql.connect("localhost","katherine","123456","db_kate",charset="utf8")
    return db


def add_ingredient(cursor):
    ingredient = input("name of ingredient:")
    num = input("number in storage:")
    description = input("description:")
    sql = """insert into ingredients(title,amount,description) values ("{title}","{amount}","{desc}")"""
    sql = sql.format(title=ingredient, amount=num, desc=description)
    cursor.execute(sql)
    db.commit()
    print("added")

def find_ingredient(cursor,item):
    sql="""select title,amount from ingredients where title=\"{item}\""""
    sql=sql.format(item=item)

    cursor.execute(sql)
    items=cursor.fetchall()            #此语句用法尚待掌握
    if len(items)==0:
        print("sorry,that's ingredient was't found!")
    else:
        for item in items:
            print(item[0]+" "+item[1])


def list_ingredients(cursor):
    sql="""select title,amount from ingredients"""

    cursor.execute(sql)
    items=cursor.fetchall()
    print("items in the inventory!")
    for item in items:
        print(item[0]+" "+item[1])

def update_ingredient(cursor):
    item=input("which item?")
    column=input("what column?(title,amount,description)?")
    value=input("to what value?")
    if column[0].lower()=="t":
        sql="""update ingredients 
        set title="{new}" 
        where title=\"{title}\""""
    elif column[0].lower()=="a":
        sql = """update ingredients 
        set amount="{new}" 
        where title=\"{title}\""""
    elif column[0].lower()=="d":
        sql = """update ingredients 
                set description="{new}" 
                where title=\"{title}\""""
    else:
        print("input invalue!")

    sql=sql.format(new=value,title=item)
    cursor.execute(sql)
    db.commit()
    print("update successful")

def menu():
    print("what do you wnat to do?")
    print("A-add an ingredient!")
    print("S-search for an ingredient!")
    print("L-list all ingredients!")
    print("U-update the ingredient")
    print("Q-quit")
    choice=input("choice[A/S/L//U/Q]:")
    return choice[0].strip().lower()

db = open_database()
cursor = db.cursor()      #方法是括号，不能省略！

while True:
    choice=menu()
    if choice=="a":
        add_ingredient(cursor)
    elif choice=="s":
        item=input("what ingredient?")
        find_ingredient(cursor,item)
    elif choice=="l":
        list_ingredients(cursor)
    elif choice=="u":
        update_ingredient(cursor)
    elif choice=="q":
        print("goodbye")
        break
    else:
        print("input invalues!")
db.commit()
db.close()