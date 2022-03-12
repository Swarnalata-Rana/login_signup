def register():
    db=open("database.txt","r")
    username=input("create username:-")
    password=input("create password:-")
    password1=input("confirm password:-")
    # gender=input("enter your gender")
    # DOB=input("enter your DOB")
    d=[]
    f=[]
    for i in db:
        a,b=i.split(",")
        b=b.strip()
        d.append(a)
        f.append(b)
    data=dict(zip(d,f))
    if password!=password1:
        print("passwords don't match,restar")
        register()
    else:
        if len(password)<=6:
            print("password too short,restart:")
            register()
        elif username in d:
           print("username exist")
           register()
        else:
             db=open("database.txt","a")
             db.write(username+","+password+"\n")
             print("success!")
def access():
    db=open("database.txt","r")
    username=input("enter your username:-")
    password=input("enter your password:-")
    # gender=input("enter your gender")
    # DOB=input("enter your DOB")

    if not len(username or password)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(",")
            b=b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d,f))
        try:
            if data[username]:
                try:
                    if password==data[username]:
                        print("login success")
                        print("hii,",username)
                    else:
                        print("password or username incorrect")
                except:
                    print("incorrect passwoard or username")
            else:
                print("username doesn't exist")
        except:
            print("login error")
def home(option=None):
    option=input("login | signup:-")
    if option=="login":
        access()
    elif option=="signup":
        register()
    else:
        print("plese enter an option")
home()




    