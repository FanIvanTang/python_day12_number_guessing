from tud_test_base import set_keyboard_input

from main import guess_time, user_guess, continue_game


def test_case_1_guuss_time():

    set_keyboard_input(["hard"])

    assert guess_time() == 5


def test_case_2_guuss_time():

    set_keyboard_input(["easy"])

    assert guess_time() == 10


def test_case_3_guuss_time():

    set_keyboard_input(["eAsy"])

    assert guess_time() == 10


def test_case_4_guuss_time():

    set_keyboard_input(["HARD"])

    assert guess_time() == 5


def test_case_1_user_guess():

    set_keyboard_input(["23"])

    assert user_guess(23) == 0


def test_case_2_user_guess():

    set_keyboard_input(["44"])

    assert user_guess(23) == 21


def test_case_3_user_guess():

    set_keyboard_input(["20"])

    assert user_guess(23) == -3


def test_case_1_continue_game():
    set_keyboard_input(["y"])

    assert continue_game() == True


def test_case_2_continue_game():
    set_keyboard_input(["Y"])

    assert continue_game() == True


def test_case_3_continue_game():
    set_keyboard_input(["n"])

    assert continue_game() == False


def test_case_4_continue_game():
    set_keyboard_input(["N"])

    assert continue_game() == False
