"""Health Management System:- write a function that when executed takes as input client name
One more function to retrieve exercise or food for any client

* Health Management System. 3 clients - Sujay, Rohan and Avi
* Total 6 files. write a function that when executed takes as input client name
* One more function to retrieve exercise or food for any client"""


def getdate():
    import datetime
    return datetime.datetime.now()


def retrieve_food1():
    f = open("Sujay_food.txt")
    print(f.read(), "\n")
    f.close()


def retrieve_exercise1():
    f = open("Sujay_exercise.txt")
    print(f.read(), "\n")
    f.close()


def log_food1():
    f = open("Sujay_food.txt", 'a')
    date = str(getdate())
    f.write("[")
    f.write(date)
    f.write("]\t")
    up = input("\nEnter the food which Sujay is ate:-")
    f.write(up.upper())
    f.write("\n")
    f.close()
    print("\nYou successfully update Sujay's food list\n")


def log_exercise1():
    f = open("Sujay_exercise.txt", "a")
    date = str(getdate())
    f.write("[")
    f.write(date)
    f.write("]\t")
    up = input("\nEnter what Sujay do in exercise:-")
    f.write(up.upper())
    f.write("\n")
    print("\nYou successfully update Sujay's exercise list\n")


def retrieve_food2():
    f = open("Rohan_food.txt")
    print(f.read(), "\n")
    f.close()


def retrieve_exercise2():
    f = open("Rohan_exercise.txt")
    print(f.read(), "\n")
    f.close()


def log_food2():
    f = open("Rohan_food.txt", 'a')
    date = str(getdate())
    f.write("[")
    f.write(date)
    f.write("]\t")
    up = input("\nEnter the food which Rohan is ate:-")
    f.write(up.upper())
    f.write("\n")
    f.close()
    print("\nYou successfully update Rohan's food list\n")


def log_exercise2():
    f = open("Rohan_exercise.txt", "a")
    date = str(getdate())
    f.write("[")
    f.write(date)
    f.write("]\t")
    up = input("\nEnter what Rohan do in exercise:-")
    f.write(up.upper())
    f.write("\n")
    print("\nYou successfully update Rohan's exercise list\n")


def retrieve_food3():
    f = open("Avi_food.txt")
    print(f.read(), "\n")
    f.close()


def retrieve_exercise3():
    f = open("Avi_exercise.txt")
    print(f.read(), "\n")
    f.close()


def log_food3():
    f = open("Avi_food.txt", 'a')
    date = str(getdate())
    f.write("[")
    f.write(date)
    f.write("]\t")
    up = input("\nEnter the food which Avi is ate:-")
    f.write(up.upper())
    f.write("\n")
    f.close()
    print("\nYou successfully update Avi's food list\n")


def log_exercise3():
    f = open("Avi_exercise.txt", "a")
    date = str(getdate())
    f.write("[")
    f.write(date)
    f.write("]\t")
    up = input("\nEnter what Avi do in exercise:-")
    f.write(up.upper())
    f.write("\n")
    print("\nYou successfully update Avi's exercise list\n")


while True:
    name = int(input("1. Sujay's file\n2. Rohan's file\n3. Avi's file\n0. Exit\nEnter your file's choice:-"))
    if (name==1):
        sel = int(input("\nYou choose Sujay's file\n1. Log food record\n2. Log exercise record"
                        "\n3. Retrieve food\n4. Retrieve exercise\nEnter your choice:-"))
        if (sel==1):
            log_food1()
        elif (sel==2):
            log_exercise1()
        elif (sel==3):
            retrieve_food1()
        elif (sel==4):
            retrieve_exercise1()
        else:
            print("You enter wrong choice")
    elif (name==2):
        sel = int(input("\nYou choose Rohan's file\n1.Log food record\n2.Log exercise record"
                        "\n3. Retrieve food\n4. retrieve exercise\nEnter your choice:-"))
        if (sel==1):
            log_food2()
        elif (sel==2):
            log_exercise2()
        elif (sel==3):
            retrieve_food2()
        elif (sel==4):
            retrieve_exercise2()
        else:
            print("You enter wrong choice")
    elif (name==3):
        sel = int(input("\nYou choose Avi's file\n1. Log food record\n2.Log exercise record"
                        "\n3.Retrieve food\n4.Retrieve exercise\nEnter your choice:-"))
        if (sel==1):
            log_food3()
        elif (sel==2):
            log_exercise3()
        elif (sel==3):
            retrieve_food3()
        elif (sel==4):
            retrieve_exercise3()
        else:
            print("You enter wrong choice")
    elif (name==0):
        break
    else:
        print("You enter wrong choice")
