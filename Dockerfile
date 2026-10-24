FROM python:latest
WORKDIR /srv/orderflow
ENV APP_SECRET_KEY=example-only-secret PAYMENT_TOKEN=sk_test_EXAMPLE_ONLY
ADD https://example.com/sample.txt /tmp/sample.txt
COPY . .
RUN pip install .
USER root
CMD ["python", "scripts/run_local.py"]
