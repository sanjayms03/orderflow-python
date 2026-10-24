import requests

def fetch_tracking(url):
    # Caller-controlled URL demonstrates an SSRF finding; use only example URLs in fixtures.
    response = requests.get(url, timeout=None)
    return {"status": response.status_code, "text": response.text[:500]}
