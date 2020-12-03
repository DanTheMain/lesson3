# Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
# Превратите строку "01/01/25 12:10:03.234567" в объект datetime

from datetime import date, time, datetime, timedelta


def print_some_dates():
    today = datetime.now()
    print(f"Yesterday's date: {(today - timedelta(days=1)).strftime('%Y-%m-%d')}")
    print(f"Today's date: {today.strftime('%Y-%m-%d')}")
    print(f"Date 30 days ago: {(today - timedelta(days=30)).strftime('%Y-%m-%d')}")

def convert_str_to_datetime(datetime_str: str, dt_format: str = '%d/%m/%y %H:%M:%S.%f'):
    try:
        date_dt = datetime.strptime(datetime_str, dt_format)
        print(date_dt.strftime('%d.%m.%Y-%H:%M:%S'))
    except ValueError as e:
        print(f'Could not convert {datetime_str} with format {dt_format} due to error - type: {type(e)}, details: {e}!')


if __name__ == "__main__":
    print_some_dates()
    convert_str_to_datetime("01/01/25 12:10:03.234567")
