FROM python:3.11

WORKDIR /author
RUN pip install gunicorn
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["make", "run"]