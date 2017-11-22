NUMBER_OF_FRAMES = 10


def score(game):
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
    if char in [str(i) for i in range(10)]:
        return int(char)
    elif char in ['X', 'x', '/']:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def count_spare_score(last_roll, next_roll):
    score = 0
    score += get_value('/') - get_value(last_roll)
    score += get_value(next_roll)
    return score


def count_strike_score(next_roll, roll_after_next):
    score = 0
    score += get_value('X')
    score += get_value(next_roll) + get_value(roll_after_next)
    if roll_after_next == '/':
        score -= get_value(next_roll)
    return score
