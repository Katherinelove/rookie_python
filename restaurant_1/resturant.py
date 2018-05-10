from datetime import datetime
import os
import json
import pymysql

def get_seats():
    seats = []
    message = "请输入你约定了几桌？"
    seat_num = input(message)
    for i in range(int(seat_num)):
        print("seat", i + 1)
        seat = get_seat()
        seats.append(seat)
    return seats


def get_seat():
    seat = []
    while True:
        item = float(input("本桌菜单单价：[0点餐下一桌]"))
        if item != 0:
            seat.append(item)
        else:
            return seat


def print_time():
    time = datetime.now()
    temp_time = "date/time:{M}/{D}/{Y} {H}:{Min}"
    print(temp_time.format(M=time.month, D=time.day, Y=time.year, H=time.hour, Min=time.minute))


def print_seat(seat):
    for item in seat:
        print("${}".format(item))
        total = get_seat_total(seat)
    print("=" * 30)
    print("本桌共花费{}".format(total))


def get_seat_total(seat):
    total = 0
    for item_price in seat:
        total += item_price
    return total


def print_receipt(seats):
    print_time()

    grand_total = 0
    for seat in seats:
        print_seat(seat)
        grand_total += get_seat_total(seat)
        print()
    print("{}桌共消费{}".format(len(seats), grand_total))
    return grand_total

def get_receipt(filename):
    try:
        f=open("restaurant_1/receipts/"+filename)
        reciepts=json.load(f)
        f.close()
    except:
        reciepts={}
    return reciepts

def save_receipt(grand_total):
    try :
        os.makedirs("restaurant_1/receipts")
    except:
        pass
    date=datetime.now()
    filename="{Y}{M}{D}.json".format(Y=date.year,M=date.month,D=date.day)
    receipts=get_receipt(filename)
    key=str(date.hour)+str(date.minute)+str(date.second)
    receipts[key]=grand_total
    f=open("restaurant_1/receipts/"+filename,"w")
    json.dump(receipts,f,indent=10)
    f.close()
    show_day_receipts_sheet(filename)

def show_day_receipts_sheet(filename):
    f=open("restaurant_1/receipts/"+filename)
    json_date=json.load(f)
    f.close()
    print(json_date)


while True:
    seats=get_seats()
    grand_total=print_receipt(seats)
    save_receipt(grand_total)

    q=input("quit?[y/n]")
    if q[0].lower()=="y":
        break