if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    shape_points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    draw = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    win = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

    loss = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    tot_score = 0

    for l in lines:
        game = tuple(l.strip().split(' '))
        opponent = game[0]
        outcome = game[1]
        if outcome == 'X':
            p = shape_points[loss[opponent]]
            tot_score += p
        elif outcome == 'Y':
            p = shape_points[draw[opponent]]
            tot_score += (3 + p)
        else:
            p = shape_points[win[opponent]]
            tot_score += (6 + p)

    print(tot_score)
