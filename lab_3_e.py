import sys

import lab_3_helpers


def print_filter_status_200():
    for line in sys.stdin:
        if lab_3_helpers.check_status_in_line(line, 200):
            print(line)


print_filter_status_200()
