import random

choiсe_1 = '⭕'
choiсe_2 = '❌'


# Example greed with numbers
example_line_1 = ['1', "|", "2", "|", '3']
example_line_2 = ['4', "|", "5", "|", '6']
example_line_3 = ['7', "|", "8", "|", '9']
hor_board = ['---------']


list_for_grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def print_grid():
    print(f"{list_for_grid[0]} | {list_for_grid[1]} | {list_for_grid[2]}\n"
          f"---------\n"
          f"{list_for_grid[3]} | {list_for_grid[4]} | {list_for_grid[5]}\n"
          f"---------\n"
          f"{list_for_grid[6]} | {list_for_grid[7]} | {list_for_grid[8]}\n")


#For printing example greed with numbers
def print_lines(line1, line2, line3):
      print(f"{' '.join(line1)}\n"
            f"{''.join(hor_board)}\n"
            f"{' '.join(line2)}\n"
            f"{''.join(hor_board)}\n"
            f"{' '.join(line3)}\n")


def play_game():
    user_choice = int(input('Based on the numerical arrangement above, choose a number to draw the sign: '))
    if user_choice not in numbers:
        print("\nThe cell is already occupied. Try again")
    else:
        list_for_grid[user_choice - 1] = user_sign
        numbers.remove(user_choice)
        if len(numbers) != 0:
            computer_choice = random.choice(numbers)
            list_for_grid[computer_choice - 1] = AI_sign
            numbers.remove(computer_choice)
    print_grid()


def check_winner():
    for id in winning_positions:
        if list_for_grid[id[0]] == user_sign and list_for_grid[id[1]] == user_sign and list_for_grid[id[2]] == user_sign:
            return 'My congratulations! You won!'
        elif list_for_grid[id[0]] == AI_sign and list_for_grid[id[1]] == AI_sign and list_for_grid[id[2]] == AI_sign:
            return 'So sorry! AI was better this time!'


end_of_game = False

while input('Do you want to play Tic Tac Toe? Type "y" or "n": ') == 'y':
    # Ask User to choose sign
    ask_user = input("Choose which side you're on. 0 for ⭕ and 1 for ❌: ")
    if ask_user == 0:
        user_sign = choiсe_1
        AI_sign = choiсe_2
    else:
        AI_sign = choiсe_1
        user_sign = choiсe_2

    print(f"\nYour sign: {user_sign}\n"
          f"Computer sign: {AI_sign}\n")

    print_lines(example_line_1, example_line_2, example_line_3)

    while end_of_game == False:
        user_choice = int(input('Based on the numerical arrangement above, choose a number to draw the sign: '))
        if user_choice not in numbers:
            print("\nThe cell is already occupied. Try again")
        else:
            list_for_grid[user_choice - 1] = user_sign
            numbers.remove(user_choice)
            if len(numbers) != 0:
                computer_choice = random.choice(numbers)
                list_for_grid[computer_choice - 1] = AI_sign
                numbers.remove(computer_choice)
        print_grid()

        if check_winner():
            end_of_game = True
            print(check_winner())
        elif not check_winner() and len(numbers) == 0:
            end_of_game = True
            print('Tie! This time :)')


