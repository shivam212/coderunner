FROM python:3.9.1
ADD . /coderunner
WORKDIR /coderunner
RUN pip install -r requirements.txt