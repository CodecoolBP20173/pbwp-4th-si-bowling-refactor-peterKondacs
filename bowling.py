def score(game):
    """
    Calculates the the score for a bowling game.

    Args:
        game: a series of characters each representing a roll of the player.

    Returns: the final score as an integer based on the given rolls.
    """

    NUMBER_OF_FRAMES = 10
    result = 0
    actual_frame = 1
    in_first_try = True
    for i in range(len(game)):
        if actual_frame <= NUMBER_OF_FRAMES:
            if game[i] == '/':
                result += count_spare_score(game[i-1], game[i+1])
            elif game[i] in ['X', 'x']:
                result += count_strike_score(game[i+1], game[i+2])
                in_first_try = True
                actual_frame += 1
            else:
                result += get_value(game[i])
            if not in_first_try:
                actual_frame += 1
            if game[i] not in ['X', 'x']:
                in_first_try = not in_first_try
    return result


def get_value(char):
    """
    Gives the score value of the given character.

    Args:
        char: a character representing the result of a roll in a bowling game.

    Returns: the score value as an integer for a given roll
    """

    if char in [str(i) for i in range(10)]:
        return int(char)
    elif char in ['X', 'x', '/']:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def count_spare_score(last_roll, next_roll):
    """
    Makes the modified score calculation for a spare roll.

    Args:
        last_roll: the character that represents the last roll
        next_roll: the character that represents the next roll

    Returns: the modified score of a spare roll as an integer.
    """

    score = 0
    score += get_value('/') - get_value(last_roll)
    score += get_value(next_roll)
    return score


def count_strike_score(next_roll, roll_after_next):
    """
    Makes the modified score calculation for a strike roll.

    Args:
        last_roll: the character that represents the next roll
        roll_after_next: the character that represents the roll after the next roll

    Returns: the modified score of a strike roll as an integer.
    """

    score = 0
    score += get_value('X')
    score += get_value(next_roll) + get_value(roll_after_next)
    if roll_after_next == '/':
        score -= get_value(next_roll)
    return score
