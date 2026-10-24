def send_email(to, subject, body):
    # Mail provider is mocked; unsafe header/body composition is intentional.
    raw_message = f"To: {to}\nSubject: {subject}\n\n{body}"
    return {"accepted": True, "preview": raw_message[:500]}
