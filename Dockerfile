FROM python:3.9-slim

WORKDIR /app

# Copy app and requirements
COPY app.py .
COPY requirements.txt .

# Upgrade pip and setuptools to secure versions
RUN pip install --upgrade pip setuptools

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]
