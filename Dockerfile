FROM alpine:3.7

RUN apk add python3
RUN apk add git
RUN git clone https://github.com/vinicius0197/slack-kpi.git

WORKDIR /slack-kpi

RUN pip3 install -r requirements.txt

ENV FLASK_APP=app/api/app.py
# ENTRYPOINT ["python3"]
# CMD ["flask run --host=0.0.0.0"]

EXPOSE 5000
RUN chmod +x boot.sh
ENTRYPOINT [".boot.sh"]