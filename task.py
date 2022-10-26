
f_file = open('data.txt','w+')
import re

def passwd(password):
  l, u, p, d = 0, 0, 0, 0
                
  capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  smallalphabets="abcdefghijklmnopqrstuvwxyz"
  specialchar="$@_"
  digits="0123456789"
  
  for i in password:

      # counting lowercase alphabets
      if (i in smallalphabets):
          l+=1           
      # counting uppercase alphabets
      if (i in capitalalphabets):
          u+=1            
      if (i in digits):
          d+=1           
      if(i in specialchar):
          p+=1 

  if (l>=1 and u>=1 and p>=1 and d>=1):
      print("Valid Password")
      return True
  else:
    print("invalid password")
    return False

def Register():
  username=input("Enter Username :")
  password=input("Enter Password :")
  db = open("data.txt", "r")
  d = []
  for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        d.append(a)
  if len(password)>5 and len(password)<=16:
   
          if(not username==None):
             db=open("data.txt","r")
             db = db.readlines()
             users = []
             for d in db:
               user = d.split(',')[0]
               users.append(user)
             if(username in users):
               print("user exists")
               Register()
             else:
                if(bool(re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',username))==True):
                  status = passwd(password)
                  if status:
                    db = open("data.txt", "w")
                    db.write(username+", "+password+"\n")
                    print("User created successfully!")
                    print("Please login to proceed:")
                  else:
                    Register()
                else:
                    print("Invalid Username")
                    Register()      
                
          else:
            print("Username should not be null")
            Register()     
     
  else:
     print("Inavlid Password")
     Register()


def login():
    Username = input("Enter your username:")
    Password = input("Enter your Password:")
    
    if not len(Username or Password) < 1:
        if True:
            db = open("data.txt", "r")
            db = db.readlines()
            d = []
            f = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
                if Username in data.keys():
                  if Password == data[Username]:
                    print("Login success!")
                    print("Hi", Username)
                  else:
                    print("password incorrect")
                    passwordsuggest = int(input("1:forgetten password|2:new password"))
                    if(passwordsuggest == 1):
                      print("Retrived user password : ", data[Username])              
                    elif(passwordsuggest == 2):
                      newpassword=input("Enter new password")
                      status = passwd(newpassword)
                      if status:
                        data[Username] = newpassword
                        print("Password updated :)")
                      else:
                        while (not status):
                          print("Invalid Password \n Enter the valid password :")
                          newpassword=input("Enter new password")
                          status = passwd(newpassword)
                          if status:
                            data[Username] = newpassword
                            print("Password updated :)")
                                       
                else:
                    print("Username doesn't exist")
                    print("User does not exist! Do you want to Register ?")
                    response = input("y or n")
                    if response == 'y': 
                      Register()
                    else:
                      pass
        else:
            print("Error logging into the system")
            login()
            
    else:
        print("Please attempt login again")
        login()


mode = int(input("Select Mode : 1. Register | 2. Login : "))
if mode == 1:
  Register()
elif mode == 2:
  login()
else:
  print("Invalid mode :( ")

