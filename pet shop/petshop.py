





from show import*
from search import *
from edit import *
from delete import *

vacsan = []
appointments = []
pets = []
while True:
    main_menu = input("1.register new pet   2.show all pets   3.search pet   4.edit informaition   5.delete pet   6.vaccination   7.exit")
    while True:
        match main_menu:
            case "1":
                pet_name = input("your pet name:")
                if pet_name.isalpha() != True:
                    print("try again.")
                    break
                else:
                    pet_name = pet_name.title()
                    print(pet_name, "accepted.")
                owner_name = input("your name:")
                if owner_name.isalpha() != True:
                    print("try again.")
                    break
                else:
                    owner_name = owner_name.title()
                    print(owner_name, "accepted.")
                species = input("gune pet shoma:")
                print(species, "accepted.")
                nezhad = input("nezhade pet shoma:")
                print(nezhad, "accepted.")
                age = int(input("your pet age:"))
                age_menu = input("1.day 2.month 3.year")
                match age_menu:
                    case "1":
                        pet_age = str(age) + "days"
                        print(pet_age, "accepted.")
                        
                    case "2":
                        pet_age = str(age) + "months"
                        print(pet_age, "accepted.")
                        
                    case "3":
                        pet_age = str(age) + "years"
                        print(pet_age, "accepted.")
                        
                phone_number = input("phone number:")
                if len(phone_number) != 11 or phone_number.isnumeric() != True or phone_number.startswith("09") != True:
                    print("lotfn shomare hamrahe 11 rqmi ba 09- vared konid.")
                    break
                else:
                    print(phone_number, "accepted.")
                gender_menu = input("1.male 2.female")
                match gender_menu:
                    case "1":
                        gender = "male"
                        print("male. accepted")
                    case "2":
                        gender = "female"
                        print("female. accepted")
                weight_num = float(input("your pet weight(kg):"))
                weight = str(weight_num) + " kg"
                print(weight, "accepted.")
                color = input("your pet color:")
                if color.isalpha() != True:
                    print("try again.")
                    break
                else:
                    print(color, "accepted.")
                doctor_names = ["ahmadi", "musavi", "salehzade"]
                doctor = int(input("aya dampezeshke khassi made nzr drid?(1.ble 2.kheir):"))
                if doctor != 1 and doctor != 2:
                    print("try again.")
                doctor = doctor == 1
                import random
                doctor_name = random.choice(doctor_names)
                print("yeki az behtrin dampezeshk haye ma baraye shoma:", doctor_name)
                if doctor == True: 
                    doctor_name = input("name dmpezeshke made nzr shoma(dr.ahmadi, dr.musavi, dr.salehzade):") 
                    if doctor_name not in doctor_names:
                        print("try again.")
                        break
                    else:
                        print("dampezeshke shoma", doctor_name)
                ellat_morajee = input("ellate morajee shoma:")
                appointment_date = input("ruze madde nzr baraye morajee(year14--/month/day):")
                for i in range(len(appointments)):
                    if appointment_date == appointments[i][4]:
                        print("in ruz rezerv shode ast.")
                        break
                    else:
                        print(appointment_date, "accepted.")
                appointments.append([pet_name, owner_name, doctor_name, ellat_morajee, appointment_date])
                pets.append([pet_name, owner_name,species, nezhad, pet_age, phone_number, gender, weight, color, "pending appointment"])
                break
            case "2":
                show_pet(pets, appointments)
                break
            case "3":
                search_pet(pets)
                break
            case "4":
                shomare_radif_edit = int(input("shomare radife peti k mikhahid edit konid:"))
                edit_pets(pets, shomare_radif_edit)
                break
            case "5":
                delete_pets(pets, appointments)
                break
            case "6":
                vaccination_menu = input("1. add new vacsan   2.show vaccination history   3.delete vacsan   4.exit")
                match vaccination_menu:
                    case "1":
                        pet_name = input("pet name:")
                        owner_name = input("owner name:")
                        if pets:
                            for i in range(len(pets)):
                                if pets[i][0] == pet_name.title() and pets[i][1] == owner_name.title():
                                    vacsan_name = input("vacsan name:")
                                    vacsan_date = input("vacsan date(year/month/day):")
                                    vacsan.append([pet_name, owner_name,vacsan_name,vacsan_date])
                                    print("vacsan afzude shod.")
                                    break
                            else:
                                print("pet and owner not found.")
                                break
                        else:
                            print("no pets yet.")
                            break
                    case "2":
                        if vacsan:
                            for i in range(len(vacsan)):
                                print("pet name:", vacsan[i][0])
                                print("owner:", vacsan[i][1])
                                print("vacsan name:", vacsan[i][2])
                                print("vacsan date:", vacsan[i][3])
                                print("-------------------------")
                            break
                        else:
                            print("vacsani sabt nshode.")
                            break
                    case "3":
                        delete_vacsan = input("pet name or owner name:")
                        if vacsan:
                            for i in range(len(vacsan)):
                                if delete_vacsan == vacsan[i][0] or vacsan[i][1]:
                                    print(vacsan[i])
                                    check_del = int(input("you sure you want to delete?(1.yes/2.no):"))
                                    if check_del != 1 and check_del != 2:
                                        print("try again.")
                                        break
                                    elif check_del == 1:
                                        vacsan.pop(vacsan[i])
                                        print("vacsan deleted.")
                                    elif check_del == 2:
                                        print("delete canceled.")
                                    else:
                                        print("pet or owner not available")
                            break
                        else:
                            print("no vacsan yet.")
                            break
                    case "4":
                        break
            case "7":
                print("thanks for choosing us.")
                break





