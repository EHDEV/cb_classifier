FROM python:3.6

RUN pip install -r requirements.txt

ADD . /cb_classifier

WORKDIR /cb_classifier

EXPOSE  5000

CMD ["python", "cb_main.py", "-p 5000"]

