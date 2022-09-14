FROM python:3.9.14-buster

WORKDIR /usr/local/src/presta

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy project
COPY . .

EXPOSE 8080