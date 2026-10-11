from logic_utils import check_guess, parse_guess, start_new_game, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, the hint should say to go lower.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, the hint should say to go higher.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_parse_guess():
    assert parse_guess("42") == (True, 42, None)
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess(" 42 ") == (True, 42, None)
    assert parse_guess("42.9") == (False, None, "Enter a whole number.")
    assert parse_guess("not a number") == (False, None, "Enter a whole number.")


def test_update_score():
    assert update_score(0, "Win", 1) == 80
    assert update_score(10, "Too High", 2) == 15
    assert update_score(10, "Too Low", 1) == 5


def test_start_new_game_resets_game_state():
    state = {
        "secret": 50,
        "attempts": 4,
        "status": "won",
        "history": [25, 50],
    }

    start_new_game(state, 1, 1)

    assert state == {
        "secret": 1,
        "attempts": 0,
        "status": "playing",
        "history": [],
    }
