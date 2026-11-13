





def show(customer:list)->list:
    if customer:
        for i in range(len(customer)):
            print(i +1, ".", customer[i])
            print("---------------------")
    else:
        print("no customer yet.")