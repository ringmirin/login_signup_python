import json
import os
user_input=int(input("1) signup, 2) login: "))
if user_input==1:
   username=input("enter your name: ")
   def mainfun():
      global username
      password1=input("enter password: ")
      password2=input("re-enter password: ")
      f="!@#$%&*^"
      a,b,c,d=0,0,0,0
      for i in password1:
         if (i.islower()):
            a+=1
         if (i.isupper()):
            b+=1
         if (i.isdigit()):
            c+=1
         if i in f:
            d+=1
      if (a>=1 and b>=1 and c>=1 and d>=1 or a+b+c+d==len(password1)):
         if password1==password2:
            if len(password1)>=6 and len(password1)<=10:
               print("confirm password")
               if (os.path.isfile("login_signup.json")):
                  file_name=open("login_signup.json","r")
                  file=json.load(file_name)
                  for i in file["User"]:
                     if i["username"]==username:
                        print("This user already exist")
                        break
                  else:
                     dic,d={},{}
                     dic["username"]=username
                     dic["password"]=password2
                     d["description"]=input["About"]
                     d["DOB"]=input("Date of birth")
                     d["Gender"]=input("Gender")
                     d["Hobbies"]=input("Hobbies")
                     dic["Profile"]=d
                     v=file["User"]
                     v.append(dic)
                     f=open("login_signup.json","w")
                     json.dump(file,f, indent=4)
                     f.close()
                     print("signup successfully")
                     
               else:
                  dic,list,d,dict={},[],{},{}
                  dic["username"]=username
                  dic["password"]=password1
                  d["description"]=input("About: ")
                  d["DOB"]=input("Date of birth: ")
                  d["Gender"]=input("Gender: ")
                  d["Hobbies"]=input("Hobbies: ")
                  dic["profile"]=d
                  list.append(dic)
                  dict["User"]=list
                  f=open("login_signup.json","w+")
                  json.dump(dict,f, indent=4)
                  f.close()
                  print("signup successfully")
            else:
               print("password must be more than 6 characters")
         else:
            print("both the password unmatch")
      else:
         print("must have atleast a digit, uppercase, lowercase and a special character")
                     
   mainfun()
   
elif user_input==2:
   a=open("login_signup.json","r")
   f=json.load(a)
   d=input("enter your name: ")
   e=input("enter your password")
   for i in f["User"]:
      if i["username"]==d:
         if d==i["username"]:
            if e==i["password"]:
               print("login successfully")
               print(i)
               break
            else:
               print("wrong password")
               break
         else:
            print("This username does not exist")
   else:
      print("you enter wrong input")
         
      