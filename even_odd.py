from odd_even_module import *
while True:
    choice = show_menu()
    print("*" * 30)

    if choice==1:
        add_number()
        print("*"*30)
    elif choice==2:
        odd_numbers()
        print("*"*30)
    elif choice==3:
        even_numbers()
        print("*"*30)
    elif choice==4:
        print("bye")
        break
    else:
        print("Invalid numbers")

