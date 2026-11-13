





def edit_pets(pets:list,edit:int)->list:
    edit_menu = input("1.pet name 2.owner name 3.species 4.nezhad 5.pet age 6.phone number 7.gender 8.weight 9.color")
    match edit_menu:
        case "1":
            edited_name = input("pet name:")
            if pets:
                if 1 <= edit <= len(pets):
                    if edited_name.strip() == "":
                            print("invalid name.")
                    else:
                        pets[edit - 1][0] = edited_name
                        print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")
        case "2":
            edited_owner = input("new owner:")
            if pets:
                if 1 <= edit <= len(pets):
                        for i in range(len(pets)):
                            if i != edit - 1 and edited_owner == pets[i][1]:
                                print("owner is alredy exist.")
                                break
                        else:
                            pets[edit - 1][1] = edited_owner
                            print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")
        case "3":
            edited_species = input("pet species:")
            if pets:
                if 1 <= edit <= len(pets):
                    if edited_species.strip() == "":
                            print("invalid species.")
                    else:
                        pets[edit - 1][2] = edited_species
                        print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")
        case "4":
            edited_nezhad = input("pet nezhad:")
            if pets:
                if 1 <= edit <= len(pets):
                    if edited_nezhad.strip() == "":
                            print("invalid nezhad.")
                    else:
                        pets[edit - 1][3] = edited_nezhad
                        print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")
        case "5":
            edited_age = input("pet age(month/year/day):")
            if pets:
                if 1 <= edit <= len(pets):
                    if edited_age.strip() == "":
                            print("invalid age.")
                    else:
                        pets[edit - 1][3] = edited_age
                        print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")
        case "6":
            edited_number = input("new number:")
            if pets:
                if 1 <= edit <= len(pets):
                    if len(edited_number) != 11 or edited_number.isdigit() != True:
                        print("wrong number.")
                    else:
                        for i in range(len(pets)):
                            if i != edit - 1 and edited_number == pets[i][1]:
                                print("number is alredy used.")
                                break
                        else:
                            pets[edit - 1][5] = edited_number
                            print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")
        case "7":
            edited_gender = input("pet gender(male/female):")
            if pets:
                if 1 <= edit <= len(pets):
                    if edited_gender.strip() == "":
                            print("invalid gender.")
                    else:
                        pets[edit - 1][6] = edited_gender
                        print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")
        case "8":
            edited_weight = float(input("weight(kg):"))
            if pets:
                if 1 <= edit <= len(pets):
                    if edited_weight.strip() == "":
                            print("invalid weight.")
                    else:
                        pets[edit - 1][3] = edited_weight
                        print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")
        case "9":
            edited_color = input("pet color:")
            if pets:
                if 1 <= edit <= len(pets):
                    if edited_color.strip() == "":
                            print("invalid color.")
                    else:
                        pets[edit - 1][8] = edited_color
                        print(pets[edit - 1])
                else:
                    print("number not found.")
            else:
                print("no pets yet.")