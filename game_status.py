def check_win(info):
    if info['board'][0][0] == info['board'][0][1] == info['board'][0][2] != "":
        return True

    if info['board'][1][0] == info['board'][1][1] == info['board'][1][2] != "":
        return True

    if info['board'][2][0] == info['board'][2][1] == info['board'][2][2] != "":
        return True

    if info['board'][0][0] == info['board'][1][0] == info['board'][2][0] != "":
        return True

    if info['board'][0][1] == info['board'][1][1] == info['board'][2][1] != "":
        return True

    if info['board'][0][2] == info['board'][1][2] == info['board'][2][2] != "":
        return True

    if info['board'][0][0] == info['board'][1][1] == info['board'][2][2] != "":
        return True

    if info['board'][0][2] == info['board'][1][1] == info['board'][2][0] != "":
        return True

    return False


def block_win(info, letter):
    if info['board'][0][0] == info['board'][0][1] == letter and info['board'][0][2] == " ":
        info['board'][0][2] = 'O'
        return True

    if info['board'][0][0] == info['board'][0][2] == letter and info['board'][0][1] == " ":
        info['board'][0][1] = 'O'
        return True

    if info['board'][0][1] == info['board'][0][2] == letter and info['board'][0][0] == " ":
        info['board'][0][0] = 'O'
        return True

    # Check second row
    if info['board'][1][0] == info['board'][1][1] == letter and info['board'][1][2] == " ":
        info['board'][1][2] = 'O'
        return True

    if info['board'][1][0] == info['board'][1][2] == letter and info['board'][1][1] == " ":
        info['board'][1][1] = 'O'
        return True

    if info['board'][1][1] == info['board'][1][2] == letter and info['board'][1][0] == " ":
        info['board'][1][0] = 'O'
        return True

    # Third row
    if info['board'][1][0] == info['board'][1][1] == letter and info['board'][2][2] == " ":
        info['board'][1][2] = 'O'
        return True

    if info['board'][1][0] == info['board'][1][2] == letter and info['board'][2][1]== " ":
        info['board'][1][1] = 'O'
        return True

    if info['board'][1][1] == info['board'][1][2] == letter and info['board'][2][0] == " ":
        info['board'][1][0] = 'O'
        return True

    if info['board'][0][0] == info['board'][1][0] == letter and info['board'][1][0] == " ":
        info['board'][1][0] = 'O'
        return True

    if info['board'][0][0] == info['board'][1][0] == letter and info['board'][1][0] == " ":
        info['board'][1][0] = 'O'
        return True

    if info['board'][1][0] == info['board'][1][0] == letter and info['board'][0][0] == " ":
        info['board'][0][0] = 'O'
        return True

    if info['board'][0][1] == info['board'][1][1] == letter and info['board'][2][1] == " ":
        info['board'][1][1] = 'O'
        return True

    if info['board'][0][1] == info['board'][1][1] == letter and info['board'][1][1] == " ":
        info['board'][1][1] = 'O'
        return True

    if info['board'][1][1] == info['board'][1][1] == letter and info['board'][0][1] == " ":
        info['board'][0][1] = 'O'
        return True

    if info['board'][0][2] == info['board'][1][2] == letter and info['board'][1][2] == " ":
        info['board'][1][2] = 'O'
        return True

    if info['board'][0][2] == info['board'][1][2] == letter and info['board'][1][2] == " ":
        info['board'][1][2] = 'O'
        return True

    if info['board'][1][2] == info['board'][1][2] == letter and info['board'][0][2] == " ":
        info['board'][0][2] = 'O'
        return True

    if info['board'][0][0] == info['board'][1][1] == letter and info['board'][1][2] == " ":
        info['board'][1][2] = 'O'
        return True

    if info['board'][0][0] == info['board'][1][2] == letter and info['board'][1][1] == " ":
        info['board'][1][1] = 'O'
        return True

    if info['board'][1][1] == info['board'][1][2] == letter and info['board'][0][0] == " ":
        info['board'][0][0] = 'O'
        return True

    if info['board'][0][2] == info['board'][1][1] == letter and info['board'][1][0] == " ":
        info['board'][1][0] = 'O'
        return True

    if info['board'][0][2] == info['board'][1][0] == letter and info['board'][1][1] == " ":
        info['board'][1][1] = 'O'
        return True

    if info['board'][1][1] == info['board'][1][0] == letter and info['board'][0][2] == " ":
        info['board'][0][2] = 'O'
        return True

    return False