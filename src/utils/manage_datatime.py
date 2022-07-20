import time
import argparse
from dateutil.parser import parse
from datetime import datetime, timedelta

#This whole module help us handle type formats.

DATE_FORMAT = "%Y-%m-%d"
DATE_FORMAT_WITH_HOUR = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT_WITH_MS = "%Y-%m-%d %H:%M:%S.%f"
DATE_ISO_8601_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def now():
    return datetime.now()


def get_date_with_hour():
    return now().strftime(DATE_FORMAT_WITH_HOUR)


def get_date():
    return now().strftime(DATE_FORMAT)


def get_utc_date():
    return datetime.utcnow().isoformat()


def parse_date(date, date_format=DATE_FORMAT):
    return date.strftime(date_format)


def parse_date_with_hour(date, date_format=DATE_FORMAT_WITH_HOUR):
    return date if type(date) == datetime or date is None else parse(date)


def format_date_with_ms(date, date_format=DATE_FORMAT_WITH_MS):
    return date.strftime(date_format)


def format_date(date, date_format=DATE_FORMAT_WITH_HOUR):
    return date.strftime(date_format)


def time_difference(first_time, second_time):
    if not (bool(first_time) and bool(second_time)):
        return float(0)
    return abs(timedelta.total_seconds(first_time - second_time))


def parse_time(date, date_format=DATE_FORMAT_WITH_HOUR):
    return date if date is None else time.strptime(date, date_format)


def format_time(date, date_format=DATE_FORMAT_WITH_HOUR):
    return time.strftime(date_format, date)


def to_iso_format(date, date_format=DATE_FORMAT_WITH_HOUR):
    if date:
        gmt_date = time.gmtime(time.mktime(parse_time(date, date_format)))
        return format_time(gmt_date, date_format=DATE_ISO_8601_FORMAT)
    return date


def minutes_to_seconds(minutes):
    return minutes * 60


def valid_date(s):
    try:
        return datetime.strptime(s, DATE_FORMAT_WITH_HOUR)
    except:
        try:
            return datetime.strptime(s, DATE_ISO_8601_FORMAT)
        except ValueError:
            msg = "Not a valid date: '{0}'.".format(s)
            raise argparse.ArgumentTypeError(msg)


def str_date_in_same_minute(str_date: str, reference: datetime):
    return time_difference(valid_date(str_date), reference) <= 60
