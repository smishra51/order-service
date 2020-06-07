FROM python:3.8
COPY [".env" ,"config.py", "requirements.txt", "wsgi.py", "./"]
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["wsgi.py"]
