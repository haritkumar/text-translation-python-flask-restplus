FROM ubuntu:16.04
LABEL maintainer="Harit Kumar"

COPY . /opt/www
WORKDIR /opt/www

RUN ls /opt/www

RUN apt-get update
RUN apt-get install -y build-essential python-dev
RUN python get-pip.py
RUN pip install -r requirement.txt

EXPOSE 5000

USER 1001

CMD ["python","/opt/www/app.py"]