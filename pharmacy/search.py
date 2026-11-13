





def search(customer:list)->list:
    search_menu = input("1.search by last name 2.search by number radif")
    match search_menu:
        case "1":
            name_search = input("last name:")
            if customer:
                for i in range(len(customer)):
                    if customer[i][1] == name_search:
                        print("name has been found.")
                        print(customer[i])
                        break
                else:
                    print("no customer found.")
            else:
                print("no customer yet.")
        case "2":
            num_search = int(input("number:"))
            if customer:
                if 1 <= num_search <= len(customer):
                    print(customer[num_search - 1])
                else:
                    print("no customer found.")
            else:
                print("no customer yet.")