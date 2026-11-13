





def show_pet(pets:list, appointments:list)->list:
    if pets:
        for i in range(len(pets)):
            print(i+1, ".", pets[i][0:10])
            if appointments:
                for i in range(len(appointments)):
                    print("doctor:", appointments[i][2], "/ellate morajee:", appointments[i][3], "/time morajee:", appointments[i][4])
                print("--------------")
            else:
                print("no appointments.")
    else:
        print("no pets yet.")