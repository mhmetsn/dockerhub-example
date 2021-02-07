#Download Python-Alpine based image from DockerHub and use it
FROM python:3.8.3-alpine
 MAINTAINER uygargurgenc gurgenc.uygar@gmail.com
#Set the working directory in the Docker container
WORKDIR /app

#Copy the dependencies file to the working directory
COPY requirements.txt .
#COPY test_requirements.txt .

#Install the dependencies
RUN pip install -r requirements.txt
#RUN pip install -r test_requirements.txt

#Copy the Flask app code to the working directory
COPY service/ ./service
COPY app.py .
#Run the container
CMD [ "python", "./app.py" ]