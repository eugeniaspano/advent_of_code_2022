from collections import defaultdict


def default_zero():
    return 0


def default_empty_list():
    return []


def setup_structure(blocks):
    sizes = defaultdict(default_zero)
    contains = defaultdict(default_empty_list)

    parent_folder = ''
    for i, block in enumerate(blocks):
        if block[0] == '..':
            parent_folder = '/'.join(parent_folder.split('/')[:-2]) + '/'
            continue

        if i == 0:
            folder = block[0]
            parent_folder = folder
        else:
            folder = parent_folder + block[0] + '/'
            parent_folder = folder

        sub_folders = [folder + line.split(' ')[1] + '/' for line in block if line.startswith('dir')]
        contains[folder].extend(sub_folders)

        base_size = sum([int(line.split(' ')[0]) for line in block if line[0].isdigit()])
        sizes[folder] += base_size

    return sizes, contains


def main():
    file = open("input.txt")
    test_file = open("test_input.txt")
    input = file.read().split('$ cd')
    blocks = [command.strip().split('\n') for command in input if command != '']

    sizes, contains = setup_structure(blocks)

    for folder in reversed(sizes):
        sizes[folder] += sum(sizes[subfolder] for subfolder in contains[folder])

    max_size = 70000000
    target_unused = 30000000

    currently_unused = max_size - sizes['/']

    for size in sorted(sizes.values()):
        if currently_unused + size > target_unused:
            print(size)
            break


if __name__ == "__main__":
    main()
