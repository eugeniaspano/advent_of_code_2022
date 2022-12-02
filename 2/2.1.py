if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    draws = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    wins = {
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
            p = points[loss[opponent]]
            tot_score += p
        elif outcome == 'Y':
            p = points[draws[opponent]]
            tot_score += (3 + p)
        else:
            p = points[wins[opponent]]
            tot_score += (6 + p)

    print(tot_score)
