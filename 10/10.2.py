from pprint import pprint


def draw_pixel(screen, row, column):
    screen[row] = screen[row][:column] + '#' + screen[row][column+1:]
    return screen


def update_screen(screen, cycle, X, row):
    drawing_pixel = cycle % 40
    if drawing_pixel < 0:
        print(drawing_pixel)
    if drawing_pixel in range(X - 1, X + 2):
        screen = draw_pixel(screen, row, drawing_pixel)

    return screen


def main():
    file = open("input.txt")
    test_file = open("test_input.txt")
    lines = file.readlines()

    X = 1
    cycle = 0
    end_of_lines = [40, 80, 120, 160, 200, 240]

    screen = []
    for r in range(6):
        screen.append('')
        for c in range(40):
            screen[r] += '.'

    row = 0
    for command in lines:
        if command.strip() == 'noop':
            screen = update_screen(screen, cycle, X, row)
            cycle += 1
            if cycle in end_of_lines:
                row += 1

        else:
            screen = update_screen(screen, cycle, X, row)
            cycle += 1
            if cycle in end_of_lines:
                row += 1

            screen = update_screen(screen, cycle, X, row)
            cycle += 1
            if cycle in end_of_lines:
                row += 1
            X += int(command.strip().split(' ')[1])
    pprint(screen)


if __name__ == "__main__":
    main()

