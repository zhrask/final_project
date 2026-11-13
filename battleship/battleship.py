






while True:
    main_menu = input("battle ship game(1.play with computer  2.play with another player  3.exit)")
    match main_menu:
        case "1":
            board = []#safhe bazi 10 *10
            for i in range(10):#radif ha
                radif = []
                for j in range(10):#sotun ha
                    radif.append("-") #10 ta radif misazam amma kenare hm nistn pas b board batyad bebrmeshun
                board.append(radif)
            for i in range(10):
                for j in range(10):
                    print(board[i][j], end="  ")
                print()
            number_ships = int(input("how many ships to strt:"))
            for i in range(number_ships):
                while True:
                    radif_ship = int(input("radife kashtie shoma:"))
                    sotun_ship = int(input("sotune kashtie shoma:"))
                    if 0 <= radif_ship <=9 and 0<= sotun_ship <= 9:
                        if board[radif_ship][sotun_ship] == "-":
                            board[radif_ship][sotun_ship] = "s2"
                            for i in range(10):
                                for j in range(10):
                                    print(board[i][j], end="  ")
                                print()
                            break
                        else:
                            print("in khane por ast.")
                    else:
                        print("radif va sotun beine 0-9 bashad")
            import random
            computer_board = []#safhe joda baraye computer
            for i in range(10):
                radif = []
                for j in range(10):
                    radif.append("-")
                computer_board.append(radif)
            for i in range(10):
                for j in range(10):
                    print(computer_board[i][j], end="  ")
                print()
            for i in range(number_ships):
                while True:
                    radif_ship_computer = random.randint(0,9)
                    sotun_ship_computer = random.randint(0,9)
                    if computer_board[radif_ship_computer][sotun_ship_computer] == "-":
                        computer_board[radif_ship_computer][sotun_ship_computer] = "c2"
                        for i in range(10):
                            for j in range(10):
                                print(computer_board[i][j], end="  ")
                            print()
                        break
            while True:
                while True:
                    shoot_radif = int(input("radife shelik:"))
                    shoot_sotun = int(input("sotune shelik:"))
                    if 0 <= shoot_radif <=9 and 0<= shoot_sotun <= 9:
                        if computer_board[shoot_radif][shoot_sotun] == "*" or computer_board[shoot_radif][shoot_sotun] == "o": #khune morde ya miss shot nzne
                            continue #player mokhtasat jadid besze
                        if computer_board[shoot_radif][shoot_sotun] == "c2":
                            computer_board[shoot_radif][shoot_sotun] = "c1"
                            print("hit.")
                            for i in range(10):
                                for j in range(10):
                                    print(computer_board[i][j], end="  ")
                                print()
                            break
                        elif computer_board[shoot_radif][shoot_sotun] == "c1":
                            computer_board[shoot_radif][shoot_sotun] = "*"
                            print("killed.")
                            for i in range(10):
                                for j in range(10):
                                    print(computer_board[i][j], end="  ")
                                print()
                            break
                        else:
                            computer_board[shoot_radif][shoot_sotun] = "o"
                            print("miss shot!")
                            break
                    else:
                        print("shomare radif o sotun 0-9 bashad.")
                computer_ships = 0 #tedade ship haye daraye june computer
                for i in range(10):
                    for j in range(10):
                        if computer_board[i][j] == "c2" or computer_board[i][j] == "c1":
                            computer_ships += 1
                if computer_ships == 0: 
                    print("You win!")
                    break



            #agar ba methode all() benevism
                #if all(computer_board[i][j] != "c2" and computer_board[i][j] != "c1"
                #    for i in range(10) for j in range(10)):
                #    print("you win!")
                #    break
                while True:
                    shoot_radif_computer = random.randint(0,9)
                    shoot_sotun_computer = random.randint(0,9)
                    if board[shoot_radif_computer][shoot_sotun_computer] == "*" or board[shoot_radif_computer][shoot_sotun_computer] == "o": #khune morde ya miss shot nzne
                        continue #computer mokhtasat jadid besze
                    else:
                        if board[shoot_radif_computer][shoot_sotun_computer] == "s2":#har ship 2jun dre k yedunsh km beshe
                            board[shoot_radif_computer][shoot_sotun_computer] = "s1"
                            print("shoot.")
                            for i in range(10):
                                for j in range(10):
                                    print(board[i][j], end="  ")
                                print()
                            break
                        elif board[shoot_radif_computer][shoot_sotun_computer] == "s1":
                            board[shoot_radif_computer][shoot_sotun_computer] = "*"#ship dead
                            print("died.")
                            for i in range(10):
                                for j in range(10):
                                    print(board[i][j], end="  ")
                                print()
                            break
                        else:
                            board[shoot_radif_computer][shoot_sotun_computer] = "o" #khune miss shod khali bud
                            print("miss shot!")
                            break
                player_ships = 0 #tedade ship haye daraye june player
                for i in range(10):
                    for j in range(10):
                        if board[i][j] == "s2" or board[i][j] == "s1":
                            player_ships += 1
                if player_ships == 0: 
                    print("You lose!")
                    break


                #agar ba methode all() benevism
                #if all(board[i][j] != "s2" and board[i][j] != "s1"
                #    for i in range(10) for j in range(10)):
                #    print("you lose.!")
                #    break
        case "2":
            board_player1 = []#safhe bazi 10 *10 player1
            for i in range(10):#radif ha
                radif = []
                for j in range(10):#sotun ha
                    radif.append("-") #10 ta radif misazam amma kenare hm nistn pas b board batyad bebrmeshun
                board_player1.append(radif)
            for i in range(10):
                for j in range(10):
                    print(board_player1[i][j], end="  ")
                print()
            number_ships = int(input("how many ships to strt:"))
            for i in range(number_ships):
                while True:
                    radif_ship = int(input("radife kashtie shoma:"))
                    sotun_ship = int(input("sotune kashtie shoma:"))
                    if 0 <= radif_ship <=9 and 0<= sotun_ship <= 9:
                        if board_player1[radif_ship][sotun_ship] == "-":
                            board_player1[radif_ship][sotun_ship] = "s2"
                            for i in range(10):
                                for j in range(10):
                                    print(board_player1[i][j], end="  ")
                                print()
                            break
                        else:
                            print("in khane por ast.")
                    else:
                        print("radif va sotun beine 0-9 bashad")
                    
            board_player2 = []#safhe bazi 10 *10 player2
            for i in range(10):#radif ha
                radif = []
                for j in range(10):#sotun ha
                    radif.append("-") #10 ta radif misazam amma kenare hm nistn pas b board batyad bebrmeshun
                board_player2.append(radif)
            for i in range(10):
                for j in range(10):
                    print(board_player2[i][j], end="  ")
                print()
            number_ships = int(input("how many ships to strt:"))
            for i in range(number_ships):
                while True:
                    radif_ship = int(input("radife kashtie shoma:"))
                    sotun_ship = int(input("sotune kashtie shoma:"))
                    if 0 <= radif_ship <=9 and 0<= sotun_ship <= 9:
                        if board_player2[radif_ship][sotun_ship] == "-":
                            board_player2[radif_ship][sotun_ship] = "c2"
                            for i in range(10):
                                for j in range(10):
                                    print(board_player2[i][j], end="  ")
                                print()
                            break
                        else:
                            print("in khane por ast.")
                    else:
                        print("radif va sotun beine 0-9 bashad")
            
            while True: #shellikha
                print("player 1 turn:")
                while True:
                    shoot_radif_player1 = int(input("radife shelik:"))
                    shoot_sotun_player1 = int(input("sotune shelik:"))
                    if 0 <= shoot_radif_player1 <=9 and 0<= shoot_sotun_player1 <= 9:
                        if board_player2[shoot_radif_player1][shoot_sotun_player1] == "*" or board_player2[shoot_radif_player1][shoot_sotun_player1] == "o": #khune morde ya miss shot nzne
                            continue #player mokhtasat jadid besze
                        if board_player2[shoot_radif_player1][shoot_sotun_player1] == "c2":
                            board_player2[shoot_radif_player1][shoot_sotun_player1] = "c1"
                            print("hit.")
                            for i in range(10):
                                for j in range(10):
                                    print(board_player2[i][j], end="  ")
                                print()
                            break
                        elif board_player2[shoot_radif_player1][shoot_sotun_player1] == "c1":
                            board_player2[shoot_radif_player1][shoot_sotun_player1] = "*"
                            print("killed.")
                            for i in range(10):
                                for j in range(10):
                                    print(board_player2[i][j], end="  ")
                                print()
                            break
                        else:
                            board_player2[shoot_radif_player1][shoot_sotun_player1] = "o"
                            print("miss shot!")
                            break
                    else:
                        print("shomare radif o sotun 0-9 bashad.")
                player2_ships = 0 #tedade ship haye daraye june player2
                for i in range(10):
                    for j in range(10):
                        if board_player2[i][j] == "c2" or board_player2[i][j] == "c1":
                            player2_ships += 1
                if player2_ships == 0: 
                    print("player1 wins!")
                    break


                #agar ba methode all() benevism
                #if all(board_player2[i][j] != "c2" and board_player2[i][j] != "c1"
                #    for i in range(10) for j in range(10)):
                #    print("player1 wins!")
                #    break

                print("player2 turn:")
                while True:
                    shoot_radif_player2 = int(input("radife shelik:"))
                    shoot_sotun_player2 = int(input("sotune shelik:"))
                    if 0 <= shoot_radif_player2 <=9 and 0<= shoot_sotun_player2 <= 9:
                        if board_player1[shoot_radif_player2][shoot_sotun_player2] == "*" or board_player1[shoot_radif_player2][shoot_sotun_player2] == "o": #khune morde ya miss shot nzne
                            continue #player mokhtasat jadid besze
                        if board_player1[shoot_radif_player2][shoot_sotun_player2] == "s2":
                            board_player1[shoot_radif_player2][shoot_sotun_player2] = "s1"
                            print("hit.")
                            for i in range(10):
                                for j in range(10):
                                    print(board_player1[i][j], end="  ")
                                print()
                            break
                        elif board_player1[shoot_radif_player2][shoot_sotun_player2] == "s1":
                            board_player1[shoot_radif_player2][shoot_sotun_player2] = "*"
                            print("killed.")
                            for i in range(10):
                                for j in range(10):
                                    print(board_player1[i][j], end="  ")
                                print()
                            break
                        else:
                            board_player1[shoot_radif_player2][shoot_sotun_player2] = "o"
                            print("miss shot!")
                            break
                    else:
                        print("shomare radif o sotun 0-9 bashad.")
                player1_ships = 0 #tedade ship haye daraye june player1
                for i in range(10):
                    for j in range(10):
                        if board_player1[i][j] == "s2" or board_player1[i][j] == "s1":
                            player1_ships += 1
                if player1_ships == 0: 
                    print("player2 wins!")
                    break

                #agar ba methode all() benevism
                #if all(board_player1[i][j] != "s2" and board_player1[i][j] != "s1"
                #    for i in range(10) for j in range(10)):
                #    print("player2 wins!")
                #    break
                
            
        case "3":
            print("byeee.")
            break