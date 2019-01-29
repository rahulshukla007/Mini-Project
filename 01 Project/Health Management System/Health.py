# Health Management System

#prerequisites
#Create 3 files for diet in same folder
#Create 3 files for exercise in same folder

#---------------------------------written time------------------------------------------#
def getdate():
    import datetime
    return datetime.datetime.now()
date = getdate()

#---------------------------------written data------------------------------------------#
def rohan_WD(name,x):
    with open("rohan_diet.txt", "w") as f:
        f.write(str(date)+'\n'+(input("write a diet: ")))
        print("\n----> You have written successfully <------")
def rohan_WE(name,x):
    with open("rohan_exercise.txt","w") as f:
        f.write(str(date)+'\n'+(input("name of exercise: ")))
        print("\n----> You have written successfully <------")

def harry_WD(name,x):
    with open("harry_diet.txt", "w") as f:
        f.write(str(date)+'\n'+(input("write a diet: ")))
        print("\n----> You have written successfully <------")
def harry_WE(name,x):
    with open("harry_exercise.txt","w") as f:
        f.write(str(date)+'\n'+(input("name of exercise: ")))
        print("\n----> You have written successfully <------")

def hammad_WD(name,x):
    with open("hammad_diet.txt", "w") as f:
        f.write(str(date)+'\n'+(input("write a diet: ")))
        print("\n----> You have written successfully <------")
def hammad_WE(name,x):
    with open("hammad_exercise.txt","w") as f:
        f.write(str(date)+'\n'+(input("name of exercise: ")))
        print("\n----> You have written successfully <------")

#---------------------------------Read data------------------------------------------------#
def rohan_RD(name,x):
    with open("rohan_diet.txt") as f:
        a=f.read()
        print(a)
def rohan_RE(name,x):
    with open("rohan_exercise.txt") as f:
        a = f.read()
        print(a)


def harry_RD(name,x):
    with open("harry_diet.txt") as f:
        a = f.read()
        print(a)
def harry_RE(name,x):
    with open("harry_exercise.txt") as f:
        a = f.read()
        print(a)

def hammad_RD(name,x):
    with open("hammad_diet.txt") as f:
        a = f.read()
        print(a)
def hammad_RE(name,x):
    with open("hammad_exercise.txt") as f:
        a = f.read()
        print(a)

#---------------------------------Take input------------------------------------------------#

decision = input("What you want to do-->\n1 for write, 2 for retrieve : ")
if decision == "1":
    name = input("Press --> 1 for Rohan,\n2 for Harry,\n3 for Hammad:\n" )
    x = input("Press --> 1 for Diet, 2 for for Exercise: ")
    if name == "1" and x == "1":
        rohan_WD(name,x)
    elif name == "1" and x == "2":
        rohan_WE(name,x)


    if name == "2" and x == "1":
        harry_WD(name,x)
    elif name == "2" and x == "2":
        harry_WE(name,x)


    if name == "3" and x == "1":
        hammad_WD(name,x)
    elif name == "3" and x == "2":
        hammad_WE(name,x)

else:
    name = input("Press --> 1 for Rohan,\n2 for Harry,\n3 for Hammad:\n")
    x = input("Press --> 1 for Diet, 2 for for Exercise: ")

    if name == "1" and x == "1":
        rohan_RD(name, x)
    elif name == "1" and x == "2":
        rohan_RE(name, x)

    if name == "2" and x == "1":
        harry_RD(name, x)
    elif name == "2" and x == "2":
        harry_RE(name, x)

    if name == "3" and x == "1":
        hammad_RD(name, x)
    elif name == "3" and x == "2":
        hammad_RE(name, x)


