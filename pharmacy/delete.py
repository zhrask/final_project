



def delete(customer:list, medicines:list)->None:
    main_delete_menu = input("1.delete customer and medicines    2.delete medicine  ")
    match main_delete_menu:
        case "1":
            customer_num = int(input("shomare radife customer baraye hazf:"))
            if customer:
                if 1 <= customer_num <= len(customer):
                    print(customer[customer_num - 1])
                    check_del = int(input("you sure you want to delete?(1.yes/2.no):"))
                    if check_del != 1 and check_del != 2:
                        print("try again.")
                        return
                    elif check_del == 1:
                        customer.pop(customer_num - 1)
                        print("customer deleted.")
                    elif check_del == 2:
                        print("delete canceled.")
                else:
                    print("shomare radif na mojud.")
            else:
                print("no customer yet.")

        case "2":
            customer_num = int(input("shomare radife customer baraye hazf:"))
            if customer:
                if 1 <= customer_num <= len(customer):
                    medicines = customer[customer_num - 1][3]
                    
                    if medicines:
                        for i in range(len(medicines)):
                            print(i + 1, medicines[i])
                        medicines_num = int(input("shomare radife medicines baraye hazf:"))
                        if 1 <= medicines_num <= len(medicines):
                            print(medicines[medicines_num - 1])
                            check_del = int(input("you sure you want to delete?(1.yes/2.no):"))
                            if check_del != 1 and check_del != 2:
                                print("try again.")
                                return
                            elif check_del == 1:
                                medicines.pop(medicines_num - 1)
                                print("medicines deleted.")
                                final_price = 0
                                for i in range(len(medicines)):
                                    final_price += medicines[i][2]
        
                                customer[customer_num - 1][4] = final_price
        
                            elif check_del == 2:
                                print("delete canceled.")
                        else:
                            print("shomare radife daru namojud.")
                    else:
                        print("medicines na mojud.")
                else:
                    print("shomare radif na mojud.")
            else:
                print("no customer yet.")