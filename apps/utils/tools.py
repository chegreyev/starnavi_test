import datetime

from dateutil.relativedelta import relativedelta

from utils.const import MONTHS_NAME_TRANSLATE


def get_period_name(start_date, period_type, step=0):
    if period_type == 'day':
        date_time = start_date + relativedelta(days=step)
        period_name = f'{date_time.strftime("%d")}.{date_time.strftime("%m")}.{date_time.year}'
    elif period_type == 'month':
        date_time = start_date + relativedelta(months=step)
        month = date_time.strftime("%B")
        month_translate = MONTHS_NAME_TRANSLATE.get(month)
        period_name = f'{month_translate} {date_time.year}'
    elif period_type == 'year':
        period_name = (datetime.datetime(start_date.year, 1, 1) + relativedelta(years=step)).year
    else:
        period_name = None

    return period_name
