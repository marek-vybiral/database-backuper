FROM python:3.9.1

RUN apt-get update && apt-get -y install wget lsb-release && apt-get clean all
RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update && apt-get -y install postgresql-13 && apt-get clean all

RUN apt-get update && apt-get -y install wget curl openssl && apt-get clean all

RUN pip install boto3 schedule

COPY /src /app

CMD python /app/scheduler.py