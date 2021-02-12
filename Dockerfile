FROM python:3.7.4-stretch

WORKDIR /app

# copy all files
COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run 
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app