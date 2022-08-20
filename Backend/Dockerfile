FROM python:3.10-slim
COPY requirements.txt /home/ksharma20/code/
WORKDIR /home/ksharma20/code/
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
