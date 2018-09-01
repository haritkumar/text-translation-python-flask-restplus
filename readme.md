
# Text translation rest api using python
**Text translation API can dynamically translate text between language pairs (English - en, French - fr, Spanish - es, Welsh - cy, Portuguese - pt).**

Internally it uses google transation
![alt text](https://res.cloudinary.com/haritkumar/image/upload/v1535819977/github/gs.png)

## Setup Instruction
```sh
git clone https://gitlab.com/python-pro/text-translation.git
cd text-translation/
sudo pip3 install -r requirement.txt
python3 app.py
```
- Access here http://localhost:5000/api/
![alt text](https://res.cloudinary.com/haritkumar/image/upload/v1535819977/github/gs2.png)
![alt text](https://res.cloudinary.com/haritkumar/image/upload/v1535819977/github/gs3.png)

## Dockerfile
```sh
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
```