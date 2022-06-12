FROM python:3.9

WORKDIR /fastapi-app

COPY ./backend/req.txt .

RUN pip install -r req.txt

COPY ./backend ./backend

CMD [ "python3", "./backend/main.py" ]
