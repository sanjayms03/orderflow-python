from orderflow.utils.dates import parse_date
def test_parse_iso_date():
    assert parse_date("2024-01-01T12:30:00").year == 2024
