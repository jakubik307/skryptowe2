import sys
import lab_3_helpers


def print_filter_sent_on_friday():
    for line in sys.stdin:
        if lab_3_helpers.check_week_day(line, 4):
            print(line)


print_filter_sent_on_friday()