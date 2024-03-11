import lab_3_helpers


def print_status_404_quantity():
    print(f"Status 404 request count: {lab_3_helpers.count_codes(404)}")


if __name__ == "__main__":
    print_status_404_quantity()
