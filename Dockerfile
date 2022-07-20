FROM python:3.10
COPY . ./
COPY ./requirements.txt /src/requirements.txt
ENV APP_HOME /src
WORKDIR $APP_HOME
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn main:src --host 0.0.0.0 --port 8080