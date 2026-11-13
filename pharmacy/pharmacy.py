




from delete import *
from show import *
from search import *
from edit import *

customer = []


while True:
    main_menu = input("1.add customer  2.delete   3.search   4.edit   5.show  6.exit")
    while True:
        match main_menu:
            case "1":
                first_name = input("first name:")
                last_name = input("last name:")
                doctor = input("doctor name:")

                medicines = []
                final_price = 0

                while True:
                    medicine = input("medicine name(after last medicine type end):")
                    if medicine == "end":
                        break
                    price = int(input("medicine price:"))
                    price_tax = price * 1.1
                    final_price += price_tax
                    medicines.append([medicine, price, price_tax])
                print("medicines added successfully.")
                customer.append([first_name, last_name, doctor,medicines, final_price])
                break
            case "2":
                delete(customer, medicines)
                break
            case "3":
                search(customer)
                break
            case "4":
                edit(customer)
                break
            case "5":
                show(customer)
                break
            case "6":
                print("thanks for choosing us.")
                break
