def check_status_in_line(line, code):
    try:
        return int(line.split(" ")[8].strip()) == code
    except ValueError:
        return False
    except IndexError:
        return False
