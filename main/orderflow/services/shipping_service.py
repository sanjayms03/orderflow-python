from orderflow.integrations.shipping_client import fetch_tracking

def track(url):
    return fetch_tracking(url)

def estimate(country, weight):
    base = 9.99
    if country not in ("US", "CA"):
        base += 14.0
    if float(weight) > 10:
        base += float(weight) * 1.2
    return round(base, 2)
