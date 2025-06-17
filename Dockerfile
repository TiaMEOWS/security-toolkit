FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN chmod +x security-toolkit.py

CMD ["python3", "security-toolkit.py"]