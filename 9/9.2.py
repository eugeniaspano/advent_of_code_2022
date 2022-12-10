from pprint import pprint


def compute_head_positions(start_head_pos, direction, steps):
    if direction == 'R':
        new_head_positions = [(start_head_pos[0], start_head_pos[1] + step) for step in range(1, steps + 1)]
    elif direction == 'L':
        new_head_positions = [(start_head_pos[0], start_head_pos[1] - step) for step in range(1, steps + 1)]
    elif direction == 'U':
        new_head_positions = [(start_head_pos[0] - step, start_head_pos[1]) for step in range(1, steps + 1)]
    elif direction == 'D':
        new_head_positions = [(start_head_pos[0] + step, start_head_pos[1]) for step in range(1, steps + 1)]

    return new_head_positions


def too_distant(tail_pos, head_pos):
    head_x = head_pos[0]
    head_y = head_pos[1]
    tail_x = tail_pos[0]
    tail_y = tail_pos[1]

    if abs(tail_x - head_x) > 1 or abs(tail_y - head_y) > 1:
        return True
    return False


def tail_moves(tail_pos, head_pos):
    head_x = head_pos[0]
    head_y = head_pos[1]
    tail_x = tail_pos[0]
    tail_y = tail_pos[1]

    if head_x == tail_x:
        if head_y > tail_y:
            # right
            new_tail_pos = (head_x, tail_y + 1)
        else:
            # left
            new_tail_pos = (head_x, tail_y - 1)
    elif head_y == tail_y:
        if head_x > tail_x:
            # down
            new_tail_pos = (tail_x + 1, head_y)
        else:
            # up
            new_tail_pos = (tail_x - 1, head_y)
    elif head_y > tail_y:
        if head_x < tail_x:
            # up right
            new_tail_pos = (tail_x - 1, tail_y + 1)
        else:
            # down right
            new_tail_pos = (tail_x + 1, tail_y + 1)
    elif head_y < tail_y:
        if head_x < tail_x:
            # up left
            new_tail_pos = (tail_x - 1, tail_y - 1)
        else:
            # down left
            new_tail_pos = (tail_x + 1, tail_y - 1)
    else:
        print(f"ERROR: tail: {tail_pos}, head: {head_pos}")
        exit(1)

    return new_tail_pos


def compute_tail_move(head_pos, tail_pos):
    if too_distant(tail_pos, head_pos):
        new_tail_pos = tail_moves(tail_pos, head_pos)
    else:
        new_tail_pos = tail_pos

    return new_tail_pos


def main():
    file = open("input.txt")
    test_file = open("test_input.txt")
    head_moves = file.readlines()

    head_position = (0, 0)
    tails = []
    for i in range(9):
        tails.append([(0, 0)])

    for move in head_moves:
        direction = move.strip().split(' ')[0]
        steps = int(move.strip().split(' ')[1])

        new_head_positions = compute_head_positions(head_position, direction, steps)
        head_position = new_head_positions[-1]

        for head in new_head_positions:
            for i in range(len(tails)):
                tails[i].append(compute_tail_move(head, tails[i][-1]))
                head = tails[i][-1]

    final_tail_positions = tails[8]
    print(len(set(final_tail_positions)))


if __name__ == "__main__":
    main()
