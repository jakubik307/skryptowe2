import sys
import lab_3_helpers


def print_requests_sent_from_poland():
    for line in sys.stdin:
        if lab_3_helpers.check_country(line, "pl"):
            print(line)


if __name__ == "__main__":
    print_requests_sent_from_poland()
