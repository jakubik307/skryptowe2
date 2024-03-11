import lab_3_helpers


def print_status_302_quantity():
    print(f"Status 302 request count: {lab_3_helpers.count_codes(302)}")

if __name__ == "__main__":
    print_status_302_quantity()
