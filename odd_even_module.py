def show_menu():
     print("options:\n"
           "1)enter ten number:\n"
           "2)the list of add numbers:\n"
           "3)the list of even numbers:\n"
           "4)exit:\n")
     option = int(input("enter your option: "))
     return option

list_of_odd=[]
list_of_even=[]

def add_number():
    for i in range(1,10+1,1):
        number=int(input("enter your number: "))
        if number % 2 == 0:
            list_of_even.append(number)
        else:
            list_of_odd.append(number)

def odd_numbers():
    print("odd numbers is:",list_of_odd)
def even_numbers():
    print("even numbers is:",list_of_even)