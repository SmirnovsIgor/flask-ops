FROM python:3.7
ARG secret_salt
ARG test_salt
ENV SALT=$secret_salt
ENV TEST_SALT=$test_salt
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN mkdir /flask-app
WORKDIR /flask-app
COPY requirements.txt /flask-app/
EXPOSE 5000
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /flask-app/
CMD ["bash", "start.sh"]
