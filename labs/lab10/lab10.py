"""
Name: <Christopher Hamilton, II>
<lab10>.py
"""


def build_board():
    position_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return position_list


def display_board(position_list):
    print("_" * 13)
    counter = 0
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(position_list[counter], end=" | ")
            counter += 1
        print("\n")
    print("_" * 13)


def place_spot(position_list, spot, marker):
    position_list[spot] = marker


def legal_spot (position_list, spot):
    if position_list[spot] == "x" or position_list[spot] == "o" or 9 < spot or spot < 0:
        return False
    else:
        return True


def game_won(position_list):
    win_con = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for con in win_con:
        counter = 0
        for spot in con:
            if position_list[spot - 1] == "x":
                counter += 1
            if counter == 3:
                return "x wins"
        counter = 0
        for spot in con:
            if position_list[spot - 1] == "o":
                counter += 1
            if counter == 3:
                return "o wins"


def game_over(position_list, turn_count):
    if game_won(position_list) == "x wins" or game_won(position_list) == "o wins" or turn_count == 9:
        return True
    else:
        return False


def play_game():
    position_list = build_board()
    display_board(position_list)
    turn_count = 0
    game_finished = game_over(position_list, turn_count)
    while not game_finished:
        if turn_count % 2 == 0:
            marker = "x"
            spot = int(input("x you're up! ")) - 1
            if legal_spot(position_list, spot):
                place_spot(position_list, spot, marker)
                turn_count += 1
        else:
            marker = "o"
            spot = int(input("o place your mark! ")) - 1
            if legal_spot(position_list, spot):
                place_spot(position_list, spot, marker)
                turn_count += 1
        display_board(position_list)
        game_finished = game_over(position_list, turn_count)
    if game_won(position_list):
        print(game_won(position_list))
    else:
        print("The winner is kono dio da!!!")


def main():
    play_game()
    pass


main()
