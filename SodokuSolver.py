import PySimpleGUI as sg  # , random


solution = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
            [6, 8, 2, 5, 7, 1, 4, 9, 3],
            [1, 9, 7, 8, 3, 4, 5, 6, 2],
            [8, 2, 6, 1, 9, 5, 3, 4, 7],
            [3, 7, 4, 6, 8, 2, 9, 1, 5],
            [9, 5, 1, 7, 4, 3, 6, 2, 8],
            [5, 1, 9, 3, 2, 6, 8, 7, 4],
            [2, 4, 8, 9, 5, 7, 1, 3, 6],
            [7, 6, 3, 4, 1, 8, 2, 5, 9]]

puzzle = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
          [6, 8, 0, 0, 7, 0, 0, 9, 0],
          [1, 9, 0, 0, 0, 4, 5, 0, 0],
          [8, 2, 0, 1, 0, 0, 0, 4, 0],
          [0, 0, 4, 6, 0, 2, 9, 0, 0],
          [0, 5, 0, 0, 0, 3, 0, 2, 8],
          [0, 0, 9, 3, 0, 0, 0, 7, 4],
          [0, 4, 0, 0, 5, 0, 0, 3, 6],
          [7, 0, 3, 0, 1, 8, 0, 0, 0]]

window = sg.Window('Sudoku',
                   [[sg.Frame('', [[sg.B('', size=(3, 1),
                                         font=('Courier', 40),
                                         enable_events=True,
                                         pad=(0, 0),
                                         key=(fr * 3 + r, fc * 3 + c))
                                    for c in range(3)] for r in range(3)]) for fc in range(3)] for fr in range(3)] + [[
                                                                                                                          sg.B(
                                                                                                                              d,
                                                                                                                              key=(
                                                                                                                              9,
                                                                                                                              d),
                                                                                                                              size=(
                                                                                                                              3,
                                                                                                                              1),
                                                                                                                              font=(
                                                                                                                              'Courier',
                                                                                                                              30),
                                                                                                                              pad=(
                                                                                                                              0,
                                                                                                                              10),
                                                                                                                              button_color=(
                                                                                                                              'white',
                                                                                                                              'black'))
                                                                                                                          for
                                                                                                                          d
                                                                                                                          in
                                                                                                                          range(
                                                                                                                              1,
                                                                                                                              10)]],
                   element_padding=(0, 0), element_justification='c', finalize=True)
window[(9, 1)].update(button_color=('black', 'white'))
numselected = 1
window[(0, 4)].update(4, disabled=True, disabled_button_color=('white', 'black'))


def newgame():
    for r, row in enumerate(puzzle):
        for c, col in enumerate(row):
            # print(r,c)
            # print(col)
            if puzzle[r][c] > 0:
                print(r, c)
                print('puzzle number')
                window[r, c].update(text=col, disabled=True, disabled_button_color=('green', 'pink'))
            else:
                print(r, c)
                pass


def solve_check():
    matches = 0
    for r, row in enumerate(puzzle):
        for c, col in enumerate(row):
            if solution[r][c] == col:
                matches = matches + 1

    if matches == 81:
        print('Solved!')
    else:
        print(matches)


def button_check(numselected):
    print(numselected)
    for i in range(1, 10):
        if sum(item.count(i) for item in puzzle) == 9:
            window[(9, i)].update(disabled=True, disabled_button_color=('blue', 'yellow'))
            numselected = i + 1
            window[(9, numselected)].update(button_color=('white', 'black'))
        else:
            window[(9, i)].update(disabled=False)
    if numselected > 9:
        numselected = 1

        # window.Refresh()
    print(numselected)
    return numselected


def button_selected(numselected):
    for i in range(1, 10):
        window[(9, i)].update(button_color=('white', 'black'))
    window[event].update(button_color=('black', 'white'))
    numselected = event[1]
    return numselected


newgame()

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    elif event >= (0, 0) and event <= (8, 8):
        window[event].update(numselected, button_color=('black', 'white'))
        r, c = event
        puzzle[r][c] = numselected
        print(puzzle)
        if solution[r][c] != numselected:
            window[event].update(button_color=('black', 'red'))
    
        numselected = button_check(numselected)
        print(numselected)
        solve_check()
    elif event >= (9, 1) and event <= (9, 9):
        numselected = button_selected(numselected)
        print(numselected)