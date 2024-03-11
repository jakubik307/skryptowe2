import sys

import lab_3_helpers


def print_total_sent_bytes():
    total_bytes = 0

    for line in sys.stdin:
        if lab_3_helpers.get_request_from_line(line) == "GET":
            total_bytes += lab_3_helpers.get_bytes_from_line(line)

    gigabytes = total_bytes / 1024 ** 3

    print(f"Total data sent: {gigabytes} GB")


if __name__ == "__main__":
    print_total_sent_bytes()
