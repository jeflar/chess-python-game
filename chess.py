#Lar, Jeff Emerson F.
#chess.played
#This is a game of chess which can be played by two-players. 
#The player whose turn it is to move is in check and has no legal move to escape check would be considered checkmate and the game is over.

#1.1 ; 2.1 - PAWN
#1.2 ; 2.2 - ROOK
#1.3 ; 2.3 - HORSE
#1.4 ; 2.4 - BISHOP
#1.5 ; 2.5 - QUEEN
#1.6 ; 2.6 - KING
#0         - EMPTY SPACE

#in game board that would be displayed in the program
board = [["","1","2","3","4","5","6","7","8",""]
        ,["1",2.2,2.3,2.4,2.5,2.6,2.4,2.3,2.2,"1"]
        ,["2",2.1,2.1,2.1,2.1,2.1,2.1,2.1,2.1,"2"]
        ,["3",0,0,0,0,0,0,0,0,"3"]
        ,["4",0,0,0,0,0,0,0,0,"4"]
        ,["5",0,0,0,0,0,0,0,0,"5"]
        ,["6",0,0,0,0,0,0,0,0,"6"]
        ,["7",1.1,1.1,1.1,1.1,1.1,1.1,1.1,1.1,"7"]
        ,["8",1.2,1.3,1.4,1.5,1.6,1.4,1.3,1.2,"8"]
        ,["","1","2","3","4","5","6","7","8",""]]

#list of in game data needed to run the program
scores = []
whitepieces = [1.1,1.2,1.3,1.4,1.6,1.5]
blackpieces = [2.1,2.2,2.3,2.4,2.6,2.5]
allpieces = [1.1,1.2,1.3,1.4,1.5,1.6,2.1,2.2,2.3,2.4,2.5,2.6]
allpieces_noking = [1.1,1.2,1.3,1.4,1.5,2.1,2.2,2.3,2.4,2.5]
allpieces_str = ["1.1","1.2","1.3","1.4","1.6","1.5","2.1","2.2","2.3","2.4","2.6","2.5"]
valid_choices = ["1","2","3","4","5","6","7","8"]
gridboard = ["","1","2","3","4","5","6","7","8"]
#game_stats[0] contains the player num
#game_stats[1] contains the player no of moves in white
#game_stats[2] contains the player no of moves in black
#game_stats[3:7] contains if the player can castle 
game_stats = ["2","1","0","w_rightcastle","w_leftcastle","b_rightcastle","b_leftcastle"]

#prints the menu and asks for the input of the user (new game,load game,view highscores,exit)
def menu():
    while True:
        #menu
        print(" ---------------------------------------- ")
        print("|  Hello Players! This is a chess game.  |")
        print(" ----------------------------------------")
        print("     --------------------------------")
        print("    |   1   |   New Game     |   1   |")
        print("    |--------------------------------|")
        print("    |   2   |   Load Game    |   2   |")
        print("    |--------------------------------|")
        print("    |   3   |   HighScores   |   3   |")
        print("    |--------------------------------|")
        print("    |   4   |   Exit         |   4   |")
        print("     -------------------------------")
        print("Note: This program automatically saves the game every turn so feel free to quit when you are tired.")
        print("Note: To exit the program during in game just enter \"exit\" .")
        print("")
        a=0
        scores.clear()
        hs = 0
        load(hs)
        #converts all score moves to integer for proper sorting
        for x in scores:
            nums = int(x[0])
            scores[a][0] = nums
            a += 1
        scores.sort()
        game = input("Please enter your choice:  ")
        if game == "1":
            printboard()
        elif game == "2":
            hs = 1
            #loads all data in text file
            load(hs)
            printboard()
        elif game == "3":
            #when there are no scores in the list then it is empty
            if scores == []:
                print("There are no scores in the saved file")
                continue
            a=1
            print("     --------------------------------------------")
            print("   /| Ranking |   Name   |    Number of Moves    |")
            print("  / |--------------------------------------------|")
            #load all the ones in the text file and sorts them with least number of moves in number 1
            #top 10 are only included in the game
            for i in scores:
                #different spaces to print due to different numbers
                #i[1]- name of the player; i[0]- score of the player
                if a == 10:
                    if int(i[0] > 99):
                        print(" |  |   "+str(a),"   |  ",i[1],"  |""         ",i[0],"         |")                            
                    elif int(i[0]) > 9:
                        print(" |  |   "+str(a),"   |  ",i[1],"  |""         ",i[0],"          |")
                    else:
                        print(" |  |   "+str(a),"   |  ",i[1],"  |""          ",i[0],"          |")  
                else:
                    if int(i[0] > 99):
                        print(" |  |    "+str(a),"   |  ",i[1],"  |""         ",i[0],"         |")
                    elif int(i[0]) > 9:
                        print(" |  |    "+str(a),"   |  ",i[1],"  |""         ",i[0],"          |")    
                    else:
                        print(" |  |    "+str(a),"   |  ",i[1],"  |""          ",i[0],"          |")	
                    a += 1
                print(" |  |--------------------------------------------|")
            print(" | /                                            /")
            print("  ----------------------------------------------")
        elif game == "4":
            print("     ---------------------")
            print("    | \    THANK YOU    / |")
            print("    |  \  FOR PLAYING  /  |")
            print("    |   ---------------   |")
            print("    |  /      GOOD     \  |")
            print("    | /       BYE!      \ |")
            print("     ---------------------")
            exit()
        else:
            print("Invalid Choice")
    
#currentplayer,prints the board, checks if pawnpromotion, checks if checkmate, saves to the file every turn
def printboard():
    game = True
    #replaces game_stats[0:3] into int
    game_stats[0] = int(game_stats[0])
    game_stats[1] = int(game_stats[1])
    game_stats[2] = int(game_stats[2])
    white_moves = game_stats[1]
    black_moves = game_stats[2]
    player = game_stats[0]
    game_stats[0] = player 
    #if there is pawnpassant in game_stats then replaces the number of it into int
    if "pawnpassant" in game_stats:
        game_stats[-1] = int(game_stats[-1])
    #prints the board and determines the current player
    while game:
        game_stats[1] = white_moves 
        game_stats[2] = black_moves
        noplayer = playernumber(player)
        #puts who is the current player's turn in game_stats[0]
        if noplayer == 1:
            game_stats[0] = 2
        elif noplayer == 2:
            game_stats[0] = 1
        #interface printing of the board
        for x in range(10):
            if x%1==0 and x != 0:
                if x == 1:
                    print("___|____|____|____|____|____|____|____|____|___")
                elif x == 9:
                    print("___|____|____|____|____|____|____|____|____|___")
                    print("   |    |    |    |    |    |    |    |    |   ")
                else:
                    print("___|____|____|____|____|____|____|____|____|___")
            for y in range(10):
                pieces(x,y)
            print()
        #if white pawn reached row 1 or black pawn reached row 8 then pawn would be promoted
        if pawnpromotion():
            for x in range(10):
                if x%1==0 and x != 0:
                    if x == 1:
                        print("___|____|____|____|____|____|____|____|____|___")
                    elif x == 9:
                        print("___|____|____|____|____|____|____|____|____|___")
                        print("   |    |    |    |    |    |    |    |    |   ")
                    else:
                        print("___|____|____|____|____|____|____|____|____|___")
                for y in range(10):
                    pieces(x,y)
                print()
        #saves the current state of the board,details of game_stats,highscores into the text file every turn
        save()
        player += 1
        #checkmate checker
        if noplayer == 1:
            #checks if there is a possible move for white
            if checkmate(noplayer):
                #checks if white is checked
                if checking(noplayer) == False:
                    print("              ---------------------")
                    print("             |      Checkmate!     |")
                    print("             |---------------------|")
                    print("             |     Black Wins!!!   |")
                    print("              ---------------------")
                    if highscore(noplayer):
                        save()
                        exit()
                #if not checked then the game is a draw or stalemate
                else:
                    print("              ---------------------")
                    print("             |        Draw!!       |")
                    print("              --------------------- ")
                    save()
                    exit()
            else:
                #checks if the player is checked
                if checking(noplayer) == False:
                    print("              ---------------------")
                    print("             |        Check!       |")
                    print("              --------------------- ")
                #incrementing the number of moves
                black_moves += 1
                print("              ---------------------")
                print("             |     White's Turn    |")
                print("              --------------------- ")
        elif noplayer == 2:
            #checks if there is a possible move for black
            if checkmate(noplayer):
                #checks if black is checked
                if checking(noplayer) == False:
                    print("              ---------------------")
                    print("             |      Checkmate!     |")
                    print("             |---------------------|")
                    print("             |     White Wins!!!   |")
                    print("              ---------------------")
                    if highscore(noplayer):
                        save()
                        exit()
                #if not checked then it is a draw or stalemate
                else:
                    print("              ---------------------")
                    print("             |        Draw!!       |")
                    print("              --------------------- ")
                    save()
                    exit()
            else:
                #checks if black is checked
                if checking(noplayer) == False:
                    print("              ---------------------")
                    print("             |        Check!       |")
                    print("              --------------------- ")
                #increment for number of moves
                white_moves += 1
                print("              ---------------------")
                print("             |     Black's Turn    |")
                print("              --------------------- ")
        #asks for the move of the player
        move(noplayer)

#replaces the numbers on the board with appropriate chess pieces
def pieces(x,y):
    if board[x][y] == 0:
        print("    ",end = "|")
    elif board[x][y] == 1.1:
        print(" wP ",end = "|")       
    elif board[x][y] == 1.2:
        print(" wR ",end = "|")
    elif board[x][y] == 1.3:
        print(" wH ",end = "|")
    elif board[x][y] == 1.4:
        print(" wB ",end = "|")
    elif board[x][y] == 1.5:
        print(" wQ ",end = "|")
    elif board[x][y] == 1.6:
        print(" wK ",end = "|")
    elif board[x][y] == 2.1:
        print(" bP ",end = "|")
    elif board[x][y] == 2.2:
        print(" bR ",end = "|")
    elif board[x][y] == 2.3:
        print(" bH ",end = "|")
    elif board[x][y] == 2.4:
        print(" bB ",end = "|")
    elif board[x][y] == 2.5:
        print(" bQ ",end = "|")
    elif board[x][y] == 2.6:
        print(" bK ",end = "|")
    elif y == 9:
        print(" "+str(board[x][y])+" ",end = " ")
    elif x == 9 and y ==0:
        print(" "+str(board[x][y])+"  ",end = "|")
    elif x == 0 or x == 9:
        print(" "+str(board[x][y])+"  ",end = "|")
    else:
        if y == 0:
            print(" "+str(board[x][y])+" ",end = "|")
        else:
            print(" "+str(board[x][y])+" ",end = " ")

#counter for player number    
def playernumber(player):
    player = (player % 2) + 1
    return player

#selects the row,col of the piece to be move and the row,col of the piece in where to move
def move(c):
    #ai is used for checkmate checker when true then the user is the one who is making the move
    ai = False
    move = True
    while move:
        print("     |-------------------------------")
        print("     |------Select your Piece       ")
        #piece selector and checks if it valid
        col_piece = input("     |Enter Column     ||  ") 
        col_piece = col_piece.upper()
        if col_piece == "EXIT":
        	exit()
        row_piece = input("     |Enter Row        ||  ") 
        row_piece = row_piece.upper()
        if row_piece == "EXIT":
        	exit()
        if col_piece in valid_choices and row_piece in valid_choices:
            col_piece = int(col_piece)
            row_piece = int(row_piece)
            #z is the current piece chosen by the user
            z = board[row_piece][col_piece]
            #checks if the chosen piece belongs to the player's turn
            good = checkpiece(c,z)
            if good:
                #if valid piece then chooses a place where to move
                print("     |-------Move to where? ")
                col_move = input("     |Enter Column     ||  ") 
                col_move = col_move.upper()
                if col_move == "EXIT":
                	exit()
                row_move = input("     |Enter Column     ||  ") 
                row_move = row_move.upper()
                if row_move == "EXIT":
                	exit()
                if col_move in valid_choices and row_move in valid_choices:
                    print("     |-------------------------------")
                    print("     |-------------------------------")
                    col_move = int(col_move)
                    row_move = int(row_move)
                    #runs the function depending on the piece chosen by the user
                    #takes in the piece chosen, desired location to move, if it is checkmate checker and current player
                    #if the move is valid and if there en passant in game_stats then removes it
                    if z == 1.1 or z == 2.1:
                        move = pawn(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == True:
                            #if the move of the pawn is not valid checks then it checks if the move is en passant 
                            move = passant(row_move,col_move,row_piece,col_piece,c)
                            #if en passant then it does the move and removes the possibility to en passant
                            if move == False:
                                game_stats.remove("pawnpassant")
                                game_stats.pop(-1)
                            else:
                                print("     |Invalid Choice") 
                        else:
                            #if valid move then removes en passant but when the move of the player is 2 spaces horizontally then it does not remove en passant
                            if ((z == 1.1 and row_move == row_piece-2) or (z == 2.1 and row_move == row_piece+2)) == False:
                                if "pawnpassant" in game_stats:
                                    game_stats.remove("pawnpassant")
                                    game_stats.pop(-1)
                    elif z == 1.2 or z == 2.2:
                        move = rook(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == True:
                            print("     |Invalid Choice")
                        else:
                            #if valid move then removes en passant  
                            if "pawnpassant" in game_stats:
                                game_stats.remove("pawnpassant")
                                game_stats.pop(-1)  
                            if c == 1:
                            #removes the ability of the user to castle depending on his move
                                if row_piece == 8 and col_piece == 8:
                                    if "w_rightcastle" in game_stats:
                                        game_stats.remove("w_rightcastle")         
                                elif row_piece == 8 and col_piece == 1:
                                    if "w_leftcastle" in game_stats:
                                        game_stats.remove("w_leftcastle")
                            elif c == 2:
                            #removes the ability of the user to castle depending on his move
                                if row_piece == 1 and col_piece == 8:
                                    if "b_rightcastle" in game_stats:
                                        game_stats.remove("b_rightcastle")        
                                elif row_piece == 1 and col_piece == 1:
                                    if "b_leftcastle" in game_stats:
                                        game_stats.remove("b_leftcastle")       
                    elif z == 1.3 or z == 2.3:    
                        move = horse(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == True:
                            print("     |Invalid Choice")
                        else:
                            #if valid move then removes en passant
                            if "pawnpassant" in game_stats:
                                game_stats.remove("pawnpassant")
                                game_stats.pop(-1)
                    elif z == 1.4 or z == 2.4:
                        move = bishop(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == True:
                            print("     |Invalid Choice")
                        else:
                            #if valid move then removes en passant
                            if "pawnpassant" in game_stats:
                                game_stats.remove("pawnpassant")     
                                game_stats.pop(-1)
                    elif z == 1.5 or z == 2.5:
                        move = queen(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == True:
                            print("     |Invalid Choice")
                        else:
                            #if valid move then removes en passant
                            if "pawnpassant" in game_stats:
                                game_stats.remove("pawnpassant")
                                game_stats.pop(-1)
                    elif z == 1.6 or z == 2.6:
                        move = king(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == True:
                            #if the normal move of king is invalid checks it checks if the chosen move is a castle
                            move = castling(row_move,col_move,row_piece,col_piece,c)
                            if move == True:
                                print("     |Invalid Choice")
                        else:
                            #if valid move then removes en passant
                            if "pawnpassant" in game_stats:
                                game_stats.remove("pawnpassant")
                                game_stats.pop(-1)   
                            if c == 1:
                                #removes the ability of the user to castle depending on his move
                                if "w_rightcastle" in game_stats:
                                    game_stats.remove("w_rightcastle")
                                    if "w_leftcastle" in game_stats:
                                        game_stats.remove("w_leftcastle")
                            elif c == 2:
                                #removes the ability of the user to castle depending on his move
                                if "b_rightcastle" in game_stats:
                                    game_stats.remove("b_rightcastle")
                                    if "b_leftcastle" in game_stats:
                                        game_stats.remove("b_leftcastle")
                else:
                    print("     |Please enter a number ranging 1-8")
        else:
            print("     |Please enter a number ranging 1-8")

#checks if chosen piece of the player is his own
def checkpiece(pnum,piece):
    if pnum == 1:
        if piece in whitepieces:
            return True
        else:
            print("     |------Please select a white piece")
            return False
    elif pnum == 2:
        if piece in blackpieces:
            return True
        else:
            print("     |------Please select a black piece")
            return False

#FOR EVERY MOVING FUNCTION
#   -checks first who is the player doing the move
#   -checks if the coordinate is empty or there is an enemy in the space there, else then it is invalid
#   -checks if the move is correct for the respective piece
#   -collision checkers(if applicable)
#   -if move is valid then replace the current block with a 0 and the place to move with z(the piece)
#   -checks if the player would be check doing the move(invalid)
#   -if all is good then the move is valid
#
#   -if ai: this checks if there is a possible move and if there is the computer would return the piece to its original position
       
#PAWN MOVING FUNCTION
def pawn(a,b,c,x,y,z,ai):
    eaten = board[a][b]
    #if move is valid changes the chosen coordinate of the user to the current piece 
    #and the coordinate of the current piece would be replaced with 0
    #if ai is true then it would only be for the checkmate checker and would check if there is an avalable move for pawn
    #but it replaces back the pieces to its original positions again
    #if the move is not valid it replaces it back to its original positions again
    if c == 1:
        #if the piece of white is in row 7 then it can move 2 steps upward and en passant would be possible for the player next turn
        if board[a][b] == 0:
            if a == (x-2) and b == y and x == 7:
                #checks if there is collision when 2 steps are used
                if a == (x-2) and board[x-1][y] in allpieces:
                    return True                        
                else:
                    board[x][y] = 0
                    board[a][b] = z
                    if checking(c):
                        if ai == True:
                            board[x][y] = z
                            board[a][b] = eaten
                            return False
                        else:
                            #adds the ability of the opposing player to en passant the pawn moved
                            if "pawnpassant" in game_stats:
                                game_stats.remove("pawnpassant")
                                game_stats.pop(-1)
                            game_stats.append("pawnpassant")
                            game_stats.append(b)#row_move coordinate for en passant function movement
                            return False
                    else:
                        board[x][y] = z
                        board[a][b] = eaten
                        return True
            elif a == (x-1) and b == y:
                board[x][y] = 0
                board[a][b] = z
                if checking(c):
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                        return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True
        #whitepawn eating blackpieces
        elif board[a][b] in blackpieces:
            if a == (x-1) and (b == (y-1) or b == (y+1)):
                board[x][y] = 0
                board[a][b] = z
                if checking(c):
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                    	capture(eaten)
                    	return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True     
        else:
            return True
    elif c == 2:
        if board[a][b] == 0:
            if a == (x+2) and b == y and x == 2:
                #checks if there is collision when 2 steps are used
                if a == (x+2) and board[x+1][y] in allpieces:
                    return True                        
                else:
                    board[x][y] = 0
                    board[a][b] = z
                    if checking(c):
                        if ai == True:
                            board[x][y] = z
                            board[a][b] = eaten
                            return False
                        else:
                            #adds the ability of the opposing player to en passant the pawn moved
                            if "pawnpassant" in game_stats:
                                game_stats.remove("pawnpassant")
                                game_stats.pop(-1)
                            game_stats.append("pawnpassant")
                            game_stats.append(b)    #row_move coordinate for en passant function movement
                            return False
                    else:
                        board[x][y] = z
                        board[a][b] = eaten
                        return True
            elif a == (x+1) and b == y:
                board[x][y] = 0
                board[a][b] = z
                if checking(c):
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                        return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True
        #blackpawn eating whitepieces
        elif board[a][b] in whitepieces:
            if a == (x+1) and (b == (y-1) or b == (y+1)):
                board[x][y] = 0
                board[a][b] = z
                if checking(c):
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                    	capture(eaten)
                    	return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True     
        else:
            return True

#ROOK MOVING FUNCTION
def rook(a,b,c,x,y,z,ai):
    #if move is valid changes the chosen coordinate of the user to the current piece 
    #and the coordinate of the current piece would be replaced with 0
    #if ai is true then it would only be for the checkmate checker and would check if there is an avalable move for rook
    #but it replaces back the pieces to its original positions again
    #if the move is not valid it replaces it back to its original positions again
    eaten = board[a][b]
    good = checkcross(a,b,x,y,c)
    if good:
        if c == 1:
            if board[a][b] == 0 or board[a][b] in blackpieces:
                board[x][y] = 0
                board[a][b] = z
                if checking(c):
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                    	capture(eaten)
                    	return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True
                    
        elif c == 2:
            if board[a][b] == 0 or board[a][b] in whitepieces:
                board[x][y] = 0
                board[a][b] = z
                if checking(c):
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                    	capture(eaten)
                    	return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True
    else:
        return True

#HORSE MOVING FUNCTION
def horse(a,b,c,x,y,z,ai):
    #if move is valid changes the chosen coordinate of the user to the current piece 
    #and the coordinate of the current piece would be replaced with 0
    #if ai is true then it would only be for the checkmate checker and would check if there is an avalable move for horse
    #but it replaces back the pieces to its original positions again
    #if the move is not valid it replaces it back to its original positions again
    eaten = board[a][b]
    if c == 1:
        if board[a][b] == 0  or board[a][b] in blackpieces:
            #L MOVES
            if (a == (x-2) and b == (y-1)) or (a == (x-2) and b == (y+1)) or (a == (x+2) and b == (y-1)) or (a == (x+2) and b == (y+1)) or (a == (x+1) and b == (y+2)) or (a == (x-1) and b == (y+2)) or (a == (x+1) and b ==(y-2)) or (a == (x-1) and b ==(y-2)):
                board[x][y] = 0
                board[a][b] = z
                good = checking(c)
                if good:
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                    	capture(eaten)
                    	return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True
        else:
            return True     
    elif c == 2:
        if board[a][b] == 0 or board[a][b] in whitepieces:
            if (a == (x-2) and b == (y-1)) or (a == (x-2) and b == (y+1)) or (a == (x+2) and b == (y-1)) or (a == (x+2) and b == (y+1)) or (a == (x+1) and b == (y+2)) or (a == (x-1) and b == (y+2)) or (a == (x+1) and b ==(y-2)) or (a == (x-1) and b ==(y-2)):
                board[x][y] = 0
                board[a][b] = z
                good = checking(c)
                if good:
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                    	capture(eaten)
                    	return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True
        else:
            return True

#Checks if the move of the user is diagonal    
def diagonal(a,b,c,x,y,z):
    if a > x:
        #quadrant 3 checker 
        if b < y:
            k = x
            for j in range(y-1,0,-1):
                k += 1
                if (j==b) and (k==a):
                    board[x][y] = 0
                    board[a][b] = z
                    return False
            return True
        #quadrant 4 checker 
        elif b > y:
            k = x
            for j in range(y+1,9):
                k += 1
                if (j==b) and (k==a):
                    board[x][y] = 0
                    board[a][b] = z
                    return False
            return True
    elif a < x:
        #quadrant 2 checker
        if b < y:
            k = x
            for j in range(y-1,0,-1):
                k -= 1
                if (j==b) and (k==a):
                    board[x][y] = 0
                    board[a][b] = z
                    return False
            return True
        #quadrant 3 checker
        elif b > y:
            k = x
            for j in range(y+1,9):
                k -= 1
                if (j==b) and (k==a):
                    board[x][y] = 0
                    board[a][b] = z
                    return False
            return True

#BISHOP MOVING FUNCTION                
def bishop(a,b,c,x,y,z,ai):
    #if move is valid changes the chosen coordinate of the user to the current piece 
    #and the coordinate of the current piece would be replaced with 0
    #if ai is true then it would only be for the checkmate checker and would check if there is an avalable move for bishop
    #but it replaces back the pieces to its original positions again
    #if the move is not valid it replaces it back to its original positions again
    good = checkdiagonals(a,b,x,y)
    eaten = board[a][b]
    if good:
        if c == 1:
            if board[a][b] == 0 or board[a][b] in blackpieces:
                diagon = diagonal(a,b,c,x,y,z)
                if diagon:
                    return True
                else:
                    if checking(c):
                        if ai == True:
                            board[x][y] = z
                            board[a][b] = eaten
                            return False
                        else:
                            capture(eaten)
                            return False
                    else:
                        board[x][y] = z
                        board[a][b] = eaten
                        return True
            else:
                return True
        elif c == 2:
            if board[a][b] == 0 or board[a][b] in whitepieces:
                diagon = diagonal(a,b,c,x,y,z)
                if diagon:
                    return True
                else:
                    if checking(c):
                        if ai == True:
                            board[x][y] = z
                            board[a][b] = eaten
                            return False
                        else:
                            capture(eaten)
                            return False
                    else:
                        board[x][y] = z
                        board[a][b] = eaten
                        return True
            else:
                return True
    else:
        return True

#QUEEN MOVING FUNCTION
def queen(a,b,c,x,y,z,ai):
    #combination of rook and bishop move functions
    if rook(a,b,c,x,y,z,ai) == False:
        return False
    else:
        if bishop(a,b,c,x,y,z,ai) == False:
            return False
        else:
            return True

#KING MOVING FUNCTION
def king(a,b,c,x,y,z,ai):
    #if move is valid changes the chosen coordinate of the user to the current piece 
    #and the coordinate of the current piece would be replaced with 0
    #if ai is true then it would only be for the checkmate checker and would check if there is an avalable move for king
    #but it replaces back the pieces to its original positions again
    #if the move is not valid it replaces it back to its original positions again
    eaten = board[a][b]
    if c == 1:
        #1 tile movements
        if ((a == (x+1) and (y  == b)) or (a == (x-1) and (y==b)) or (a == x and b == (y+1)) or (a == x and b == (y-1)) or (a == (x+1) and b == (y+1)) or (a == (x-1) and b == (y-1)) or (a == (x-1) and b == (y+1)) or (a == (x+1) and b == (y-1))):
            if board[a][b] == 0 or board[a][b] in blackpieces:
                board[x][y] = 0
                board[a][b] = z
                good = checking(c)
                if good:
                    if ai == True:
                        board[x][y] = z
                        board[a][b] = eaten
                        return False
                    else:
                        capture(eaten)
                        return False
                else:
                    board[x][y] = z
                    board[a][b] = eaten
                    return True
            else:
                return True
        else:
            return True
    elif c == 2:
        #1 tile movements
        if ((a == (x+1) and (y  == b)) or (a == (x-1) and (y==b)) or (a == x and b == (y+1)) or (a == x and b == (y-1)) or (a == (x+1) and b == (y+1)) or (a == (x-1) and b == (y-1)) or (a == (x-1) and b == (y+1)) or (a == (x+1) and b == (y-1))):
            if board[a][b] == 0 or board[a][b] in whitepieces:
                    board[x][y] = 0
                    board[a][b] = z
                    good = checking(c)
                    if good:
                        if ai == True:
                            board[x][y] = z
                            board[a][b] = eaten
                            return False
                        else:
                            capture(eaten)
                            return False
                    else:
                        board[x][y] = z
                        board[a][b] = eaten
                        return True
            else:
                return True
        else:
            return True

#collision checker if there is a piece horizontally or diagonally before the chosen coordinate of the user
def checkcross(a,b,x,y,c):
    if x == a:
        #right checker
        if b > y:
            for d in range(y+1,b):
                if board[x][d] in allpieces:
                    return False
            return True
        #left checker
        elif b < y:
            for d in range(y-1,b,-1):
                if board[x][d] in allpieces:
                    return False
            return True
    elif y == b:
        #down checker
        if a > x:
            for d in range(x+1,a):
                if board[d][y] in allpieces:
                    return False
            return True
        #up checker
        elif a < x:
            for d in range(x-1,a,-1):
                    if board[d][y] in allpieces:
                        return False
            return True
    return False

#collision checker if there is a piece diagonally before the chosen coordinate of the user
def checkdiagonals(a,b,x,y):
    if a > x:
        #quadrant 3 checker
        if b < y:
            k = x
            for j in range(y-1,b,-1):
                k += 1
                if board[k][j] in allpieces:
                    return False
            else:
                return True
        #quadrant 4 checker
        elif b > y:
            k = x
            for j in range(y+1,b):
                k += 1
                if board[k][j] in allpieces:
                    return False
            else:
                return True
    elif a < x:
        #quadrant 2 checker
        if b < y:
            k = x
            for j in range(y-1,b,-1):
                k -= 1
                if board[k][j] in allpieces:
                    return False
            else:
                return True
        #quadrant 1 checker
        elif b > y:
            k = x
            for j in range(y+1,b):
                k -= 1
                if board[k][j] in allpieces:
                    return False
            else:
                return True
    else:
        return False

#checks if the king is checked or will be checked
def checking(c):
    #checks all the pieces in every piece of block in the game
    for x in range(10):
        for y in range(10):
            #checks every checking function of the respective piece
            #if check returns false else it returns true
            if board [x][y] == 2.1 or board[x][y] == 1.1:
                if checkpawn(x,y,c) == False:
                    return False 
            elif board[x][y] == 2.2 or board[x][y] == 1.2:
                if checkrook(x,y,c) == False:
                    return False 
            elif board[x][y] == 2.3 or board[x][y] == 1.3:
                if checkhorse(x,y,c) == False:
                    return False 
            elif board[x][y] == 2.4 or board[x][y] == 1.4:
                if checkbishop(x,y,c) == False:
                    return False 
            elif board[x][y] == 2.5 or board[x][y] == 1.5:
                if checkqueen(x,y,c) == False:
                    return False 
            elif board[x][y] == 2.6 or board[x][y] == 1.6:
                if checkking(x,y,c) == False:
                    return False 
    return True

#checks if the pawn checks the king
def checkpawn(x,y,c):
    #1 piece diagonally checking the king
    if c == 1:
        if (board[x][y] == 2.1 and (board[x+1][y-1] == 1.6 or board[x+1][y+1] == 1.6)):
            return False
        else:
            return True
    elif c == 2:
        if (board[x][y] == 1.1 and (board[x-1][y-1] == 2.6 or board[x-1][y+1] == 2.6)):
            return False
        else:
            return True

#checks if the rook checks the king
def checkrook(x,y,c):
    a = 1.2
    b = 2.2
    #horizontal and vertical checking
    return checkupdownleftright(x,y,a,b,c)

#checks if the horse checks the king
def checkhorse(x,y,c):
    #L MOVES TO SEE IF THE KING IS IN THAT BLOCK
    if c == 1:
        #different x and y due to the reason of it being out of range if the horse is in the corner
        if x == 8 and y == 8:
            if (board[x][y] == 2.3 and (board[x-2][y-1] == 1.6 or board[x-2][y+1] == 1.6 or board[x+1][y+2] == 1.6 or board[x-1][y-2] == 1.6)):
                return False
        elif x == 8 and y == 1:
            if (board[x][y] == 2.3 and (board[x-2][y-1] == 1.6 or board[x-2][y+1] == 1.6 or board[x+1][y+2] == 1.6 or board[x-1][y+2] == 1.6)):
                return False
        elif x == 1 and y == 8:
            if (board[x][y] == 2.3 and (board[x+2][y-1] == 1.6 or board[x+2][y+1] == 1.6 or board[x+1][y-2] == 1.6 or board[x-1][y-2] == 1.6)):
                return False
        elif x == 1 and y == 1:
            if (board[x][y] == 2.3 and (board[x+2][y-1] == 1.6 or board[x+2][y+1] == 1.6 or board[x+1][y+2] == 1.6 or board[x-1][y+2] == 1.6 )):
                return False
        elif x == 8:
            if (board[x][y] == 2.3 and (board[x-2][y-1] == 1.6 or board[x-2][y+1] == 1.6 or board[x+1][y+2] == 1.6 or board[x-1][y+2] == 1.6 or board[x+1][y-2] == 1.6 or board[x-1][y-2] == 1.6)):
                return False
        elif x == 1:
            if (board[x][y] == 2.3 and (board[x+2][y-1] == 1.6 or board[x+2][y+1] == 1.6 or board[x+1][y+2] == 1.6 or board[x-1][y+2] == 1.6 or board[x+1][y-2] == 1.6 or board[x-1][y-2] == 1.6)):
                return False
        elif y == 8:
            if (board[x][y] == 2.3 and (board[x-2][y-1] == 1.6 or board[x-2][y+1] == 1.6 or board[x+2][y-1] == 1.6 or board[x+2][y+1] == 1.6 or board[x+1][y-2] == 1.6 or board[x-1][y-2] == 1.6)):
                return False
        elif y == 1:
            if (board[x][y] == 2.3 and (board[x-2][y-1] == 1.6 or board[x-2][y+1] == 1.6 or board[x+2][y-1] == 1.6 or board[x+2][y+1] == 1.6 or board[x+1][y+2] == 1.6 or board[x-1][y+2] == 1.6)):
                return False
        else:
            if (board[x][y] == 2.3 and (board[x-2][y-1] == 1.6 or board[x-2][y+1] == 1.6 or board[x+2][y-1] == 1.6 or board[x+2][y+1] == 1.6 or board[x+1][y+2] == 1.6 or board[x-1][y+2] == 1.6 or board[x+1][y-2] == 1.6 or board[x-1][y-2] == 1.6)):
                return False
            else:
                return True
    elif c == 2:
        if x == 8 and y == 8:
            if (board[x][y] == 1.3 and (board[x-2][y-1] == 2.6 or board[x-2][y+1] == 2.6 or board[x+1][y+2] == 2.6 or board[x-1][y-2] == 2.6)):
                return False
        elif x == 8 and y == 1:
            if (board[x][y] == 1.3 and (board[x-2][y-1] == 2.6 or board[x-2][y+1] == 2.6 or board[x+1][y+2] == 2.6 or board[x-1][y+2] == 2.6)):
                return False
        elif x == 1 and y == 8:
            if (board[x][y] == 1.3 and (board[x+2][y-1] == 2.6 or board[x+2][y+1] == 2.6 or board[x+1][y-2] == 2.6 or board[x-1][y-2] == 2.6)):
                return False
        elif x == 1 and y == 1:
            if (board[x][y] == 1.3 and (board[x+2][y-1] == 2.6 or board[x+2][y+1] == 2.6 or board[x+1][y+2] == 2.6 or board[x-1][y+2] == 2.6 )):
                return False
        elif x == 8:
            if (board[x][y] == 1.3 and (board[x-2][y-1] == 2.6 or board[x-2][y+1] == 2.6 or board[x+1][y+2] == 2.6 or board[x-1][y+2] == 2.6 or board[x+1][y-2] == 2.6 or board[x-1][y-2] == 2.6)):
                return False
        elif x == 1:
            if (board[x][y] == 1.3 and (board[x+2][y-1] == 2.6 or board[x+2][y+1] == 2.6 or board[x+1][y+2] == 2.6 or board[x-1][y+2] == 2.6 or board[x+1][y-2] == 2.6 or board[x-1][y-2] == 2.6)):
                return False
        elif y == 8:
            if (board[x][y] == 1.3 and (board[x-2][y-1] == 2.6 or board[x-2][y+1] == 2.6 or board[x+2][y-1] == 2.6 or board[x+2][y+1] == 2.6 or board[x+1][y-2] == 2.6 or board[x-1][y-2] == 2.6)):
                return False
        elif y == 1:
            if (board[x][y] == 1.3 and (board[x-2][y-1] == 2.6 or board[x-2][y+1] == 2.6 or board[x+2][y-1] == 2.6 or board[x+2][y+1] == 2.6 or board[x+1][y+2] == 2.6 or board[x-1][y+2] == 2.6)):
                return False
        else:
            if (board[x][y] == 1.3 and (board[x-2][y-1] == 2.6 or board[x-2][y+1] == 2.6 or board[x+2][y-1] == 2.6 or board[x+2][y+1] == 2.6 or board[x+1][y+2] == 2.6 or board[x-1][y+2] == 2.6 or board[x+1][y-2] == 2.6 or board[x-1][y-2] == 2.6)):
                return False
            else:
                return True

#checks if the bishop checks the king          
def checkbishop(x,y,c):
    a = 1.4
    b = 2.4
    #diagonally checking
    return checkquadrants(x,y,a,b,c)

#checks if the queen checks the king
def checkqueen(x,y,c):
    #combination of bishop and rook
    a = 1.5
    b = 2.5
    crosscheck = checkupdownleftright(x,y,a,b,c)
    if crosscheck == True:
        return checkquadrants(x,y,a,b,c)
    else:
        return False

#checks if the king checks the opposite king
def checkking(x,y,c):
    #written to prevent kings from being one spaces to one another
    if c == 1:
        if board[x][y] == 2.6 and (board[x+1][y] == 1.6 or board[x-1][y] == 1.6 or board[x+1][y+1] == 1.6 or board[x+1][y-1] == 1.6 or board[x-1][y+1] == 1.6 or board[x-1][y-1] == 1.6 or board[x][y+1] == 1.6 or board[x][y-1] == 1.6):
            return False
        else:
            return True
    elif c == 2:
        if board[x][y] == 1.6 and (board[x+1][y] == 2.6 or board[x-1][y] == 2.6 or board[x+1][y+1] == 2.6 or board[x+1][y-1] == 2.6 or board[x-1][y+1] == 2.6 or board[x-1][y-1] == 2.6 or board[x][y+1] == 2.6 or board[x][y-1] == 2.6):
            return False
        else:
            return True

#checks horizontally and vertically if it checks the king
def checkupdownleftright(x,y,a,b,c):
    #if it is in allpieces_noking means that there is a piece blocking the way
    #if it is in the gridboard means that it reached the edge of the board
    upcheck = True
    downcheck = True
    leftcheck = True
    rightcheck = True
    if c == 1:
        if upcheck:
            for i in range(1,8):
                if board[x-i][y] in gridboard:
                    break
                elif board[x-i][y] in allpieces_noking:
                    break
                elif board[x][y] == b and board[x-i][y] == 1.6:
                    return False
        if downcheck:
            for i in range(1,8):
                if board[x+i][y] in gridboard:
                    break
                elif board[x+i][y] in allpieces_noking:
                    break
                elif board[x][y] == b and board[x+i][y] == 1.6:
                    return False
        if leftcheck:
            for i in range(1,8):
                if board[x][y-i] in gridboard:
                    break
                elif board[x][y-i] in allpieces_noking:
                    break
                elif board[x][y] == b and board[x][y-i] == 1.6:
                    return False
        if rightcheck:
            for i in range(1,8):
                if board[x][y+i] in gridboard:
                    break
                elif board[x][y+i] in allpieces_noking:
                    break
                elif board[x][y] == b and board[x][y+i] == 1.6:
                    return False
        return True
    elif c == 2:
        if upcheck:
            for i in range(1,8):
                if board[x-i][y] in gridboard:
                    break
                elif board[x-i][y] in allpieces_noking:
                    break
                elif board[x][y] == a and board[x-i][y] == 2.6:
                    return False
        if downcheck:
            for i in range(1,8):
                if board[x+i][y] in gridboard:
                    break
                elif board[x+i][y] in allpieces_noking:
                    break
                elif board[x][y] == a and board[x+i][y] == 2.6:
                    return False
        if leftcheck:
            for i in range(1,8):
                if board[x][y-i] in gridboard:
                    break
                elif board[x][y-i] in allpieces_noking:
                    break
                elif board[x][y] == a and board[x][y-i] == 2.6:
                    return False
        if rightcheck:
            for i in range(1,8):
                if board[x][y+i] in gridboard:
                    break
                elif board[x][y+i] in allpieces_noking:
                    break
                elif board[x][y] == a and board[x][y+i] == 2.6:
                    return False
        return True

#checks diagonally if it checks the king
def checkquadrants(x,y,a,b,c):
    #if it is in allpieces_noking means that there is a piece blocking the way
    #if it is in the gridboard means that it reached the edge of the board
    q1check = True
    q2check = True
    q3check = True
    q4check = True
    if c == 1:
        #upper right diagonal check
        if q1check:
            k = x
            for j in range(y+1,10):
                k -= 1
                if board[k][j] in gridboard:
                    break    
                if board[k][j] in allpieces_noking:
                    break   
                elif board[x][y] == b and board[k][j] == 1.6:
                    return False 
        if q2check:
        #upper left diagonal check
            k = x
            for j in range(y-1,-1,-1):
                k -= 1
                if board[k][j] in gridboard:
                    break   
                elif board[k][j] in allpieces_noking:
                    break   
                elif board[x][y] == b and board[k][j] == 1.6:
                    return False
        #lower left diagonal check
        if q3check:
            k = x
            for j in range(y-1,-1,-1):
                k += 1
                if board[k][j] in gridboard:
                    break   
                elif board[k][j] in allpieces_noking:
                    break   
                elif board[x][y] == b and board[k][j] == 1.6:
                    return False
        #lower right diagonal check
        if q4check:
            k = x
            for j in range(y+1,10):
                k += 1
                if board[k][j] in gridboard:
                    break   
                elif board[k][j] in allpieces_noking:
                    break   
                elif board[x][y] == b and board[k][j] == 1.6:
                    return False
        #if king not there in all quadrants then returns true
        return True

    elif c == 2:
        #upper right diagonal check
        if q1check:
            k = x
            for j in range(y+1,10):
                k -= 1
                if board[k][j] in gridboard:
                    break    
                if board[k][j] in allpieces_noking:
                    break   
                elif board[x][y] == a and board[k][j] == 2.6:
                    return False
        #upper left diagonal check
        if q2check:
            k = x
            for j in range(y-1,-1,-1):
                k -= 1
                if board[k][j] in gridboard:
                    break   
                elif board[k][j] in allpieces_noking:
                    break   
                elif board[x][y] == a and board[k][j] == 2.6:
                    return False
        #lower left diagonal check
        if q3check:
            k = x
            for j in range(y-1,-1,-1):
                k += 1
                if board[k][j] in gridboard:
                    break   
                elif board[k][j] in allpieces_noking:
                    break   
                elif board[x][y] == a and board[k][j] == 2.6:
                    return False
        #lower right diagonal check
        if q4check:
            k = x
            for j in range(y+1,10):
                k += 1
                if board[k][j] in gridboard:
                    break   
                elif board[k][j] in allpieces_noking:
                    break   
                elif board[x][y] == a and board[k][j] == 2.6:
                    return False
        #if king not there in all quadrants then returns true
        return True

#lets the pawn promote if it reaches the needed position
def pawnpromotion():
    #choices allowed for change are queen,bishop,rook, and horse
    for y in range(10):
        if board[1][y] == 1.1:
            while True:
                print("Please choose your piece:")
                choice = input("1. Rook \n2. Horse \n3. Bishop \n4. Queen \n")
                if choice == "1":
                    #replaces with a rook
                    board[1][y] = 1.2
                    return True
                elif choice == "2":
                    #replaces with a horse
                    board[1][y] = 1.3
                    return True
                elif choice == "3":
                    #replaces with a bishop
                    board[1][y] = 1.4
                    return True
                elif choice == "4":
                    #replaces with a queen
                    board[1][y] = 1.5
                    return True
                else:
                    print("Invalid Choice")
        elif board[8][y] == 2.1:
            while True:
                print("Please choose your piece:")
                choice = input("1. Rook \n2. Horse \n3. Bishop \n4. Queen \n")
                if choice == "1":
                    #replaces with a rook
                    board[8][y] = 2.2
                    return True
                elif choice == "2":
                    #replaces with a horse
                    board[8][y] = 2.3
                    return True
                elif choice == "3":
                    #replaces with a bishop
                    board[8][y] = 2.4
                    return True
                elif choice == "4":
                    #replaces with a queen
                    board[8][y] = 2.5
                    return True
                else:
                    print("Invalid Choice")
    #if there is no pawn in board[1][y] or board [8][y] then there is no pawn promotion
    return False
   
#function for king castles
def castling(a,b,x,y,c):
    #whiteright side castles if conditions are fulfilled
    if a == 8 and b == 7 and board[8][8] == 1.2 and board[x][y+1] == 0 and board[x][y+2] == 0 and "w_rightcastle" in game_stats:
        if checking(c):
            board[8][5] = 0
            board[8][6] = 1.2                                
            board[8][7] = 1.6
            board[8][8] = 0
            if checking(c):
                #if valid removes the right to castle
                if "w_rightcastle" in game_stats:
                    game_stats.remove("w_rightcastle")
                    if "w_leftcastle" in game_stats:
                        game_stats.remove("w_leftcastle")
                return False
            else:
                #if the king is check then returns to original position
                board[8][5] = 1.6
                board[8][6] = 0                                
                board[8][7] = 0
                board[8][8] = 1.2
                return True
        #if not valid then return true
        else:
            return True
    #whiteleft side castles if conditions are fulfilled
    elif a == 8 and b == 3 and board[8][1] == 1.2 and board[x][y-1] == 0 and board[x][y-2] == 0 and board[x][y-3] == 0 and "w_leftcastle" in game_stats:
        if checking(c):
            board[8][5] = 0
            board[8][4] = 1.2
            board[8][3] = 1.6
            board[8][2] = 0
            board[8][1] = 0
            if checking(c):
                #if valid removes the right to castle
                if "w_rightcastle" in game_stats:
                    game_stats.remove("w_rightcastle")
                    if "w_leftcastle" in game_stats:
                        game_stats.remove("w_leftcastle")
                return False
            else:
                #if king is check then returns to original position
                board[8][5] = 1.6
                board[8][4] = 0                                
                board[8][3] = 0
                board[8][2] = 0
                board[8][1] = 1.2
                return True
        #if not valid then return true
        else:
            return True
    #blackright side castles if conditions are fulfilled
    elif a == 1 and b == 7 and board[1][8] == 2.2 and board[x][y+1] == 0 and board[x][y+2] == 0 and "b_rightcastle" in game_stats:
        if checking(c):
            board[1][5] = 0
            board[1][6] = 2.2
            board[1][7] = 2.6
            board[1][8] = 0
            if checking(c):
                if "b_rightcastle" in game_stats:
                    game_stats.remove("b_rightcastle")
                    if "b_leftcastle" in game_stats:
                        game_stats.remove("b_leftcastle")
                return False
            #if not valid returns to original position
            else:
                board[1][5] = 2.6
                board[1][6] = 0                                
                board[1][7] = 0
                board[1][8] = 2.2
                return True 
        else:
            return True
    #blackleft side castles if conditions are fulfilled
    elif a == 1 and b == 3 and board[1][1] == 2.2 and board[x][y-1] == 0 and board[x][y-2] == 0 and board[x][y-3] == 0 and "b_leftcastle" in game_stats:
        if checking(c):
            board[1][5] = 0
            board[1][4] = 2.2
            board[1][3] = 2.6
            board[1][2] = 0
            board[1][1] = 0
            if checking(c):
                #if valid removes the right to castle
                if "b_rightcastle" in game_stats:
                    game_stats.remove("b_rightcastle")
                    if "b_leftcastle" in game_stats:
                        game_stats.remove("b_leftcastle")
                return False
            #if king is check then returns to original position
            else:
                board[1][5] = 2.6
                board[1][4] = 0                                
                board[1][3] = 0
                board[1][2] = 0
                board[1][1] = 2.2
                return True 
        #if not valid return true
        else:
            return True
    #if not valid then return true
    else:
        return True

#en passant move function
def passant(a,b,x,y,c):
    #pawn capture that can only occur immediately after a pawn makes a move of two squares from its starting square
    d = game_stats[-1]#row_move coordinate of the pawn appended when the moved two steps
    if c == 1:
        if x == 4:  
            if board[x][y+1] == 2.1 and d == y+1 and "pawnpassant" in game_stats:
                if a == x - 1 and b == y + 1:
                    board[x][y] = 0
                    board[x][y+1] = 0
                    board[a][b] = 1.1
                    return False
                else:
                    return True
            elif board[x][y-1] == 2.1 and d == y-1 and "pawnpassant" in game_stats:
                if a == x - 1 and b == y - 1:
                    board[x][y] = 0
                    board[x][y-1] = 0
                    board[a][b] = 1.1
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    elif c == 2:
        if x == 5:  
            if board[x][y+1] == 1.1 and d == y+1 and "pawnpassant" in game_stats:
                if a == x + 1 and b == y + 1:
                    board[x][y] = 0
                    board[x][y+1] = 0
                    board[a][b] = 2.1
                    return False
                else:
                    return True
            elif board[x][y-1] == 1.1 and d == y-1 and "pawnpassant" in game_stats:
                if a == x + 1 and b == y - 1:
                    board[x][y] = 0
                    board[x][y-1] = 0
                    board[a][b] = 2.1
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True

#checks if there is a possible move for the player
def checkmate(c):
    #using for loop makes an "ai" run every possible coordinate to check if there is a possible move for the player
    #ai is used to return the piece to its original position after moving because it is only used to check if there is a possible move
    ai = True
    for row_piece in range(1,9):
        for col_piece in range(1,9):
            #if not the player's turn then does not check if he has a possible move
            z = board[row_piece][col_piece]
            if c == 1:
                if board[row_piece][col_piece] in blackpieces:
                    continue
            elif c == 2:
                if board[row_piece][col_piece] in whitepieces:
                    continue
            #checks every piece in the board if there is a move
            for row_move in range(1,9):
                for col_move in range(1,9):
                    if z == 1.1 or z == 2.1:
                        move = pawn(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == False:
                            return False
                    elif z == 1.2 or z == 2.2:
                        move = rook(row_move,col_move,c,row_piece,col_piece,z,ai)    
                        if move == False:
                            return False
                    elif z == 1.3 or z == 2.3:    
                        move = horse(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == False:
                            return False
                    elif z == 1.4 or z == 2.4:
                        move = bishop(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == False:
                            return False
                    elif z == 1.5 or z == 2.5:
                        move = queen(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == False:
                            return False
                    elif z == 1.6 or z == 2.6:
                        move = king(row_move,col_move,c,row_piece,col_piece,z,ai)
                        if move == False:
                            return False
    #if there is no possible move then it is checkmate or draw
    return True

#shows what the user has eaten against the other player
def capture(z):
	if z == 1.1:
		print(" 	 ---------------------")
		print(" 	| White Pawn Captured |")
		print(" 	 ---------------------")
		print("")
	elif z == 1.2:
		print(" 	 ---------------------")
		print(" 	| White Rook Captured |")
		print(" 	 ---------------------")
		print("")
	elif z == 1.3:
		print(" 	 ----------------------")
		print(" 	| White Horse Captured |")
		print(" 	 ----------------------")
		print("")
	elif z == 1.4:
		print(" 	 -----------------------")
		print(" 	| White Bishop Captured |")
		print(" 	 -----------------------")
		print("")
	elif z == 1.5:
		print(" 	 ----------------------")
		print(" 	| White Queen Captured |")
		print(" 	 ----------------------")
		print("")
	elif z == 2.1:
		print(" 	 ---------------------")
		print(" 	| Black Pawn Captured |")
		print(" 	 ---------------------")
		print("")
	elif z == 2.2:
		print(" 	 ---------------------")
		print(" 	| Black Rook Captured |")
		print(" 	 ---------------------")
		print("")
	elif z == 2.3:
		print(" 	 ----------------------")
		print(" 	| Black Horse Captured |")
		print(" 	 ----------------------")
		print("")
	elif z == 2.4:
		print(" 	 -----------------------")
		print(" 	| Black Bishop Captured |")
		print(" 	 -----------------------")
		print("")
	elif z == 2.5:
		print(" 	 ----------------------")
		print(" 	| Black Queen Captured |")
		print(" 	 ----------------------")
		print("")

#save function for the current board,game_stats, and scores                        
def save():
    fp = open("chess.txt","w")
    #write all of the elements in the board separated by "," in the first line
    for i in board:
        for j in i:
            j = str(j) + ","
            fp.write(j)
    fp.write("\n")
    #write the current game_stats sparated by "," that is used in the current game in the second line
    for i in game_stats:
        i = str(i) + ","
        fp.write(i)
    fp.write("\n")
    #write the highscores with the first data being the number of moves then the name in the succeeding lines
    for i in scores:
        i = str(i[0])+","+str(i[1])
        fp.write(i)
        fp.write("\n")
    
    fp.close()

#load function for the data saved in text file
def load(hs):
    scores.clear()
    fp = open("chess.txt","r")
    n_line = 1
    for i in fp:
        #replaces the board with the data in the first line of the text file
        if n_line == 1:
            if hs == 1:
                data = i.split(",")
                data = data[:-1]
                x = 0
                y = 0
                for j in data:
                    if j in allpieces_str:
                        j = float(j)
                        board[x][y] = j
                    elif j == "0":
                        j = 0
                    board[x][y] = j
                    y += 1
                    if y > 9:
                        y = 0
                        if x < 9:
                            x += 1
                    elif x >= 9 and y >= 9 :
                        n_line += 1
                        break
            else:
                n_line += 1
        #clears the game_stats and adds the data in the second line
        elif n_line == 2:
            if hs == 1:
                game_stats.clear()
                data = i.split(",")
                data = data[:-1]
                for j in data:
                    game_stats.append(j)
                n_line += 1
            else:
                n_line += 1
        #adds all the data in the third line to the last and puts them in scores list
        elif n_line == 3:
            data = i.split(",")
            data1 = data[0]
            data2 = data[-1][:-1]
            data = [data1,data2]    #list to be added in scores list
            scores.append(data)
        
    fp.close()

#HIGHSCORE FUNCTION
def highscore(c):
    #takes in the name of the winner and adds his score to the scores list
    #takes only 4 character names
    #converts the number of moves into int
    a=0
    for x in scores:
        nums = int(x[0])
        scores[a][0] = nums
        a += 1
    #sorts the list
    scores.sort()
    if c == 1:
        print("Blacks' Number of Moves is ",game_stats[2])
        while True:
            name = str(input("Enter Blacks' Name(4 Characters only): "))
            name = name.upper()
            #checks if the input only has 4 characters
            if len(name) != 4:
                print("Please enter a 4 character name")
            else:
                #checks if name already taken
                for x in scores:
                    if name in x:
                        print("Name already taken choose another one.")
                        break
                else:
                    break
        #if length of scores is  not = 0
        if len(scores) != 0:
            data = [game_stats[2],name]
            #if length is 10 it checks if the value of the highest value is lower than what the player has done
            if len(scores) >= 10:
                if int(data[0]) <= int(scores[-1][0]):
                    scores.pop(-1)
                    scores.append(data)
                    return True
                else:
                    print("Sorry your number of moves did not make it into the top 10")
                    return True   
            #if not it simply appends the data to the scores
            else:
                scores.append(data)
                return True
        #if length of scores is = 0 then it simply appends the data
        else:
            data = [game_stats[2],name]
            scores.append(data)
            return True
    if c == 2:
        print("Whites' Number of Moves is ",game_stats[1])
        while True:
            name = str(input("Enter Whites' Name(4 Characters only): "))
            name = name.upper()
            #checks if the name inputted by the user is 4 characters
            if len(name) != 4:
                print("Please enter a 4 character name")
            else:
                #checker if the name is already in the scores list
                for x in scores:
                    if name in x:
                        print("Name already taken choose another one.")
                        break
                else:
                    break
        #if length is not equal to 0
        if len(scores) != 0:
            data = [game_stats[1],name]
            #if length is 10 it checks if the value of the highest value is lower than what the player has done
            if len(scores) >= 10:
                if int(data[0]) <= int(scores[-1][0]):
                    scores.pop(-1)
                    scores.append(data)
                    return True
                else:   
                    print("Sorry your number of moves did not make it into the top 10")
                    return True     
            #if not then it simply appends the data
            else:
                scores.append(data)
                return True
        #if length is == 0 then it simply appends the data
        else:
            data = [game_stats[1],name]
            scores.append(data)
            return True
    
menu()
