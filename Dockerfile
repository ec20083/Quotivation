FROM python:3.7-alpine 
WORKDIR /tasklistapp
COPY . /tasklistapp
RUN pip install -r requirements.txt
CMD ["python","app.py"]
EXPOSE 80
