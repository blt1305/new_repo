from datetime import datetime, timedelta


def print_datetime():
    print(str(datetime.now() + timedelta(hours=3)))
