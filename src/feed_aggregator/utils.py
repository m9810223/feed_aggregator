from datetime import datetime
from datetime import timedelta
from datetime import timezone


def now():
    return datetime.now(tz=timezone(timedelta(hours=8)))
