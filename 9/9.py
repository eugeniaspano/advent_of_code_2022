def compute_positions(start_head_pos, start_tail_pos, direction, steps):
    if direction == 'R':
        new_head_positions = [(start_head_pos[0], start_head_pos[1]+step) for step in range(1, steps+1)]
    elif direction == 'L':
        new_head_positions = [(start_head_pos[0], start_head_pos[1]-step) for step in range(1, steps+1)]
    elif direction == 'U':
        new_head_positions = [(start_head_pos[0]+step, start_head_pos[1]) for step in range(1, steps+1)]
    elif direction == 'D':
        new_head_positions = [(start_head_pos[0]-step, start_head_pos[1]) for step in range(1, steps+1)]
    
    new_tail_positions = []
    for head_pos in new_head_positions:
        if too_distant(start_tail_pos, head_pos):
            tail_pos = tail_moves(start_tail_pos, head_pos, direction)
            new_tail_positions.append(tail_pos)
            start_tail_pos = tail_pos

    return new_head_positions, new_tail_positions


def too_distant(tail_pos, head_pos):
    head_x = head_pos[0]
    head_y = head_pos[1]
    tail_x = tail_pos[0]
    tail_y = tail_pos[1]

    if abs(tail_x - head_x) > 1 or abs(tail_y - head_y) > 1:
        return True
    return False


def tail_moves(tail_pos, head_pos, direction):
    head_x = head_pos[0]
    head_y = head_pos[1]
    tail_x = tail_pos[0]
    tail_y = tail_pos[1]
    
    if direction == 'R':
        new_tail_pos = (head_x, tail_y + 1)
    elif direction == 'L':
        new_tail_pos = (head_x, tail_y - 1)
    elif direction == 'U':
        new_tail_pos = (tail_x + 1, head_y)
    elif direction == 'D':
        new_tail_pos = (tail_x - 1, head_y)
    
    return new_tail_pos


def main():
    file = open("input.txt")
    test_file = open("test_input.txt")
    head_moves = file.readlines()

    tail_positions = [(0, 0)]

    head_position = (0, 0)
    tail_position = (0, 0)
    for move in head_moves:
        direction = move.strip().split(' ')[0]
        steps = int(move.strip().split(' ')[1])

        new_head_positions, new_tail_positions = compute_positions(head_position, tail_position, direction, steps)
        tail_positions.extend(new_tail_positions)
        head_position = new_head_positions[-1]
        tail_position = tail_positions[-1]

    print(len(set(tail_positions)))


if __name__ == "__main__":
    main()
