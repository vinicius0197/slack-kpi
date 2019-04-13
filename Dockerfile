FROM alpine:3.7

RUN apk add python3
RUN apk add git
RUN git clone https://github.com/vinicius0197/slack-kpi.git

WORKDIR slack-kpi

RUN ls

WORKDIR /slack-kpi

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app/api/app.py
RUN flask run --host=0.0.0.0