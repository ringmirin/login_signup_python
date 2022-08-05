import json
import os
user_input=int(input("enter 1 for sign-up and 2 for log-in: "))
if user_input==1:
    username=input("enter your name:   ")
    def mainfun():
        global username
        password1=input("Enter your password:  ")
        password2=input("confirm  password:  ")
        l,u,p,d=0,0,0,0
        for i in password1:  
            if (i.islower()): 
                l+=1 
            if (i.isupper()): 
                u+=1			 
            if (i.isdigit()):
                d+=1
            if i.issearch():		
                p+=1	
        if (l>=1 and u>=1 and p>=1 and d>=1 or l+p+u+d==len(password1)):
            if password1==password2:
                if len(password1)>=6 or len(password1)<=10:
                    print("password confirm")
                    if(os.path.isfile('login_signup.json')):
                        file_name=open("login_signup.json","r")
                        a=json.load(file_name)
                        for i in a["user"]:
                            if i["username"]==username:
                                print("This user is already exist")
                                break
                        else:
                                dic,d={},{}
                                dic["username"]=username
                                dic["password"]=password1
                                d["description"]=input("About: ")
                                d["Dob"]=input("date of birth: ")
                                d["Gender"]=input("gender: ")
                                d["Hobbies"]=input("hobbies: ")
                                dic["Profile"]=d
                                v=a["user"]
                                v.append(dic)
                                f=open("login_signup.json","w+")
                                json.dump(a,f,indent=4)  
                                f.close()
                                print("Signup Succesfully....")
                                   
                    else:
                            
                            dic,li,d,di={},[],{},{}
                            dic["username"]=username
                            dic["password"]=password1
                            d["description"]=input("About:- ")
                            d["Dob"]=input("Date of birth:- ")
                            d["Gender"]=input("gender:- ")
                            d["Hobbies"]=input("hobbies:- ")
                            dic["Profile"]=d
                            li.append(dic)
                            di["user"]=li
                            f=open("login_signup.json","w+")
                            json.dump(di,f ,indent=4)
                            f.close()
                            print("Signup Succesfully....")

                else:
                    print("password must be more than 6 characters")
            else:
                print("both password are not match :")
        else:
            print("must have atleast a digit, an uppercase and a special characters")
    mainfun()

                            

elif user_input==2:
    a=open("login_signup.json","r")
    f=json.load(a)
    d=input("Enter your user name:- ")
    v=input("Enter your password:-  ")
    for i in f["User"]:
        if i["username"]==d:
            if d==i['username']:
                if v==i['password']:
                    print("Login successful :) .......")
                    print(i)
                    break
                else:
                    print("wrong  password :( .....")
                    break
            else:
               print("wrong username :( ....")
               break
        else:
            print("this username doesn't exist")
            break
else:
    print("Your enter wrong input :( ....")
    
    
    

##########

# import json,os
# def my():
#     user=(input("enter login or signup :  "))
#     if user=="signup":
#         u_name=input("enter the user_name :  ")
#         password=input("enter the password :  ")
#         p=len(password)
#         numbers = "0123456789"
#         lower_case = "abcdefghijklmnopqrstuvwxyz"
#         upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         special_chr = "!@#$%^&*()-+"
#         n,l,u,s=0,0,0,0
#         i=0
#         while i<len(password):
#             if password[i] in numbers:
#                 n=n+1
#             if password[i] in lower_case:
#                 l=l+1
#             if password[i] in upper_case:
#                 u=u+1
#             if password[i] in special_chr:
#                 s=s+1
#             i=i+1
#         if p>=6:
#             if n>=1 and l>=1 and u>=1 and s>=1 :
#                 print("strong password")
#             else:
#                 print("invalid")
#         else:
#             print("no")
#         password1=((input("repassword1 the password :  ")))
#         if password==password1 :
#                 print("your password is match")
#                 if(os.path.isfile('Signup.json')):
#                     op=open("Signup.json","r")
#                     a=json.load(op)
#                     for i in a["user"]:
#                         if i["username"]==u_name:
#                             print("Already Exists")
#                             dic={}
#                             d={}
#                             dic["username"]=u_name
#                             dic["password"]=password1
#                             d["Description"]=input("enter description : ")
#                             d["D.O.B"]=input("enter D.O.B : ")
#                             d["Gender"]=input("enter your gender : ")
#                             d["Hobbies"]=input("enter your hobbies : ")
#                             dic["Profile"]=d
#                             v=a["user"]
#                             v.append(dic)
#                             f=open("Signup.json","w+")
#                             json.dump(a,f,indent=4)  
#                             f.close()
#                             print("Signup Succesfully")
#                             break  
#                 else:
                                
#                     dic={}
#                     l=[]
#                     d={}
#                     d1={}
#                     dic["username"]=u_name
#                     dic["password"]=password1
#                     d["description"]=input("enter the description : ")
#                     d["D.O.B"]=input("enter your D.O.B : ")
#                     d["Gender"]=input("enter your gender : ")
#                     d["Hobbies"]=input("enter your hobbies : ")
#                     dic["Profile"]=d
#                     l.append(dic)
#                     d1["user"]=l
#                     file=open("Signup.json","w+")
#                     json.dump(d1,file ,indent=4)
#                     file.close()
#                     print("Signup Succesfully")            
#         else:
#             print("wrong password")  
#     elif user=="login":
#         a=open("Signup.json","r")                 
#         f=json.load(a)
#         d=input("Enter your user name for login:")
#         v=input("Enter your password for login:")
#         for i in f["user"]:
#             if d==i['username']:
#                 if v==i['password']:
#                     print("Login successful")
#                     print(i)
#                     break
#                 else:
#                     print("Check your username")
#             else:
#                 print("Check your password")
#     else:
#         print("Your enter worng input ")       
# my()