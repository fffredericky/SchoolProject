"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """ Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
        True
    >>> is_win('apple', 'a^^le')
        False
    """
    # put the function body here
    return puzzle == view

def game_over(puzzle: str, view: str, current_selection: str) -> bool:
    """ Return True if and only if the puzzle is the same as the view or the 
    current_selection is QUIT.
    
    >>> game_over('apple', 'appl^', 'Q')
        True
    >>> game_over('apple', 'a^^le', 'C')
        False
    """
    
    return puzzle == view or current_selection == 'Q'

def bonus_letter(puzzle: str, view: str, letter_to_evaluate: str) -> bool:
    """ Return True if and only if letter_to_evaluate appears in the puzzle 
    but not in the view.
    
    >>> bonus_letter('apple', 'appl^', 'e')
        True
    >>> bonus_letter('apple', 'appl^', 'x')
        False
    """
    
    return letter_to_evaluate in puzzle and  not letter_to_evaluate in view

def update_letter_view(puzzle: str, view: str, index_of_character: int, \
    guess_letter: str) -> str:
    """ Return a single character string representing the view of the 
    character at the index of index_of_character. If the character at that index 
    of the puzzle matches the guess_letter, then return that character. 
    Otherwise, return the character at index_of_character of the view.
    
    >>> update_letter_view('apple' ,'appl^', 4, 'z')
        '^'
    >>> update_letter_view('apple', 'appl^', 4, 'e')
        'e'
    """
    
    if puzzle[index_of_character: (index_of_character + 1)] == guess_letter:
        return guess_letter
    return view[index_of_character: (index_of_character + 1)]
    
def calculate_score(current_score: int, number_of_occurrences: int, \
    type_of_letter: str) -> int:
    """ Return the new score by adding CONSONANT_POINTS number_of_occurrences 
    times to current_score if type_of_letter is a consonant, or by 
    deducting the VOWEL_PRICE from current_score if type_of_letter is a vowel.
    
    >>> calculate_score(12, 3, 'C')
        15
    >>> calculate_score(12, 1, 'V')
        11
    """
    
    if type_of_letter == 'C':
        return current_score + number_of_occurrences
    elif type_of_letter == 'V':
        return current_score - 1

def next_player(current_player: str, number_of_occurrences: int) -> str:
    """ If and only if number_of_occurrences is greater than zero, 
    current_player plays again. Return the next player 
    (one of PLAYER_ONE or PLAYER_TWO).
    
    >>> next_player(PLAYER_ONE, 0)
        'Player Two'
    >>> next_player(PLAYER_ONE, 1)
        'Player One'
    """
    
    if current_player == PLAYER_ONE:
        if number_of_occurrences > 0:
            return PLAYER_ONE
        return PLAYER_TWO
    elif current_player == PLAYER_TWO:
        if number_of_occurrences > 0:
            return PLAYER_TWO
        return PLAYER_ONE