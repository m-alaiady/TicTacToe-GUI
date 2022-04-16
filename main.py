from tkinter import *
from tkinter import messagebox
from functools import partial  # for allowing sending arguments inside command attribute
from game_status import *

WINDOW_SIZE = "250x250"
PAD_Y = 57
WIDTH = 100
FONT_FAMILY = 'Arial'
FONT_SIZE = 12
BORDER_SIZE = 5

info = {
    'current_player': 'x',
    'steps_counter': 0,
    'board': [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
}


def reset():
    global info
    info = {
        'current_player': 'x',
        'steps_counter': 0,
        'board': [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
    }


def is_taken(pos, index):
    if info['board'][pos][index] == "x" or info['board'][pos][index] == "o":
        return True
    else:
        return False


def check_draw(window):
    if info['steps_counter'] >= 9:
        messagebox.showinfo("Game status", "Draw")
        window.destroy()
        reset() # reset all values to default
        root() # back to main menu


def check_if_win(window):
    if check_win(info):
        change_player()
        messagebox.showinfo("Game status", info['current_player'] + " is winner")
        window.destroy()
        reset() # reset all values to default
        root() # back to main menu


def is_finish(window):
    if check_if_win(window) or check_draw(window):
        return True
    else:
        return False


def change_player():
    if info['current_player'] == 'x':
        info['current_player'] = 'o'
    else:
        info['current_player'] = 'x'


def root():
    root = Tk()
    root.geometry(WINDOW_SIZE)
    root.title("Tic Tac Toe GUI")
    Label(root, text="Choose playing mode", font=(FONT_FAMILY, FONT_SIZE)).pack(pady=PAD_Y)

    Button(root, text="2 Players", command=partial(choose_character, root), width=WIDTH, font=(FONT_FAMILY, FONT_SIZE), bd=BORDER_SIZE).pack()
    Button(root, text="Computer", command=partial(choose_character, root), width=WIDTH, font=(FONT_FAMILY, FONT_SIZE), bd=BORDER_SIZE).pack()
    Button(root, text="Exit", command=lambda: root.destroy(), width=WIDTH, font=(FONT_FAMILY, FONT_SIZE), bd=BORDER_SIZE).pack()

    root.mainloop()


def back_to_main(window):
    window.destroy()
    root()


def choose_character(root):
    root.destroy()
    window = Tk()
    window.geometry(WINDOW_SIZE)

    Label(window, text="Who will start first?", font=(FONT_FAMILY, FONT_SIZE)).pack(pady=PAD_Y)
    Button(window, text="X", command=partial(draw_board, window), width=WIDTH, font=(FONT_FAMILY, FONT_SIZE), bd=BORDER_SIZE).pack()
    Button(window, text="O", command=partial(draw_board, window, True), width=WIDTH, font=(FONT_FAMILY, FONT_SIZE), bd=BORDER_SIZE).pack()
    Button(window, text="Back", command=partial(back_to_main, window), width=WIDTH, font=(FONT_FAMILY, FONT_SIZE), bd=BORDER_SIZE).pack()

    window.mainloop()


def draw_board(root, o_player = False):
    if(o_player):
        info['current_player'] = 'o'

    root.destroy()
    window = Tk()
    window.geometry("345x255")

    Button(window, text=info['board'][0][0], height=5, width=15, command=lambda: change_text(window, 0, 0)).grid(row=0, column=0),
    Button(window, text=info['board'][0][1], height=5, width=15, command=lambda: change_text(window, 0, 1)).grid(row=0, column=1),
    Button(window, text=info['board'][0][2], height=5, width=15, command=lambda: change_text(window, 0, 2)).grid(row=0, column=2),

    Button(window, text=info['board'][1][0], height=5, width=15, command=lambda: change_text(window, 1, 0)).grid(row=1, column=0),
    Button(window, text=info['board'][1][1], height=5, width=15, command=lambda: change_text(window, 1, 1)).grid(row=1, column=1),
    Button(window, text=info['board'][1][2], height=5, width=15, command=lambda: change_text(window, 1, 2)).grid(row=1, column=2),

    Button(window, text=info['board'][2][0], height=5, width=15, command=lambda: change_text(window, 2, 0)).grid(row=2, column=0),
    Button(window, text=info['board'][2][1], height=5, width=15, command=lambda: change_text(window, 2, 1)).grid(row=2, column=1),
    Button(window, text=info['board'][2][2], height=5, width=15, command=lambda: change_text(window, 2, 2)).grid(row=2, column=2),

    check_if_win(window)
    check_draw(window)

    window.mainloop()


def change_text(root, pos, index):
    if not is_taken(pos, index):
        info['steps_counter'] += 1
        info['board'][pos][index] = info['current_player']
        change_player()
    else:
        messagebox.showinfo("Position conflict", "position taken, choose another one")

    draw_board(root)


if __name__ == '__main__':
    root()




