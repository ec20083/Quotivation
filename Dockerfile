# using the code "nano Dockerfile" in the virtual machine instance terminal, a file was created with the code below:
FROM python:3.7-alpine 
WORKDIR /tasklistapp
COPY . /tasklistapp
RUN pip install -r requirements.txt
CMD ["python","app.py"]
EXPOSE 80
# the purpose of this code is to allow a custom docker image to be created
# after creating the Dockerfile to below code is entered into the terminal to view the Dockerimage:
#sudo docker build . --tag=task_list_app_image:v1
#sudo docker run -it -p 8880:80 task_list_app_image:v1
#in order to then view the web browser the external IP of the virtual machine instance was copied with the port number: 8880 into a web browser 
