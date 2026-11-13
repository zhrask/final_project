





def edit(customer:list)->list:
    edit_menu = input("1.edit customer info    2.edit medicine ")
    match edit_menu:
        case "1":
            if customer:
                while True:
                    edit_num = int(input("shomare radifi k mikhahid edit konid:"))
                    if 1 <= edit_num <= len(customer):
                        customer_edit_menu = input("1.edit first name    2.edit last name   3.edit doctor name   4.finish editting")
                        match customer_edit_menu:
                            case "1":
                                new_first_name = input("new first name:")
                                customer[edit_num - 1][0] = new_first_name
                            case "2":
                                new_last_name = input("new last name:")
                                customer[edit_num - 1][1] = new_last_name
                            case "3":
                                new_doctor = input("new doctor name:")
                                customer[edit_num - 1][2] = new_doctor
                            case "4":
                                break
                        print("changes save successfully.")
                    else:
                        print("shomare rdif yft nshod.")
            else:
                print("no customer yet.")

                
        case "2":
            if customer:
                edit_num = int(input("shomare radifi k mikhahid edit konid:"))
                if 1 <= edit_num <= len(customer):
                    medicines = customer[edit_num - 1][3]
                    if medicines:
                        for i in range(len(medicines)):
                            print(i +1, medicines[i][0])
                            medicines_edit_num = int(input("shomare rdife medicine k mikhahid edit konid"))
                            if 1 <= medicines_edit_num <= len(medicines):
                                while True:
                                    medicine_edit_menu = input("1.edite medicine name   2.edit medicine price    3.finish editting")
                                    match medicine_edit_menu:
                                        case "1":
                                            new_medicine_name = input("new medicine name:")
                                            medicines[medicines_edit_num - 1][0] = new_medicine_name
                                        case "2":
                                            new_medicine_price = int(input("new medicine price:"))
                                            medicines[medicines_edit_num - 1][1] = new_medicine_price
                                            medicines[medicines_edit_num - 1][2] = new_medicine_price * 1.1
                                            final_price = 0
                                            for i in range(len(medicines)):
                                                final_price += medicines[i][2]
                                                customer[edit_num - 1][4] = final_price
                                        case "3":
                                            break
                                    print("changes save successfully.")
                            else:
                                print("shomare radife medicine yaft nshod.")
                    else:
                        ("no medicine yet.")
            else:
                print("no customer yet.")
            