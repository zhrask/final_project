



def delete_pets(pets:list, appointments:list)->None:
    main_delete_menu = input("1.delete pet information    2.delete appointment")
    match main_delete_menu:
        case "1":
            delete_menu = input("1.delete by number   2.delete by owner name ")
            match delete_menu:
                case "1":
                    if pets:
                        num_delete = int(input("number:"))
                        if 1 <= num_delete <= len(pets):
                            print(pets[num_delete - 1])
                            check_del = int(input("you sure you want to delete?(1.yes/2.no):"))
                            if check_del != 1 and check_del != 2:
                                print("try again.")
                                return delete_pets
                            elif check_del == 1:
                                pets.pop(num_delete - 1)
                                appointments.pop(num_delete - 1)
                                print("pet and appointment deleted.")
                            elif check_del == 2:
                                print("delete canceled.")
                        else:
                            print("shomare radif na mojud.")
                    else:
                        print("no pets yet.")
                case "2":
                    name_delete = input("owner name:")
                    if pets:
                        for i in range(len(pets)):
                            if pets[i][1] == name_delete.title():
                                print(pets[i])
                                check_del = int(input("you sure you want to delete?(1.yes/2.no):"))
                            if check_del != 1 and check_del != 2:
                                print("try again.")
                                return delete_pets
                            elif check_del == 1:
                                pets.pop(i)
                                appointments.pop(i)
                                print("pet and appointment deleted.")
                            elif check_del == 2:
                                print("delete canceled.")
                        else:
                            print("shomare radif na mojud.")
                    else:
                        print("no pets yet.")
        case "2":
            delete_menu = input("1.delete by number   2.delete by owner name ")
            match delete_menu:
                case "1":
                    if appointments:
                        num_delete = int(input("number:"))
                        if 1 <= num_delete <= len(appointments):
                            print(appointments[num_delete - 1])
                            check_del = int(input("you sure you want to delete?(1.yes/2.no):"))
                            if check_del != 1 and check_del != 2:
                                print("try again.")
                                return delete_pets
                            elif check_del == 1:
                                appointments.pop(num_delete - 1)
                                print("appointment deleted.")
                            elif check_del == 2:
                                print("delete canceled.")
                        else:
                            print("shomare radif na mojud.")
                    else:
                        print("no pets yet.")
                case "2":
                    name_delete = input("pet name:")
                    if appointments:
                        for i in range(len(appointments)):
                            if appointments[i][0] == name_delete.title():
                                print(appointments[i])
                                check_del = int(input("you sure you want to delete?(1.yes/2.no):"))
                            if check_del != 1 and check_del != 2:
                                print("try again.")
                                return delete_pets
                            elif check_del == 1:
                                appointments.pop(delete - 1)
                                print("appointment deleted.")
                            elif check_del == 2:
                                print("delete canceled.")
                        else:
                            print("shomare radif na mojud.")
                    else:
                        print("no pets yet.")

