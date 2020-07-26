FROM python:3.7-alpine
WORKDIR /home
COPY ./services/server/. .
RUN pip install -r Requirements.txt
EXPOSE 5000
CMD ["python" , "index.py"]


