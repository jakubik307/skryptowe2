import sys

import lab_3_helpers


def print_image_download_ratio():
    image_data = 0
    total_data = 0

    for line in sys.stdin:
        if lab_3_helpers.get_request_from_line(line) == "GET":
            bytes_in_line = lab_3_helpers.get_bytes_from_line(line)
            total_data += bytes_in_line
            if is_image(lab_3_helpers.get_path_from_line(line)):
                image_data += bytes_in_line

    try:
        ratio = image_data / total_data
    except ZeroDivisionError:
        ratio = 0

    print(f"Image download ratio: {ratio}")


def is_image(path):
    image_extensions = ('.gif', '.jpg', '.jpeg', '.xbm')

    for extension in image_extensions:
        if extension in path:
            return True
    return False


if __name__ == "__main__":
    print_image_download_ratio()
