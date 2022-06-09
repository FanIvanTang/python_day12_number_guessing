# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


from art import logo

import random


def generate_a_number(low, high):
    """
    random generate a number between low and high
    """
    print(f"I'm thinking of a number between {low}, and {high} ")
    return random.randint(low, high)


def guess_time():
    """
    base on user input to return guess time
    """

    difficulty_level = {"easy": 10, "hard": 5}

    difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ")

    while difficulty.lower() not in difficulty_level:
        difficulty = input("Opoos, right input, Type 'easy' or 'hard': ")

    return difficulty_level[difficulty.lower()]


def user_guess(right_number):
    """
    base on user input to return negetive too low, positive too high, zero is equal
    """

    user_input = input("Make a guess: ")

    while True:

        try:
            user_number = int(user_input)
            break
        except ValueError:
            user_input = input("Oposs, you have input an integer, Make a guess: ")

    return user_number - right_number


def continue_game():
    """
    base on user input to decide continue game or not
    """

    is_continue = input("Would you like play again? Type 'y' or 'n': ")

    while is_continue.lower() not in ["y", "n"]:
        is_continue = input("Oppos, right input? Type 'y' or 'n': ")

    return is_continue.lower() == "y"


if __name__ == "__main__":

    game_in_process = True

    play_times = 0
    win_times = 0

    while game_in_process:
        print(logo)

        number = generate_a_number(1, 100)
        # print(number)

        attempts = guess_time()

        is_win = False

        while attempts > 0:

            print(f"You have {attempts} attempts remainning to guess the number.")

            low_right_high = user_guess(right_number=number)

            if low_right_high == 0:
                print(f"You got it! The answer was {number}.")
                is_win = True
                win_times += 1
                break
            elif low_right_high < 0:
                print("Too low.\nGuess Again")
            else:
                print("Too high.\nGuess Again")

            attempts -= 1

        if not is_win:
            print("You've run out of guesses, you lose.")

        play_times += 1

        game_in_process = continue_game()

    print(
        f"Thank you play this game,\nyou have played {play_times} times, and won {win_times} times\ngood job,see you again"
    )
