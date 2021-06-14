from Gym_manger import Gym_memberships
from Coustmer import Customer

print("****************** GYM MEMBERSHIP PORTAL******************")
print(" Hello Admin, please select a from below shown menu")

def menu():
    print("1. Create Member")
    print("2. View Member")
    print("3. Delete Member")
    print("4. Update Member") 
    print("5. Create Regimen")
    print("6. View Regimen")
    print("7. Delete Regimen")
    print("8. Update Regimen")
    print("0. Exit")
    print("\n Enter you choice: ")

menu()

while True:
    option = int(input())
    if option == 1:
        name = str(input("Enter your member's Name - "))
        age = str(input("Enter member's Age -"))
        gender = str(input("Enter member's Gender -"))
        phone_no = str(input("Enter member's Phone - "))
        email = str(input("Enter member's Email ID -"))
        bmi = str(input("Enter member's BMI - "))
        if bmi < '18.5':
            r={'Mon': 'Chest\n',
                'Tue': 'Biceps\n',
                'Wed': 'Rest\n',
                'Thu': 'Back\n',
                'Fri': 'Triceps\n',
                'Sat': 'Rest\n',
                'Sun': 'Rest'}
        elif bmi < '25':
            r={'Mon': 'Chest\n',
                'Tue': 'Biceps\n',
                'Wed': 'Cardio/Abs\n',
                'Thu': 'Back\n',
                'Fri': 'Triceps\n',
                'Sat': 'Legs\n',
                'Sun': 'Rest'}
        
        elif bmi < '30':
            r={'Mon': 'Chest\n',
                'Tue': 'Biceps\n',
                'Wed': 'Cardio/Abs\n',
                'Thu': 'Back\n',
                'Fri': 'Triceps\n',
                'Sat': 'Legs\n',
                'Sun': 'Cardio'}
        
        elif bmi >= '30':
            r={'Mon': 'Chest\n',
                'Tue': 'Biceps\n',
                'Wed': 'Cardio/Abs\n',
                'Thu': 'Back\n',
                'Fri': 'Triceps\n',
                'Sat': 'Cardio\n',
                'Sun': 'Cardio'}


        duration = str(input("Enter member's Duration(in months) - "))
        coustmer = Customer(name,age,gender,phone_no,email,bmi,duration)
        Gym_memberships.regimen[phone_no]=r
        Gym_memberships.add_coustmer(coustmer)

    elif option == 2:
        ck_phone=input("Enter member's Phone Number: ")
        #print("Name\tAge\tgender\tPhone_no\tEmail\tbmi\tDuration")
        for customer_id in Gym_memberships.coustmer_data.keys():
            if customer_id==ck_phone:
                customer=Gym_memberships.coustmer_data[customer_id]
                name=customer.getName()
                age=customer.getAge()
                gender=customer.getGender()
                phone_no=customer.getphone_no()
                Email=customer.getEmail()
                bmi=customer.getBmi()
                duration=customer.getDuration()

                print(" Name: {}\n Age : {} \n gender: {} \n Phone_no: {} \n Email: {} \n bmi: {}\n Duration: {}\n".format(name,age,gender,phone_no,Email,bmi,duration))
        print("\n")

    elif option == 3:
        ck_phone=input("Enter phone_number of member you want to delete")
        try:
            for customer_id in Gym_memberships.coustmer_data.keys():
                if customer_id==ck_phone:
                    print("Member Deleted")
            Gym_memberships.coustmer_data.pop(ck_phone)
        except:
            print("Number doesn't Exists\n")
    
    elif option == 4:
        ck_phone=input("Enter Phone Number of the member to Update Membership:")
        extent=input("Type 'extend' or 'revoke' if u want Update Member ")
        if extent == 'extend':
            for customer_id in Gym_memberships.coustmer_data.keys():
                customer=Gym_memberships.coustmer_data[customer_id]
                if customer_id==ck_phone:
                    dur=coustmer.getDuration()
                    s=int(dur)+int(input("Enter How many months do u want to be extend membership:"))
                    res=str(s)
                    coustmer.setDuration(res)
                    print("*****Updated Successfully******")
        elif extent == str('revoke'):
            for customer_id in Gym_memberships.coustmer_data.keys():
                customer=Gym_memberships.coustmer_data[customer_id]
                if customer_id==ck_phone:
                    coustmer.setDuration('0')
                    print("Membership Revoked")

    elif option == 5:
        ck_phone=input("Enter Phone Number of the member you want to create Regimen :")
        for i in Gym_memberships.regimen:
            if i==ck_phone:
               for j in Gym_memberships.regimen[i]:
                   Gym_memberships.regimen[i][j]=input(j+":")  # mark1

    
    elif option == 6:
        ck_phone=input("Enter Phone Number to View Regimen")
        for i in Gym_memberships.regimen:
            if i==ck_phone:
                for key, val in Gym_memberships.regimen[i].items():
                    print(key,":",val)
        print("\n")

    elif option == 7:
        ck_phone=input("Enter Phone Number to  Delete Regimen")
        for i in Gym_memberships.regimen:
            if i==ck_phone:
                print("Workout regimen deleted !!!")

        Gym_memberships.regimen.pop(ck_phone)
        print("\n")
    
    elif option == 8:
        ck_phone=input("Enter Phone number of the member to update regimen : ")
        for i in Gym_memberships.regimen:
            if i==ck_phone:
                d=input("Enter the day which u want to Update: ")
                for j in Gym_memberships.regimen[i]:
                    if j==d:
                        Gym_memberships.regimen[i][j]=input("Enter the workout: ")
                        print("Updated Successfully !!!")
        print("\n")
    
    elif option == 0:
        break

    else:
        print("Please Enter the Valid number")
    menu()


def MemberPortal():
    print("\n ********* MemberPortal**********")
    print("1. My Regimen")
    print("2. My Profile")
    print("3. Exit")
    print("\n Enter your choice")
MemberPortal()

while True:
    option=int(input())
    if option == 1:
        p=input("Enter your phone_number to view Regimen: ")
        print("** --Your Regimen Based on Your BMI--  **")
        for i in Gym_memberships.regimen:
            if i == p:
                for key,val in Gym_memberships.regimen[i].items():
                    print(key,":",val)
        print("\n")

    elif option == 2:
        p = input("Enter Enter your phone_number to view Profile.: ")
        try:
            for i in Gym_memberships.coustmer_data.keys():
                if i == p:
                    customer = Gym_memberships.coustmer_data[i]
                    name=customer.getName()
                    age=customer.getAge()
                    gender=customer.getGender()
                    Phone_no=customer.getPhone()
                    email=customer.getEmail()
                    bmi=customer.getBmi()
                    duration=customer.getDuration()
                    print("****PROFILE****")
                    print(" Name: {}\n Age : {} \n gender: {} \n Phone_no: {} \n Email: {} \n bmi: {}\n Duration: {}\n".format(name,age,gender,Phone_no,email,bmi,duration))
        except:
            print("No User with this phone Number exist")

    elif option == 3:
        break

    else:
        print("Enter valid key ")
    MemberPortal()