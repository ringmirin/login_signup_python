import json,os
user_input=int(input("1-signup, 2-login: "))
if user_input==1:
   username=input("enter your name: ")
   def mainfun():
      global username
      pw1=input("enter your password: ")
     
      s="!@#$%^&*"
      a,b,c,d=0,0,0,0
      for i in pw1:
         if (i.isupper()):
            a+=1
         if (i.islower()):
            b+=1
         if (i.isdigit()):
            c+=1
         if i in s:
            d+=1
      if (len(pw1))>=6 and (len(pw1))<=10:
         if ((a and b and c and d)>=1 or a+b+c+d==len(pw1)):
            pw2=input("re-enter your password: ")
            if pw1==pw2:
                  print("password confirm")
                  if (os.path.isfile ("login_signup.json")):
                     filename=open("login_signup.json","r")
                     file=json.load(filename)
                     for i in file["User"]:
                        if i["username"]==username:
                           print("username already exist")
                           break
                        else:
                           dic,d={},{}
                           dic["username"]=username
                           dic["password"]=pw2
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
                     dict1,list,dict2,dict3={},[],{},{}
                     dict1["username"]=username
                     dict1["password"]=pw2
                     dict2["description"]=input("about: ")
                     dict2["DOB"]=input("date of birth: ")
                     dict2["gender"]=input("gender: ")
                     dict2["hobbies"]=input("hobbies: ")
                     dict1["profile"]=dict2
                     list.append(dict1)
                     dict3["User"]=list
                     f=open("login_signup.json","w+")  
                     json.dump(dict3,f, indent=4)  
                     f.close()
                     print("signup successfully")    
             
            else:
               print("Both pw should be same")
         else:
            print("password should have digitd, uppercase, lowercase,special character")
      else:
         print("password should have atleast 6 characters")
   mainfun()
if user_input==2:
   file_name=open("login_signup.json","r")
   f=json.load(file_name)
   file=input("enter your name: ")
   p=input("enter your password: ")
   for i in f["User"]:
      if i["username"]==file: 
         if file==i["username"]:
            if p==i["pw2"]:
              print("login successfully")
              print(i)
              break
            else:
               print("wrong password")
         else:
            print("username does not exist")
   else:
      print("you enter wrong input")
         
                     
                     
                        
                  
   
      
      