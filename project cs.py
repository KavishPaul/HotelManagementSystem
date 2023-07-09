import mysql.connector as mycon
mydb=mycon.connect(host="localhost",user="root",passwd="kav7678ish",database="hotel")
mycursor=mydb.cursor()

mycursor.execute("create table if not exists customer(name varchar(25),mobileNo int(11),nationality varchar(20),\
state varchar(20),checkin varchar(20),checkout varchar(20))")

mycursor.execute("create table if not exists roomcharges(roombill int(6))")
mycursor.execute("create table if not exists restaurant_bill(rbill int(6))")
mycursor.execute("create table if not exists laundry_bill(lbill int(6))")
mycursor.execute("create table if not exists game_bill(gbill int(6))")


def hotel():

    file=open("Hotel.txt","r")
    read=file.readlines()
    for i in read:
        print(i,end="")


def enter_details(name,mobileNo,nationality,state,checkin,checkout):

    print("*** You have successfully entered your details ***")
    mycursor.execute("insert into customer(name,mobileNo,nationality,state,checkin,checkout) values\
    ('{}',{},'{}','{}',\'{}','{}')".format(name,mobileNo,nationality,state,checkin,checkout))
    mydb.commit()


def roomcharges():
    print("**** We have following types of rooms for you:- ****")

    print("1. Type-1 ----->  ₹8000/- per day")

    print("2. Type-2 ----->  ₹7000/- per day")

    print("3. Type-3 ----->  ₹6000/- per day")

    print("4. Type-4 ----->  ₹5000/- per day")

    your_room=int(input("Enter the room type which you want to take (1/2/3/4)"))

    days=int(input("Enter the number of days you want to stay"))

    if your_room==1:

        print("You have chosen room type '1'")
        print("You stayed for",days,"days")
        roombill=(8000*days)
        print("Your room charges will be ₹",roombill,"\n")

        mycursor.execute("insert into roomcharges(roombill) values({})".format(roombill))
        mydb.commit()

    elif your_room==2:

        print("You have chosen room type '2'")
        print("You stayed for",days,"days")
        roombill=(7000*days)
        print("Your room charges will be ₹",roombill,"\n")

        mycursor.execute("insert into roomcharges(roombill) values({})".format(roombill))
        mydb.commit()

    elif your_room==3:
        print("You have chosen room type '3'")
        print("You stayed for",days,"days")
        roombill=(6000*days)
        print("Your room charges will be ₹",roombill,"\n")

        mycursor.execute("insert into roomcharges(roombill) values({})".format(roombill))
        mydb.commit()

    elif your_room==4:
        print("You have chosen room type '4'")
        print("You stayed for",days,"days")
        roombill=(5000*days)
        print("Your room charges will be ₹",roombill,"\n")

        mycursor.execute("insert into roomcharges(roombill) values({})".format(roombill))
        mydb.commit()

    else:
        print("****  Please enter a valid room type!!!  ****")

def restaurantbill():

    print("**** RESTAURANT MENU ****")

    print("1. Breakfast package ----> ₹800 \n2. Lunch package ----> ₹800 \n3. Dinner package ----> ₹800 \n\
4. Tea ----> ₹80 \n5. Water bottle(bisleri) ----> ₹50 \n6. exit")
    rbill=0


    while 1>0:

        choice=int(input("Enter your choice from the menu"))

        if  choice==1:

            q=int(input("Enter the quantity of the food item you bought"))

            print("You bought",q,"breakfast package")

            rbill=rbill+(800*q)

        elif choice==2:

            q=int(input("Enter the quantity of the food item you bought"))

            print("You bought",q,"lunch package")

            rbill=rbill+(800*q)

        elif choice==3:

            q=int(input("Enter the quantity of the food item you bought"))

            print("You bought",q,"dinner package")

            rbill=rbill+(800*q)

        elif choice==4:

            q=int(input("Enter the quantity of the food item you bought"))

            print("You bought",q,"tea")

            print()

            rbill=rbill+(80*q)

        elif choice==5:

            q=int(input("Enter the quantity of the food item you bought"))

            print("You bought",q,"bottles of water")

            rbill=rbill+(50*q)

        elif choice==6:
            break

        else:
            print("----- Invalid Option -----")

    print("Your total restaurant bill is: ₹",rbill,"\n")

    mycursor.execute("insert into restaurant_bill(rbill) values({})".format(rbill))
    mydb.commit()

def laundrybill():

    print("**** LAUNDRY MENU ****")

    print("1. Jeans ---> ₹100\n2. Shirt/T-shirt ---> ₹100\n3. Shorts ---> ₹80\n\
4. Trousers ---> ₹80\n5. Saree ---> ₹150\n6. Exit")
    lbill=0

    while 1>0:

        laundry=int(input("Enter your choice from the laundry menu"))

        if laundry==1:
            q=int(input("Enter the quantity"))
            print("You gave",q,"jeans to laundry")
            lbill=lbill+(100*q)

        elif laundry==2:
            q=int(input("Enter the quantity"))
            print("You gave",q,"shirt/T-shirt to laundry")
            lbill=lbill+(100*q)

        elif laundry==3:
            q=int(input("Enter the quantity"))
            print("You gave",q,"shorts to laundry")
            lbill=lbill+(80*q)

        elif laundry==4:
            q=int(input("Enter the quantity"))
            print("You gave",q,"trousers to laundry")
            lbill=lbill+(80*q)

        elif laundry==5:
            q=int(input("Enter the quantity"))
            print("You gave",q,"saree to laundry")
            lbill=lbill+(150*q)

        elif laundry==6:
            break

        else:
            print("----- Invalid Option -----")

    print("Your total laundry bill is: ₹",lbill,"\n")

    mycursor.execute("insert into laundry_bill(lbill) values({})".format(lbill))
    mydb.commit()

def gamebill():

    print("**** GAME MENU ****")

    print("1. Snooker ---> ₹70\n2. Table Tennis ---> ₹70\n3. Video Games ---> ₹50\n\
4. Swimming ---> ₹100\n5. Bowling ---> ₹80\n6. Exit")
    gbill=0

    while 1>0:

        game=int(input("Enter your choice from the game menu"))

        if game==1:
            n=int(input("Enter the number of hours you played that game"))
            print("You played snooker for",n,"hours")
            gbill=gbill+(70*n)

        elif game==2:
            n=int(input("Enter the number of hours you played that game"))
            print("You played table tennis for",n,"hours")
            gbill=gbill+(70*n)

        elif game==3:
            n=int(input("Enter the number of hours you played that game"))
            print("You played video games for",n,"hours")
            gbill=gbill+(50*n)

        elif game==4:
            n=int(input("Enter the number of hours you played that game"))
            print("You did swimming for",n,"hours")
            gbill=gbill+(100*n)

        elif game==5:
            n=int(input("Enter the number of hours you played that game"))
            print("You did bowling for",n,"hours")
            gbill=gbill+(80*n)

        elif game==6:
            break

        else:
            print("----- Invalid Option -----")

    print("Your total game bill is: ₹",gbill,"\n")

    mycursor.execute("insert into game_bill(gbill) values({})".format(gbill))
    mydb.commit()


def display():

    mycursor.execute("select * from customer")
    for j in mycursor:
        name=j[0]
        mobileNo=j[1]
        nationality=j[2]
        state=j[3]
        checkin=j[4]
        checkout=j[5]

    mycursor.execute("select * from roomcharges")
    for k in mycursor:
        roombill=k[0]

    mycursor.execute("select * from restaurant_bill")
    for l in mycursor:
        rbill=l[0]

    mycursor.execute("select * from laundry_bill")
    for m in mycursor:
        lbill=m[0]

    mycursor.execute("select * from game_bill")
    for n in mycursor:
        gbill=n[0]

    print("**** HOTEL BILL ****")
    print("\n")
    print("    Customer details:")
    print("\n")
    print("Customer name:",name)
    print("Customer's mobile number",mobileNo)
    print("Customer's nationality:",nationality)
    print("Customer's state:",state)
    print("Check In date:",checkin)
    print("Check Out date:",checkout)
    print("Your room charges are: ₹",roombill)
    print("Your restaurant bill is: ₹",rbill)
    print("Your laundry bill is: ₹",lbill)
    print("Your game bill is: ₹",gbill)
    print("\n")

    subtotal=(roombill+rbill+lbill+gbill)
    tax=(0.1*subtotal)
    totalbill=(subtotal+tax)

    print("Your bill(without tax) is: ₹",subtotal)
    print("Tax is: ₹",tax)
    print("Your total bill is: ₹",totalbill)
    print("\n")

def main():

    while 1>0:

        print("**** Choose an option ****")
        print("\n")
        print("1. Read basic instructions")
        print("2. Enter your details")
        print("3. Calculate room charges")
        print("4. Calculate restaurant bill")
        print("5. Calculate laundry bill")
        print("6. Calculate game bill")
        print("7. Calculate total bill")
        print("8. Exit")
        print("\n")

        choice=int(input("Enter your choice"))

        if choice==1:
            hotel()

        elif choice==2:

            name=input("Enter your name")
            mobileNo=int(input("Enter your mobile number"))
            nationality=input("Enter your nationality")
            state=input("Enter the state in which you live")
            checkin=input("Enter your check in date")
            checkout=input("Enter your check out date")
            enter_details(name,mobileNo,nationality,state,checkin,checkout)

        elif choice==3:
            roomcharges()

        elif choice==4:
            restaurantbill()

        elif choice==5:
            laundrybill()

        elif choice==6:
            gamebill()

        elif choice==7:
            display()

        elif choice==8:
            print("**** THANK YOU FOR STAYING IN OUR HOTEL ****")
            break

        else:
            print("----- Invalid Option -----")

main()