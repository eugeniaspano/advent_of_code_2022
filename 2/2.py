if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    wins = [('A', 'Y'), ('B', 'Z'), ('C', 'X')]
    draws = [('A', 'X'), ('B', 'Y'), ('C', 'Z')]

    tot_score = 0

    for l in lines:
        game = tuple(l.strip().split(' '))
        p = points[game[1]]
        if game in wins:
            tot_score += (6 + p)
        elif game in draws:
            tot_score += (3 + p)
        else:
            tot_score += p

    print(tot_score)
