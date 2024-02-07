FROM python:3.11.6-alpine

WORKDIR /bot
COPY main.py .
COPY requirements.sh .
COPY modules ./modules

RUN ["sh", "requirements.sh"]
ENTRYPOINT ["python", "main.py"] 
