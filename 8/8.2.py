
def compute_view_range(tree, other_trees):
    range = 0
    for other in other_trees:
        range += 1
        if other >= tree:
            break
    return range


def parse_input(input):
    trees = input.split('\n')
    n_columns = len(trees[0])

    columns = ['' for _ in range(n_columns)]

    for row in trees:
        for c, tree in enumerate(row.strip()):
            columns[c] += tree

    return trees, columns


def main():
    file = open("input.txt")
    test_file = open("test_input.txt")
    input = file.read()

    rows, columns = parse_input(input)

    view_ranges = []
    for r, row in enumerate(rows):
        for c, tree in enumerate(row):
            up = columns[c][:r]
            down = columns[c][r+1:]
            right = rows[r][c+1:]
            left = rows[r][:c]

            view_ranges.append(
                compute_view_range(tree, right) *
                compute_view_range(tree, down) *
                compute_view_range(tree, reversed(up)) *
                compute_view_range(tree, reversed(left))
            )

    print(max(view_ranges))


if __name__ == "__main__":
    main()
