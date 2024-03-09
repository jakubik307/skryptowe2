import sys
import datetime


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


def get_path_from_line(line):
    try:
        return line.split(" ")[6].strip()
    except IndexError:
        return ""


def count_codes(code):
    acc = 0
    for line in sys.stdin:
        if check_status_in_line(line, code):
            acc += 1
    return acc


def check_week_day(line, day):
    try:
        return get_week_day(line.split(" ")[3].strip()) == day
    except ValueError:
        return False
    except IndexError:
        return False


def get_week_day(line):
    date = datetime.datetime.strptime(line[1:], "%d/%b/%Y:%H:%M:%S")
    return int(date.weekday())


def check_hours_range(line, start_hour, end_hour):
    try:
        return check_given_hour(line.split(" ")[3].strip(), start_hour, end_hour)
    except ValueError:
        return False
    except IndexError:
        return False


def check_given_hour(line, start_hour, end_hour):
    hour = line.split(":")
    h = int(hour[1].strip())
    m = int(hour[2].strip())
    s = int(hour[3].strip())
    if start_hour < end_hour:
        if start_hour < h < end_hour:
            return True
        if start_hour == h:
            if m > 0 or s > 0:
                return True
        return False
    else:
        if h < end_hour:
            return True
        if start_hour < h:
            return True
        if start_hour == h:
            if m > 0 or s > 0:
                return True
        return False

