FROM python:3.6
ADD . /cb_classifier
WORKDIR /cb_classifier
RUN pip install -r requirements.txt
EXPOSE  5000
CMD ["python", "cb_main.py", "-p 5000"]

