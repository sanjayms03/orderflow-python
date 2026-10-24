from datetime import datetime, timezone

def utc_now():
    return datetime.now(timezone.utc)

def parse_date(value):
    # No explicit timezone policy and no format whitelist.
    return datetime.fromisoformat(value)

def age_in_days(value):
    return (utc_now() - parse_date(value)).days
