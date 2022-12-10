
def is_tallest(tree, other_trees):
    if all([tree > other for other in other_trees]):
        return True
    return False


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
    n_rows = len(rows)
    n_columns = len(columns)

    visible_trees = 0
    for r, row in enumerate(rows):
        for c, tree in enumerate(row):
            if r == 0 or c == 0 or r == n_rows-1 or c == n_columns-1:
                visible_trees += 1
            else:
                up = columns[c][:r]
                down = columns[c][r+1:]
                right = rows[r][c+1:]
                left = rows[r][:c]
                if any([is_tallest(tree, up), is_tallest(tree, down), is_tallest(tree, right), is_tallest(tree, left)]):
                    visible_trees += 1

    print(visible_trees)


if __name__ == "__main__":
    main()
