'''
Haris Naveed
CSCI Computer Science 120A
Final Project
Professor Greg Schaper
Chess Game
'''

import subprocess
from datetime import datetime #got it from a website named https://www.programiz.com/python-programming/datetime/current-datetime

def write_file(wdict,bdict,letter,date_time):
    white_piece_after = len(list(wdict.values()))
    black_piece_after = len(list(bdict.values()))
    num_white_piece_used = 16 - white_piece_after
    num_black_piece_used = 16 - black_piece_after
    outfile = open("Previous_Games_of_Chess",'w')
    print("Chess Game: %s"% date_time,file=outfile)
    print("White Pieces: ",wdict, file=outfile)
    print("Black Pieces: ",bdict, file=outfile)
    if letter =='W':
        print("White won, using %d"% num_white_piece_used, file=outfile)
        print("Black lost, using %d"% num_black_piece_used,file=outfile)
    else:
        print("Black won, using %d"% num_black_piece_used, file=outfile)
        print("White lost, using %d"% num_white_piece_used, file=outfile)
    print("\n",file=outfile)
    print("\n",file=outfile)
    outfile.close()

def update_game_board_2(dict_,list_of_col,list_of_rows,list_of_pieces):
    keys = list(dict_.keys())
    for element in keys:
            location = dict_[element]
            if location[0] == 'A':
                num = 1
                list_of_rows.append(num)
            elif location[0] == 'B':
                num = 2
                list_of_rows.append(num)
            elif location[0] == 'C':
                num = 3
                list_of_rows.append(num)
            elif location[0] == 'D':
                num = 4
                list_of_rows.append(num)
            elif location[0] == 'E':
                num = 5
                list_of_rows.append(num)
            elif location[0] == 'F':
                num = 6
                list_of_rows.append(num)
            elif location[0] == 'G':
                num = 7
                list_of_rows.append(num)
            elif location[0] == 'H':
                num = 8
                list_of_rows.append(num)


            if location[1] == '1':
                list_of_col.append(1)
            elif location[1] == '2':
                list_of_col.append(2)
            elif location[1] == '3':
                list_of_col.append(3)
            elif location[1] == '4':
                list_of_col.append(4)
            elif location[1] == '5':
                list_of_col.append(5)
            elif location[1] == '6':
                list_of_col.append(6)
            elif location[1] == '7':
                list_of_col.append(7)
            elif location[1] == '8':
                list_of_col.append(8)

    for piece in dict_:
        list_of_pieces.append(piece)
    return list_of_col,list_of_rows,list_of_pieces


def print_game_board(game_board):
    for row in game_board:
        for col in row:
            print("\t", col, end=' ')
        print()

def update_game_board(white_dict, black_dict):
    '''Dr. Schaper helped me build this gameboard.'''
    game_board = []
    for j in range(9):
        temp = []
        for i in range(9):
            temp.append([])
        game_board.append(temp)
    for i in range(1, 9):
        game_board[0][i] = [i]
    headings = "ABCDEFGHI"
    for i in range(1, 9):
        game_board[i][0] = [headings[i - 1]]

    list_of_col = []
    list_of_rows = []
    list_of_pieces = []
    list_of_col, list_of_rows, list_of_pieces = update_game_board_2(white_dict, list_of_col, list_of_rows,
                                                                    list_of_pieces)
    list_of_col, list_of_rows, list_of_pieces = update_game_board_2(black_dict, list_of_col, list_of_rows,
                                                                    list_of_pieces)

    for index in range(len(list_of_pieces)):
        game_board[list_of_rows[index]][list_of_col[index]] = list_of_pieces[index]


    return game_board

def piece_input_validation_2(list_,piece,wdict_,bdict_):
    while True:
        if len(piece) == 3 and piece[0:2].isalpha() and piece[2].isdigit() or len(piece) == 3 and piece[0:1].isalpha() and piece[2] == "1":
            if piece in list_:
                if piece == list_[0] or piece == list_[7]:
                    wdict, bdict_ = rook(piece, wdict_, bdict_)
                elif piece == list_[1] or piece == list_[6]:
                    wdict_, bdict_ = horse(piece, wdict_, bdict_)
                elif piece == list_[2] or piece == list_[5]:
                    wdict_, bdict_ = bishop(piece, wdict_, bdict_)
                elif piece == list_[3]:
                    wdict_, bdict_ = king(piece, wdict_, bdict_)
                elif piece == list_[4]:
                    wdict_, bdict_ = queen(piece, wdict_, bdict_)
                elif piece == list_[8] or piece == list_[9] or piece == list_[10] or piece == list_[11] or piece == list_[
                    12] or piece == list_[13] or piece == list_[14] or piece == list_[15] or piece == list_[16]:
                    wdict_, bdict_ = pawn(piece, wdict_, bdict_)
                return wdict_, bdict_
            else:
                piece = input("Invalid piece, try again2: ").upper().strip()
        else:
            piece = input("Invalid piece, try again1: ").upper().strip()


def piece_input_validation(list_,wdict_,bdict_,letter):
    if letter == 'W':
        print("White Turn")
    else:
        print("Black Turn")
    piece = input("Enter a piece: ").upper().strip()

    while True:
        if piece[0] == letter:
            wdict_,bdict_ = piece_input_validation_2(list_,piece,wdict_,bdict_)
            return wdict_, bdict_
        else:
            piece = input("Invalid piece, try again3: ").upper().strip()


def check_piece_location_validation(piece,dict_):
    user_piece_new = input("Enter a new location of %s: " % piece).upper().strip()
    while True:
        if len(user_piece_new) == 2:
            if user_piece_new[0].isalpha() and user_piece_new[1].isdigit():
                if user_piece_new != dict_[piece]:
                    if user_piece_new not in dict_.values():
                        return user_piece_new
                    else:
                        user_piece_new = input("Invalid location, try again: ").upper().strip()
                else:
                    user_piece_new = input("Invalid location, try again: ").upper().strip()
            else:
                user_piece_new = input("Invalid location, try again: ").upper().strip()
        else:
            user_piece_new = input("Invalid location, try again: ").upper().strip()

def remove_piece_in_dict(dict_,new_location):
    keys = list(dict_.keys())
    for element in keys:
        if dict_[element] == new_location:
            del dict_[element]
    return dict_

def piece_check_1(list_of_pieces,dict_,dict_2,piece,list_of_potential_moves,letter):
    if dict_[piece][1] == '1' and dict_[piece][0] + str(int(2)) in list(dict_.values()):
        print("\n")
        print("Invalid piece. You cannot use this piece.")
        piece_input_validation(list_of_pieces, dict_, dict_2, letter)
    else:
        dict_, dict_2 = check_piece_1(list_of_potential_moves, piece, dict_, dict_2)
        return dict_,dict_2

def rook(piece,wdict_,bdict_):
    white_list = ['WR1', 'WH1', 'WB1', 'WK1', 'WQ1', 'WB2', 'WH2', 'WR2', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6',
                  'WP7', 'WP8']
    black_list = ['BR1', 'BH1', 'BB1', 'BK1', 'BQ1', 'BB2', 'BH2', 'BR2', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6',
                  'BP7', 'BP8']
    if piece[0] == 'W':
        # make a list of possible moves
        list_of_potential_moves = []
        for num in range(1,9):
            position_1 = wdict_[piece][0] + str(num) #moving right
            position_2 = wdict_[piece][0] + str(num) #moving left
            position_3 = chr(ord(wdict_[piece][0])+num) + wdict_[piece][1] #moving down
            position_4 = chr(ord(wdict_[piece][0])-num) + wdict_[piece][1] #moving up
            list_of_potential_moves.append(position_1)
            list_of_potential_moves.append(position_2)
            list_of_potential_moves.append(position_3)
            list_of_potential_moves.append(position_4)
        if wdict_[piece][1] == '1' and wdict_[piece][0] + str(2) in list(wdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(white_list,wdict_,bdict_,'W')
        else:
            wdict_,bdict_ = check_piece_1(list_of_potential_moves,piece,wdict_,bdict_)
    else:
        print("Black")
        list_of_potential_moves = []
        for num in range(1, 9):
            position_1 = bdict_[piece][0] + str(num)  # moving right
            position_2 = bdict_[piece][0] + str(num)  # moving left
            position_3 = chr(ord(bdict_[piece][0]) + num) + bdict_[piece][1]  # moving down
            position_4 = chr(ord(bdict_[piece][0]) - num) + bdict_[piece][1]  # moving up
            list_of_potential_moves.append(position_1)
            list_of_potential_moves.append(position_2)
            list_of_potential_moves.append(position_3)
            list_of_potential_moves.append(position_4)
        if bdict_[piece][1] == '8' and bdict_[piece][0] + str(7) in list(bdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(black_list,wdict_,bdict_,'B')
        else:
            bdict_, wdict_ = check_piece_1(list_of_potential_moves, piece, bdict_, wdict_)
    return wdict_,bdict_


def horse(piece,wdict_,bdict_):
    if piece[0] == 'W':
        print("White")
        num_place_1 = int(wdict_[piece][1]) + 1  # move one forward horizontally
        num_place_2 = int(wdict_[piece][1]) - 1  # move one backward horizontally
        num_place_3 = int(wdict_[piece][1]) + 2  # moving two places horizontally
        num_place_4 = int(wdict_[piece][1]) - 2  # moving two places backward horizontally

        pos_place_1 = chr(ord(wdict_[piece][0]) - 1) + str(num_place_3)  # move two places right and move up one
        pos_place_2 = chr(ord(wdict_[piece][0]) + 1) + str(num_place_3)  # move two places right and move down on
        pos_place_3 = chr(ord(wdict_[piece][0]) - 2) + str(num_place_1)  # move one place right and move two places up
        pos_place_4 = chr(ord(wdict_[piece][0]) + 2) + str(num_place_1)  # move one place right move two places down
        pos_place_5 = chr(ord(wdict_[piece][0]) - 1) + str(num_place_2)  # move two places left and move up one
        pos_place_6 = chr(ord(wdict_[piece][0]) + 1) + str(num_place_2)  # move two places left and move down one
        pos_place_7 = chr(ord(wdict_[piece][0]) - 2) + str(num_place_4)  # move one place left and move two places up
        pos_place_8 = chr(ord(wdict_[piece][0]) + 2) + str(num_place_4)  # move one place left and move two places down
        list_of_potential_places = [pos_place_1, pos_place_2, pos_place_3, pos_place_4, pos_place_5, pos_place_6,
                                    pos_place_7, pos_place_8]
        wdict_, bdict_ = check_piece_1(list_of_potential_places, piece, wdict_, bdict_)
    else:
        print("Black")
        num_place_1 = int(bdict_[piece][1]) + 1  # move one forward horizontally
        num_place_2 = int(bdict_[piece][1]) - 1  # move one backward horizontally
        num_place_3 = int(bdict_[piece][1]) + 2  # moving two places horizontally
        num_place_4 = int(bdict_[piece][1]) - 2  # moving two places backward horizontally

        pos_place_1 = chr(ord(bdict_[piece][0])-1) + str(num_place_4) # move two places left and move up one
        pos_place_2 = chr(ord(bdict_[piece][0])+1) + str(num_place_4) # move two places left and move down one
        pos_place_3 = chr(ord(bdict_[piece][0])-1) + str(num_place_3) # move two places right and move up one
        pos_place_4 = chr(ord(bdict_[piece][0])+1) + str(num_place_3) # move two places right and move down one
        pos_place_5 = chr(ord(bdict_[piece][0])-2) + str(num_place_2) # move one place left and move two places up
        pos_place_6 = chr(ord(bdict_[piece][0])+2) + str(num_place_2) # move one place left and move two places down
        pos_place_7 = chr(ord(bdict_[piece][0])-2) + str(num_place_1) # move one place right and move two places up
        pos_place_8 = chr(ord(bdict_[piece][0])+2) + str(num_place_1) # move one place right and move two places down

        list_of_potential_places = [pos_place_1,pos_place_2,pos_place_3,pos_place_4,pos_place_5,pos_place_6,pos_place_7,pos_place_8]
        bdict_,wdict_ = check_piece_1(list_of_potential_places,piece,bdict_,wdict_)

    return wdict_,bdict_

def bishop(piece,wdict_,bdict_):
    white_list = ['WR1', 'WH1', 'WB1', 'WK1', 'WQ1', 'WB2', 'WH2', 'WR2', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6',
                  'WP7', 'WP8']
    black_list = ['BR1', 'BH1', 'BB1', 'BK1', 'BQ1', 'BB2', 'BH2', 'BR2', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6',
                  'BP7', 'BP8']
    if piece[0] == 'W':
        print("White")
        list_of_potential_places = []
        for num_letter in range(1,9):
            for num_number in range(1,9):
                position_1 = chr(ord(wdict_[piece][0]) + num_letter) + str(num_number + 1)
                position_2 = chr(ord(wdict_[piece][0]) + num_letter) + str(num_number - 1)
                position_3 = chr(ord(wdict_[piece][0]) - num_letter) + str(num_number + 1)
                position_4 = chr(ord(wdict_[piece][0]) - num_letter) + str(num_number - 1)
                list_of_potential_places.append(position_1)
                list_of_potential_places.append(position_2)
                list_of_potential_places.append(position_3)
                list_of_potential_places.append(position_4)
        print(list_of_potential_places)

        if wdict_[piece][1] == '1' and chr(ord(wdict_[piece][0])-1) + str(2) in list(wdict_.values()) and chr(ord(wdict_[piece][0])+1) + str(2) in list(wdict_.values()):
            print("Invalid piece. You cannot use this piece")
            piece_input_validation(white_list,wdict_,bdict_,'W')
        else:
            wdict_,bdict_ = check_piece_1(list_of_potential_places,piece,wdict_,bdict_)
    elif piece[0] == 'B':
        print("Black")
        list_of_potential_places = []
        for num_letter in range(1,9):
            for num_number in range(1,9):
                position_1 = chr(ord(bdict_[piece][0]) + num_letter) + str(num_number + 1)
                position_2 = chr(ord(bdict_[piece][0]) + num_letter) + str(num_number - 1)
                position_3 = chr(ord(bdict_[piece][0]) - num_letter) + str(num_number + 1)
                position_4 = chr(ord(bdict_[piece][0]) - num_letter) + str(num_number - 1)
                list_of_potential_places.append(position_1)
                list_of_potential_places.append(position_2)
                list_of_potential_places.append(position_3)
                list_of_potential_places.append(position_4)
        print(list_of_potential_places)
        if bdict_[piece][1] == '8' and chr(ord(bdict_[piece][0])-1) + str(7) in list(bdict_.values()) and chr(ord(bdict_[piece][0])+1) + str(7) in list(bdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(black_list,wdict_,bdict_,'B')
        else:
            bdict_,wdict_ = check_piece_1(list_of_potential_places,piece,bdict_,wdict_)

    return wdict_,bdict_

def king(piece,wdict_,bdict_):
    white_list = ['WR1', 'WH1', 'WB1', 'WK1', 'WQ1', 'WB2', 'WH2', 'WR2', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6',
                  'WP7', 'WP8']
    black_list = ['BR1', 'BH1', 'BB1', 'BK1', 'BQ1', 'BB2', 'BH2', 'BR2', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6',
                  'BP7', 'BP8']
    if piece[0] == 'W':
        print("White")
        num_place_1 = int(wdict_[piece][1]) + 1  #moving forward horizontally
        num_place_2 = int(wdict_[piece][1]) - 1  #moving backward horizontally

        possible_position_1 = wdict_[piece][0] + str(num_place_1)  #moving forward horizontally
        possible_position_2 = wdict_[piece][0] + str(num_place_2) #moving backwards horizontally
        possible_position_3 = chr(ord(wdict_[piece][0]) + 1) + wdict_[piece][1] #moving down vertically
        possible_position_4 = chr(ord(wdict_[piece][0]) - 1) + wdict_[piece][1] #moving up vertically
        possible_position_5 = chr(ord(wdict_[piece][0]) + 1) + str(num_place_1) # move up diagonally to the right
        possible_position_6 = chr(ord(wdict_[piece][0]) - 1) + str(num_place_1) # move down diagonally to the right
        possible_position_7 = chr(ord(wdict_[piece][0]) + 1) + str(num_place_2) # move up diagonally to the left
        possible_position_8 = chr(ord(wdict_[piece][0]) - 1) + str(num_place_2) # move down diagonally to the left
        list_of_potential_places = [possible_position_1, possible_position_2, possible_position_3, possible_position_4,
                                    possible_position_5, possible_position_6,possible_position_7,possible_position_8]

        if possible_position_1 in list(wdict_.values()) and possible_position_5 in list(wdict_.values()) and possible_position_6 in list(wdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(white_list,wdict_,bdict_,'W')
        else:
            wdict_,bdict_ = check_piece_1(list_of_potential_places,piece,wdict_,bdict_)
    elif piece[0] == 'B':
        print("Black")
        num_place_1 = int(bdict_[piece][1]) - 1 # moves forward
        num_place_2 = int(bdict_[piece][1]) + 1 #moves back

        possible_position_1 = bdict_[piece][0] + str(num_place_1) #moving forward horizontally
        possible_position_2 = bdict_[piece][0] + str(num_place_2) # moving backward horizontally
        possible_position_3 = chr(ord(bdict_[piece][0]) + 1) + bdict_[piece][1] #moving down vertically
        possible_position_4 = chr(ord(bdict_[piece][0]) - 1) + bdict_[piece][1] #moving up vertically
        possible_position_5 = chr(ord(bdict_[piece][0]) + 1) + str(num_place_1) #moving down diagonally
        possible_position_6 = chr(ord(bdict_[piece][0]) - 1) + str(num_place_1) #moving up diagonally
        possible_position_7 = chr(ord(bdict_[piece][0]) + 1) + str(num_place_2)  # move up diagonally to the left
        possible_position_8 = chr(ord(bdict_[piece][0]) - 1) + str(num_place_2)  # move down diagonally to the left
        list_of_potential_places = [possible_position_1, possible_position_2, possible_position_3, possible_position_4,
                                    possible_position_5, possible_position_6,possible_position_7,possible_position_8]

        if possible_position_1 in list(bdict_.values()) and possible_position_5 in list(bdict_.values()) and possible_position_6 in list(bdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(black_list,wdict_,bdict_,'B')
        else:
            bdict_,wdict_ = check_piece_1(list_of_potential_places,piece,bdict_,wdict_)

    return wdict_,bdict_

def queen(piece,wdict_,bdict_):
    white_list = ['WR1', 'WH1', 'WB1', 'WK1', 'WQ1', 'WB2', 'WH2', 'WR2', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6',
                  'WP7', 'WP8']
    black_list = ['BR1', 'BH1', 'BB1', 'BK1', 'BQ1', 'BB2', 'BH2', 'BR2', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6',
                  'BP7', 'BP8']
    if piece[0] == 'W':
        print("White")
        list_of_potential_places = []
        for num in range(1,9): # same as a rook
            position_1 = wdict_[piece][0] + str(num) #moving right
            position_2 = wdict_[piece][0] + str(num) #moving left
            position_3 = chr(ord(wdict_[piece][0])+num) + wdict_[piece][1] #moving down
            position_4 = chr(ord(wdict_[piece][0])-num) + wdict_[piece][1] #moving up
            list_of_potential_places.append(position_1)
            list_of_potential_places.append(position_2)
            list_of_potential_places.append(position_3)
            list_of_potential_places.append(position_4)
        for num_letter in range(1,9): # acts as a bishop
            for num_number in range(1,9):
                position_5 = chr(ord(wdict_[piece][0]) + num_letter) + str(num_number + 1)
                position_6 = chr(ord(wdict_[piece][0]) + num_letter) + str(num_number - 1)
                position_7 = chr(ord(wdict_[piece][0]) - num_letter) + str(num_number + 1)
                position_8 = chr(ord(wdict_[piece][0]) - num_letter) + str(num_number - 1)
                list_of_potential_places.append(position_5)
                list_of_potential_places.append(position_6)
                list_of_potential_places.append(position_7)
                list_of_potential_places.append(position_8)

        if wdict_[piece][0] + str(2) in list(wdict_.values()) and chr(ord(wdict_[piece][0]) -1) + str(2) in list(wdict_.values()) and chr(ord(wdict_[piece][0])+1) + str(2) in list(wdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(white_list,wdict_,bdict_,'W')
        else:
            wdict_,bdict_ = check_piece_1(list_of_potential_places,piece,wdict_,bdict_)


    else:
        print("Black")
        list_of_potential_places = []
        for num in range(1, 9):  # same as a rook
            position_1 = bdict_[piece][0] + str(num)  # moving right
            position_2 = bdict_[piece][0] + str(num)  # moving left
            position_3 = chr(ord(bdict_[piece][0]) + num) + bdict_[piece][1]  # moving down
            position_4 = chr(ord(bdict_[piece][0]) - num) + bdict_[piece][1]  # moving up
            list_of_potential_places.append(position_1)
            list_of_potential_places.append(position_2)
            list_of_potential_places.append(position_3)
            list_of_potential_places.append(position_4)
        for num_letter in range(1,9): # acts like a bishop
            for num_number in range(1,9):
                position_5 = chr(ord(bdict_[piece][0]) + num_letter) + str(num_number + 1)
                position_6 = chr(ord(bdict_[piece][0]) + num_letter) + str(num_number - 1)
                position_7 = chr(ord(bdict_[piece][0]) - num_letter) + str(num_number + 1)
                position_8 = chr(ord(bdict_[piece][0]) - num_letter) + str(num_number - 1)
                list_of_potential_places.append(position_5)
                list_of_potential_places.append(position_6)
                list_of_potential_places.append(position_7)
                list_of_potential_places.append(position_8)
        if bdict_[piece][0] + str(7) in list(bdict_.values()) and chr(ord(bdict_[piece][0]) -1) + str(7) in list(bdict_.values()) and chr(ord(bdict_[piece][0])+1) + str(7) in list(bdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(black_list,wdict_,bdict_,'B')
        else:
            bdict_,wdict_ = check_piece_1(list_of_potential_places,piece,bdict_,wdict_)

    return wdict_,bdict_

def check_piece_1(list_of_potential_places,piece,dict_,dict_2):

    new_location = check_piece_location_validation(piece, dict_)
    while True:
        if new_location in list_of_potential_places:
            if new_location in dict_2.values():
                if piece[0:2] == 'WP':
                    if chr(ord(dict_[piece][0]) - 1) + str(int(dict_[piece][1]) + 1) == new_location or chr(ord(dict_[piece][0]) + 1) + str(int(dict_[piece][1]) + 1) == new_location:
                        dict_[piece] = new_location
                        dict_2 = remove_piece_in_dict(dict_2,new_location)
                        return dict_, dict_2

                    else:
                        print("Invalid location.")
                        new_location = check_piece_location_validation(piece,dict_)
                elif piece[0:2] == 'BP':
                    if chr(ord(dict_[piece][0]) - 1) + str(int(dict_[piece][1]) - 1) == new_location or chr(ord(dict_[piece][0]) + 1) + str(int(dict_[piece][1]) - 1) == new_location:
                        dict_[piece] = new_location
                        dict_2 = remove_piece_in_dict(dict_2, new_location)
                        return dict_, dict_2
                    else:
                        print("Invalid location.")
                        new_location = check_piece_location_validation(piece, dict_)
                else:
                    dict_[piece] = new_location
                    dict_2 = remove_piece_in_dict(dict_2, new_location)
                    return dict_, dict_2
            else:
                dict_[piece] = new_location
                return dict_, dict_2
        else:
            print("Invalid location.")
            new_location = check_piece_location_validation(piece, dict_)

def pawn(piece,wdict_,bdict_):
    '''Pawn can only move one once horizontally, except if the opposite team has a piece diagonally to the pawn'''
    white_list = ['WR1', 'WH1', 'WB1', 'WK1', 'WQ1', 'WB2', 'WH2', 'WR2', 'WP1', 'WP2', 'WP3', 'WP4', 'WP5', 'WP6',
                  'WP7', 'WP8']
    black_list = ['BR1', 'BH1', 'BB1', 'BK1', 'BQ1', 'BB2', 'BH2', 'BR2', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6',
                  'BP7', 'BP8']
    if piece[0] == 'W':
        num_place_1 = int(wdict_[piece][1]) + 1
        num_place_2 = int(wdict_[piece][1]) + 2
        possible_location_1 = wdict_[piece][0] + str(num_place_1) #Moving forward one place
        possible_location_2 = wdict_[piece][0] + str(num_place_2) #Moving forward two places
        possible_location_3 = chr(ord(wdict_[piece][0]) + 1) + str(num_place_1) #moving diagonally down
        possible_location_4 = chr(ord(wdict_[piece][0]) - 1) + str(num_place_1) #moving diagonally up

        list_of_potential_places = [possible_location_1,possible_location_2,possible_location_3,possible_location_4]
        if wdict_[piece][1] != '2':
            list_of_potential_places.remove(possible_location_2)
        if possible_location_3 not in list(bdict_.values()):
            list_of_potential_places.remove(possible_location_3)
        if possible_location_4 not in list(bdict_.values()):
            list_of_potential_places.remove(possible_location_4)
        if wdict_[piece][0] + str(int(wdict_[piece][1]) + 1) in list(bdict_.values()) or wdict_[piece][0] + str(int(wdict_[piece][1]) + 1) in list(wdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(white_list,wdict_,bdict_,'W')
        else:
            wdict_,bdict_ = check_piece_1(list_of_potential_places,piece,wdict_,bdict_)

    else:
        print("Black")
        num_place_1 = int(bdict_[piece][1]) - 1
        num_place_2 = int(bdict_[piece][1]) - 2
        possible_location_1 = bdict_[piece][0] + str(num_place_1)
        possible_location_2 = bdict_[piece][0] + str(num_place_2)
        possible_location_3 = chr(ord(bdict_[piece][0]) - 1) + str(num_place_1)
        possible_location_4 = chr(ord(bdict_[piece][0]) + 1) + str(num_place_1)

        list_of_potential_places = [possible_location_1, possible_location_2, possible_location_3, possible_location_4]
        if bdict_[piece][1] != '7':
            list_of_potential_places.remove(possible_location_2)
        if possible_location_3 not in list(wdict_.values()):
            list_of_potential_places.remove(possible_location_3)
        if possible_location_4 not in list(wdict_.values()):
            list_of_potential_places.remove(possible_location_4)
        if bdict_[piece][0] + str(int(bdict_[piece][1]) - 1) in list(wdict_.values()) or bdict_[piece][0] + str(int(bdict_[piece][1]) - 1) in list(bdict_.values()):
            print("Invalid piece. You cannot use this piece.")
            piece_input_validation(black_list,wdict_,bdict_,'B')
        else:
            bdict_,wdict_ = check_piece_1(list_of_potential_places,piece,bdict_,wdict_)


    return wdict_, bdict_

def main():
    white_list = ['WR1','WH1','WB1','WK1','WQ1','WB2','WH2','WR2','WP1','WP2','WP3','WP4','WP5','WP6','WP7','WP8']
    black_list = ['BR1','BH1','BB1','BK1','BQ1','BB2','BH2','BR2','BP1','BP2','BP3','BP4','BP5','BP6','BP7','BP8']
    white_dict = {'WR1':'A1','WH1': 'B1','WB1':'C1','WK1':'D1','WQ1':'E1','WB2':'F1','WH2':'G1','WR2':'H1','WP1':'A2','WP2':'B2','WP3':'C2','WP4':'D2','WP5':'E2','WP6':'F2','WP7':'G2','WP8':'H2'}
    black_dict = {'BR1':'A8','BH1': 'B8','BB1':'C8','BK1':'D8','BQ1':'E8','BB2':'F8','BH2':'G8','BR2':'H8','BP1':'A7','BP2':'B7','BP3':'C7','BP4':'D7','BP5':'E7','BP6':'F7','BP7':'G7','BP8':'H7'}
    now = datetime.now()
    date_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(date_string)
    print("\nWelcome to Chess.")
    print("W stands for white | B stands for black")
    print("K stands for King  | Q stands for Queen")
    print("H stands for Horse | B stands for Bishop")
    print("R stands for Rook  | P stands for Pawn")
    print("\n")
    print("The chess starts to left to right. The first input requires the color, piece, and number.")
    print("So, if you wanted to move a pawn ahead of the rook upper left, you type 'WP1.")
    print("The second input requires a location. The row is letters and column is numbers.")
    print("For 'WP1', you type in 'A3' or 'A4'.")
    print('\n')
    subprocess.call(['say',"Welcome to Chess   The chess starts to left to right The first input requires the color piece and number  So if you wanted to move a pawn ahead of the rook upper left you type 'WP1'  The second input requires a location  The row is letters and column is numbers   For 'WP1' you type in A3 or A4"])

    while "WK1" in white_dict and 'BK1' in black_dict:
        game_board = update_game_board(white_dict, black_dict)
        print_game_board(game_board)
        white_dict,black_dict = piece_input_validation(white_list,white_dict,black_dict,'W')
        print("\n")
        game_board = update_game_board(white_dict, black_dict)
        print_game_board(game_board)
        if 'BK1' not in black_dict:
            break
        white_dict,black_dict = piece_input_validation(black_list,white_dict,black_dict,'B')
        print("\n")
    if 'WK1' not in white_dict:
        subprocess.call(['say', "Checkmate, Black wins."])
        write_file(white_dict, black_dict,'B',date_string)

    elif 'BK1' not in black_dict:
        subprocess.call(['say', "Checkmate, White wins."])
        write_file(white_dict,black_dict,'W',date_string)


if __name__ == '__main__':main()