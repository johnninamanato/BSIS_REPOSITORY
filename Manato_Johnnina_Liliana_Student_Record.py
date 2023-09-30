#Manato, Johnnina Liliana
#Marayag, Elisha 
import os
os.system('cls')
from main import*

sms=student_management_system()

def display_menu():
    os.system("cls")
    print("---------------------------------------")
    print("=== Student Database Management System ===")
    print("---------------------------------------")
    print("Press 1. To Add New Student")
    print("Press 2. To View Students List")
    print("Press 3. To Search for Student's Record")
    print("Press 4. To Update Student")
    print("Press 5. To Delete Student")
    print("Press 6. To exit the system")
while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        sms.add_student()
    elif choice == '2':
        sms.view_students()
    elif choice == '3':
        sms.search_student()
    elif choice == '4':
        sms.update_student()
    elif choice == '5':
        sms.delete_student()
    elif choice == 6:
            print("THANK YOU !")
            run = False
    else:
            print("\n")

    return_to_main = input("Would you like to go back to the menu? Type 'yes' to proceed or 'no' to exit: ")
    if return_to_main != 'yes':
                break

    print 
    display_menu()
        

"""
else: 
        exit() != 'no'
    """