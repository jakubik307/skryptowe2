def check_status_in_line(line, code):
    try:
        return int(line.split(" ")[8].strip()) == code
    except ValueError:
        return False
    except IndexError:
        return False


def get_bytes_from_line(line):
    try:
        return int(line.split(" ")[9].strip())
    except ValueError:
        return 0
    except IndexError:
        return 0


def get_request_from_line(line):
    try:
        return line.split(" ")[5].replace('"', "").strip()
    except IndexError:
        return ""
