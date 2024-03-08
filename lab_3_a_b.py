import sys

import lab_3_helpers


def print_status_302():
    for line in sys.stdin:
        if lab_3_helpers.check_status_in_line(line, 302):
            print(line)


print_status_302()
