import sys
import lab_3_helpers


def print_filter_sent_between_22_and_6():
    for line in sys.stdin:
        if lab_3_helpers.check_hours_range(line, 22, 6):
            print(line)


if __name__ == '__main__':
    print_filter_sent_between_22_and_6()
