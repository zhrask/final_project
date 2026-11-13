




def search_pet(pets:list)->list:
    search_menu = input("1.search by owner name 2.search by number")
    match search_menu:
        case "1":
            name_search = input("name:")
            if pets:
                for i in range(len(pets)):
                    if pets[i][1] == name_search.title():
                        print("name has been found.")
                        print(pets[i])
                        break
                else:
                    print("no pets found.")
            else:
                print("no pets yet.")
        case "2":
            num_search = int(input("number:"))
            if pets:
                if 1 <= num_search <= len(pets):
                    print(pets[num_search - 1])
                else:
                    print("no pets found.")
            else:
                print("no pets yet.")