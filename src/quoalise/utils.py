import datetime as dt


def parse_iso_date(date: str) -> dt.date:
    return dt.datetime.strptime(date, "%Y-%m-%d").date()


def format_iso_date(date: dt.date) -> str:
    return date.strftime("%Y-%m-%d")
