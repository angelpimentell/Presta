FROM python:3.9.14-buster

WORKDIR /usr/local/src/presta

# Upgrade packages
RUN apt-get update
RUN apt-get upgrade -y

# Install dependencies
RUN /usr/local/bin/pip install --upgrade pip
COPY requirements.txt /usr/local/src/presta/requirements.txt
RUN pip install -r /usr/local/src/presta/requirements.txt

# Copy project
COPY . .

EXPOSE 8080