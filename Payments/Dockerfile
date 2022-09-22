FROM python:3.10.4-slim as builder
LABEL author='Edward' version=1.0 description="Stripe"
WORKDIR /app
COPY requirements.txt .
COPY . .
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN ["chmod", "+x", "./docker-entrypoint.sh"]
CMD ["./docker-entrypoint.sh"]