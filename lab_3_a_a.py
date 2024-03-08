import lab_3_helpers


def print_status_200_quantity():
    print(f"Status 200 request count: {lab_3_helpers.count_codes(200)}")


print_status_200_quantity()
