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