if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()

    elves_totals = []
    n_elves = 0

    elves_totals.append(0)
    for calories in lines:
        if calories != '\n':
            elves_totals[n_elves] += int(calories)
        else:
            n_elves += 1
            elves_totals.append(0)

    print(max(elves_totals))



