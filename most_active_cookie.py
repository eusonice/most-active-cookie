import sys
import csv
from datetime import datetime

def check_argument_length(args):
    if len(args) != 4:
        print('Must be in this format: {} [csv_file] -d yyyy-mm-dd'.format(args[0]))
        exit(1)

def check_date_input(args):
    try:
        target = datetime.strptime(args, '%Y-%m-%d').strftime('%Y-%m-%d')
        return target
    except:
        print('Wrong argument given for the date')
        exit(1)

def get_active_cookie(args):
    check_argument_length(args)
    csv_file, target = args[1], check_date_input(args[3])

    cookies = {}

    with open(csv_file, newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = datetime.strptime(row['timestamp'], '%Y-%m-%dT%H:%M:%S%z').strftime('%Y-%m-%d')
            if date == target:
                if row['cookie'] in cookies:
                    cookies[row['cookie']] += 1
                else:
                    cookies[row['cookie']] = 1

    most_active_cookies = [key for key, value in cookies.items() if value == max(cookies.values())]

    if not most_active_cookies:
        print('There is no active cookie for the day {}'.format(target))
        return

    for cookie in most_active_cookies:
        print(cookie)

    return most_active_cookies

if __name__ == '__main__':
    get_active_cookie(sys.argv)