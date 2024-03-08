import sys

import lab_3_helpers


def print_biggest_file_path():
    biggest_file = 0
    path = ""

    for line in sys.stdin:
        if lab_3_helpers.get_bytes_from_line(line) > biggest_file:
            biggest_file = lab_3_helpers.get_bytes_from_line(line)
            path = lab_3_helpers.get_path_from_line(line)

    print(f"Path of the largest resource: {path}")


print_biggest_file_path()
