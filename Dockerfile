FROM python:3.7-alpine

COPY . echo-bot
WORKDIR echo-bot

RUN python3 -m pip install -r requirements.txt

CMD python3 TeleTomaton.py
