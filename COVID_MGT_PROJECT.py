print ("*****************************************************")
print ("******Welcome to Covid Management System**********")
print ("****************************************************")

import mysql.connector # type: ignore
mydb=mysql.connector.connect (host='localhost',
 database='covid_management',
 user='root',
 password='XXXXXXX')

mycursor.execute ("use covid_management") # type: ignore
mycursor.execute (f"create table if not exist staff ( sno varchar(25) not null,name))
varchar(25) not null, age varchar(25) not null, gender char(1) not null, post 
varchar(25) not null, salary varchar(25) not null); ")

mycursor.execute (f"create table if not exists patients ( sno varchar(25) not  # type: ignore
null,name varchar(25) not null, age varchar(25) not null, gender char(1) not null, 
post varchar(25) not null, salary varchar(25 ) not null); ")

mycursor.execute (f"create table if not exists login (admin varchar (25) not null,  # type: ignore
password varchar (25) not null); ")

mycursor.execute (f"create table if not exists sno (patient varchar (25) not null, staff 
varchar (25) not null); ")
mycursor.execute ("select * from sno;")
z=0
for i in mycursor:
 z=1
if z==0:
mycursor.execute ("insert into sno values ('0','0'); ")
mydb.commit()
j=0
mycursor.execute ("select * from login;")
for i in mycursor:
 j=1
if (j==0):
mycursor.execute ("insert into login values ('Admin',' ng'); ")
mydb.commit()
loop1='y'
while(loopl=='y' or loop1=='Y') :
 print ("....................")
 print ("1.Admin")
 print ("2.Patient")
 print ("3.Exit")
 print ("....................")
chl=int(input("Enter your choice: "))
    if(chl==1):
    pas=input("Enter your Password: ")
mycursor.execute ("select from login")
 for i in mycursor:
 username, password-i
 if (pas==password):
 loop2='n'
 while (loop2-'n' or loop2=='N'):
 print ("__________________________")
 print ("1.Add patients")
 print ("2.Add staff")
 print ("3.Diaplay Patients Record")
 print ("4.Display Staff Record")
 print ("5.change password")
 print ("6.Remove Patients")
 print ("7.Remove Staff")
 print ("8.Logout")
 print ("__________________________")
 ch2=int (input ("Enter your choice: "))
 if (ch2==1) :
 loop3='y'
 I while (loop3=='y' or loop3=='Y'):
 name input ("Enter patients name: ")
 age-input ("Enter patients age: ")
 gender=input ("Enter patients gender: ")
 date-input ("Enter date of conformation of covid: ")
mycursor.execute ("select * from sno")
 for i in mycursor:
 patient, staff=i
 patient=int(patient) +1
mycursor.execute("insert into patients values ("+str(patient) 
+"',"+name+"',"+age+","+gender+","+date+")") # type: ignore
mycursor.execute(f"update sno set patient str{patient})
mydb.commit()
print("data of Patient has been saved successfully...")
mycursor.execute("select * from patients")
 t=0
 for i in mycursor:
 t+=1
t_idl, namel, agel, genderl, datel=i
 print (f"Total number of Corona Infected patients--> (patient}")
print(f"Active Corona Cases--> (t)")
print(f"This patient with id {t_idl} will be in quarantine upto 14 days from {datel}")
 loop3=input (f"Do You Want To Enter More Data of More Patients (y/n): 
")
 loop2=input ("Do You Want To Logout (y/n): ")
elif(ch2==2) :
 loop3='y'
 while (loop3=='y' or loop3=='Y'):
 name=input("Enter New Staff Name : ")
 age=input("Enter Age: ")
 gender-input("Enter gender (m/£) : ")
 post=input("Enter His/her post: ")
 salary=input("Enter His/her Salary: ")
mycursor.execute ("select * from sno")
 for i in mycursor:
 patient, staff=i
 staff=int(staff)+1
mycursor.execute(f"insert into staff values 
("+str(staff)+"','"+name+"',"+age+"','"+gender+"','"+post+"','"+salary+"')")
mycursor.execute("update sno set staff-'"+str(staff)+"")
mydb.commit()
print(f"staff with id {staff} has been saved successfully...")
mycursor.execute ("select• from staff")
 t=0
 for i in mycursor:
 t+=1
 print (f"Active Staff Members--> (t)")
 loop3=input ("Do You Want To Enter More Staff Data (y/n) :")
 loop2=input ("Do You Want To Logout (y/n): ")
elif(ch2==3):
idd=input("Enter patient's ID: ")
 t_id2,name2,age2,gender2,date2=["","","","",""]
mycursor.execute ("select * from patients where sno='"+idd+"")
 for i in mycursor:
 t_id2,name2,age2,gender2,date2=i
print("| IDI NAME | AGE I GENDER | CORONA POSITIVE DATE |")
print(f" (t id2) | {name2} | {age2} | {gender2} | (date2) |")
elif(ch2==4):
idd=input("Enter Staff ID: ")
 t_id3,name3,age3,gender3,past3,salary3=["","","","","",""]
mydb.commit ()
mycursor.execute("select * from staff where sno="+idd+"")
 for i in mycursor:
 t_id3,name3,age3,gender3,past3,salary3-i
 print ("| ID | NAME AGE | GENDER I POST I SALARY |")
 print (f"| {t_id3} I {name3} I {age3} I {gender3} 1 {past3}I {salary3} |")
elif(ch2==5):
 pas=input("Enter old Password: ")
mycursor.execute("select from login")
 for i in mycursor:
 username, password=i
 if (pas==password):
npas=input("Enter New Password: ")
mycursor.execute("update login set password="+npas+"")
mydb.commit()
 else:
print("Wrong Password...")
elif (ch2==6):
 Lod3='y'
 while (loop3=='y' or loop3=='Y'):
idd=input("Enter Patient ID")
mycursor.execute("delete from patients where sno="+idd+"")
mydb.commit()
print("Patient has been removed successfully")
 loop3=input("Do You Want To Remove More Patients (y/n) : ")
elif(ch2==7):
 loop3='y'
while(loop3=='y' or loop3=='Y'):
idd=input("Enter Staff ID")
mycursor.execute("delete from Staff where sno='" +idd+"")
mydb.commit()
print("Staff has been removed successfully")
 loop3=input("Do You Want To Remove More staff (y/n): ")
elif(ch2==8):
#  break
elif(ch1==2) :
print("Thank You for coming forward for your test...")
icough=input("Are you feeling cough? (y/n) : ").lower ()
 dry cough='n'
 cough='n'
if(icough=='y' or icough=='Y'):
 dry cough=input("Are you feeling dry cough (y/n): ").lower()
 cough=input("Are you feeling normal cough (y/n): ").lower()
 sneeze=input("Are You feeling Sneeze? (y/n): ").lower()
 pain=input("Are You feeling pain in your body? (y/n): ").lower()
 weakness=input("Are You feeling weakness? (y/n): ").1ower()
 mucus=input("Are You feeling any mucus (y/n) ").1ower()
itemp=int(input ("please Enter your temprature: "))
 if(itemp<=100):
 temp='low'
 else:
 temp='high'
 breath=input("Are you having difficulty in breathing (y/n): ").lower()
if(dry_cough=='y' and sneeze=='y' and pain=='y' and weakness=='y' and 
temp=='high' and breath=='y'):
print("Sorry to Say But According to us you are suffering from Corona......")
 name=input("Enter your name: ")
 age=input("Enter your age: ")
 gender=input("Enter your gender (m/f): ")
mycursor.execute ("select * from sno")
 for i in mycursor:
patient,staff=i
 patient=int(patient)+1
mycursor.execute("insert into patients values("+str(patient) +" 
"+name+"',"+age+","+gender+"', now()) ")
mycursor.execute ("update sno set patient="+str(patient) +"")
mydb.commit ()
 print ("data of Patient has been saved successfully...")
 print (f"Total number of Corona Infected patients--> {patient}")
mycursor.execute ("select from patients")
 t=0
 for i in mycursor:
 t+=1
 print (f"Active Corona Cases--> (t)")
mycursor.execute ("select * from patients")
 for i in mycursor:
 t_id5, name5, age5, gender5, date5=1
 print (f"This patient with id (t_id5) will be in quarantine upto l4 days 
from {date5}")
elif(dry_cough=='y' and sneeze=='y' and pain=='n' and weakness=='n' and 
temp=='low' and breath=='n'):
 print ("Nothing To worry, it’s just due to Air Pollution...")
elif(cough=='y' and mucus=='y' and sneeze=='y' and pain=='n' and weakness=='n' 
and temp=='low' and breath=3'n'):
 print ("nothing to worry, it’s just Common Cold...")
 else:
 print (f"You are not corona infected, if u are feeling something wrong, you 
just need to rest... ")
 print ("If then also you can't feel better, please consult to your doctor.")
elif(ch1==3):
 break