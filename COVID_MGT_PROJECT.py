print("*****************************************************")
print("******Welcome to Covid Management System**********")
print("*****************************************************")

import mysql.connector 
mydb = mysql.connector.connect(
    host='localhost',
    database='covid_management',
    user='root',
    password='XXXXXXX'
)

mycursor = mydb.cursor()  
mycursor.execute("USE covid_management")  

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS staff (
        sno VARCHAR(25) NOT NULL,
        name VARCHAR(25) NOT NULL,
        age VARCHAR(25) NOT NULL,
        gender CHAR(1) NOT NULL,
        post VARCHAR(25) NOT NULL,
        salary VARCHAR(25) NOT NULL
    );
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        sno VARCHAR(25) NOT NULL,
        name VARCHAR(25) NOT NULL,
        age VARCHAR(25) NOT NULL,
        gender CHAR(1) NOT NULL,
        date DATE NOT NULL
    );
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS login (
        admin VARCHAR(25) NOT NULL,
        password VARCHAR(25) NOT NULL
    );
""")

mycursor.execute("""
    CREATE TABLE IF NOT EXISTS sno (
        patient VARCHAR(25) NOT NULL,
        staff VARCHAR(25) NOT NULL
    );
""")

mycursor.execute("SELECT * FROM sno;")
z = 0
for i in mycursor:
    z = 1
if z == 0:
    mycursor.execute("INSERT INTO sno VALUES ('0', '0');")
    mydb.commit()

# Initialize login table with default values if it's empty
j = 0
mycursor.execute("SELECT * FROM login;")
for i in mycursor:
    j = 1
if j == 0:
    mycursor.execute("INSERT INTO login VALUES ('Admin', 'ng');")
    mydb.commit()

loop1 = 'y'
while loop1.lower() == 'y':
    print("....................")
    print("1. Admin")
    print("2. Patient")
    print("3. Exit")
    print("....................")
    chl = int(input("Enter your choice: "))

    if chl == 1:
        pas = input("Enter your Password: ")
        mycursor.execute("SELECT * FROM login")
        username, password = "", ""
        for i in mycursor:
            username, password = i
        if pas == password:
            loop2 = 'n'
            while loop2.lower() != 'n':
                print("__________________________")
                print("1. Add patients")
                print("2. Add staff")
                print("3. Display Patients Record")
                print("4. Display Staff Record")
                print("5. Change password")
                print("6. Remove Patients")
                print("7. Remove Staff")
                print("8. Logout")
                print("__________________________")
                ch2 = int(input("Enter your choice: "))
                
                if ch2 == 1:
                    loop3 = 'y'
                    while loop3.lower() == 'y':
                        name = input("Enter patient's name: ")
                        age = input("Enter patient's age: ")
                        gender = input("Enter patient's gender: ")
                        date = input("Enter date of confirmation of covid (YYYY-MM-DD): ")

                        mycursor.execute("SELECT * FROM sno")
                        patient, staff = 0, 0
                        for i in mycursor:
                            patient, staff = i
                        patient = int(patient) + 1

                        mycursor.execute(f"INSERT INTO patients VALUES ('{patient}', '{name}', '{age}', '{gender}', '{date}')")
                        mycursor.execute(f"UPDATE sno SET patient = '{patient}'")
                        mydb.commit()
                        print("Data of patient has been saved successfully...")

                        mycursor.execute("SELECT * FROM patients")
                        t = 0
                        for i in mycursor:
                            t += 1
                        print(f"Total number of Corona Infected patients: {t}")
                        print(f"This patient with id {patient} will be in quarantine up to 14 days from {date}")
                        loop3 = input("Do you want to enter more data of patients (y/n): ")

                elif ch2 == 2:
                    loop3 = 'y'
                    while loop3.lower() == 'y':
                        name = input("Enter new staff name: ")
                        age = input("Enter age: ")
                        gender = input("Enter gender (m/f): ")
                        post = input("Enter his/her post: ")
                        salary = input("Enter his/her salary: ")

                        mycursor.execute("SELECT * FROM sno")
                        patient, staff = 0, 0
                        for i in mycursor:
                            patient, staff = i
                        staff = int(staff) + 1

                        mycursor.execute(f"INSERT INTO staff VALUES ('{staff}', '{name}', '{age}', '{gender}', '{post}', '{salary}')")
                        mycursor.execute(f"UPDATE sno SET staff = '{staff}'")
                        mydb.commit()
                        print(f"Staff with id {staff} has been saved successfully...")

                        mycursor.execute("SELECT * FROM staff")
                        t = 0
                        for i in mycursor:
                            t += 1
                        print(f"Active Staff Members: {t}")
                        loop3 = input("Do you want to enter more staff data (y/n): ")

                elif ch2 == 3:
                    idd = input("Enter patient's ID: ")
                    mycursor.execute(f"SELECT * FROM patients WHERE sno = '{idd}'")
                    for i in mycursor:
                        t_id2, name2, age2, gender2, date2 = i
                    print("| ID | NAME | AGE | GENDER | CORONA POSITIVE DATE |")
                    print(f"| {t_id2} | {name2} | {age2} | {gender2} | {date2} |")

                elif ch2 == 4:
                    idd = input("Enter Staff ID: ")
                    mycursor.execute(f"SELECT * FROM staff WHERE sno = '{idd}'")
                    for i in mycursor:
                        t_id3, name3, age3, gender3, post3, salary3 = i
                    print("| ID | NAME | AGE | GENDER | POST | SALARY |")
                    print(f"| {t_id3} | {name3} | {age3} | {gender3} | {post3} | {salary3} |")

                elif ch2 == 5:
                    pas = input("Enter old password: ")
                    mycursor.execute("SELECT * FROM login")
                    for i in mycursor:
                        username, password = i
                    if pas == password:
                        npas = input("Enter new password: ")
                        mycursor.execute(f"UPDATE login SET password = '{npas}'")
                        mydb.commit()
                    else:
                        print("Wrong password...")

                elif ch2 == 6:
                    loop3 = 'y'
                    while loop3.lower() == 'y':
                        idd = input("Enter patient ID: ")
                        mycursor.execute(f"DELETE FROM patients WHERE sno = '{idd}'")
                        mydb.commit()
                        print("Patient has been removed successfully")
                        loop3 = input("Do you want to remove more patients (y/n): ")

                elif ch2 == 7:
                    loop3 = 'y'
                    while loop3.lower() == 'y':
                        idd = input("Enter staff ID: ")
                        mycursor.execute(f"DELETE FROM staff WHERE sno = '{idd}'")
                        mydb.commit()
                        print("Staff has been removed successfully")
                        loop3 = input("Do you want to remove more staff (y/n): ")

                elif ch2 == 8:
                    break

        else:
            print("Wrong Password...")

    elif chl == 2:
        print("Thank you for coming forward for your test...")
        icough = input("Are you feeling cough? (y/n): ").lower()
        dry_cough = 'n'
        cough = 'n'
        if icough == 'y' or icough == 'Y':
            dry_cough = input("Are you feeling dry cough (y/n): ").lower()
            cough = input("Are you feeling normal cough (y/n): ").lower()
        sneeze = input("Are you feeling sneeze? (y/n): ").lower()
        pain = input("Are you feeling pain in your body? (y/n): ").lower()
        weakness = input("Are you feeling weakness? (y/n): ").lower()
        mucus = input("Are you feeling any mucus (y/n): ").lower()
        itemp = int(input("Please enter your temperature: "))
        temp = 'low' if itemp <= 100 else 'high'
        breath = input("Are you having difficulty in breathing (y/n): ").lower()

        if dry_cough == 'y' and sneeze == 'y' and pain == 'y' and weakness == 'y' and temp == 'high' and breath == 'y':
            print("Sorry to say but according to us, you are suffering from Corona......")
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            gender = input("Enter your gender (m/f): ")
            mycursor.execute("SELECT * FROM sno")
            for i in mycursor:
                patient, staff = i
            patient = int(patient) + 1
            mycursor.execute(f"INSERT INTO patients VALUES ('{patient}', '{name}', '{age}', '{gender}', NOW())")
            mycursor.execute(f"UPDATE sno SET patient = '{patient}'")
            mydb.commit()
            print("Data of patient has been saved successfully...")
            print(f"Total number of Corona Infected patients: {patient}")
            mycursor.execute("SELECT * FROM patients")
            t = 0
            for i in mycursor:
                t += 1
            print(f"Active Corona Cases: {t}")
            mycursor.execute("SELECT * FROM patients")
            for i in mycursor:
                t_id5, name5, age5, gender5, date5 = i
            print(f"This patient with id {t_id5} will be in quarantine up to 14 days from {date5}")

        elif dry_cough == 'y' and sneeze == 'y' and pain == 'n' and weakness == 'n' and temp == 'low' and breath == 'n':
            print("Nothing to worry, it’s just due to air pollution...")
        elif cough == 'y' and mucus == 'y' and sneeze == 'y' and pain == 'n' and weakness == 'n' and temp == 'low' and breath == 'n':
            print("Nothing to worry, it’s just common cold...")
        else:
            print("You are not Corona infected, if you are feeling something wrong, you just need to rest...")
            print("If you still don't feel better, please consult your doctor.")

    elif chl == 3:
        break
