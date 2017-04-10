# Touristify REST API with Django
Getting Started
---------------

# Initial Setup
* Make a new virtualenv: ``virtualenv .venv``
* Activate the virtualenv: ``source env/bin/activate``
* Install Django: ``pip install -r requirements.txt``
* Edit ``drf_tour_points/settings.py:108`` to match your LANGUAGE_CODE
* Run the server: ``python manage.py runserver``
* Admin Site at ``http://127.0.0.1:8000/admin`` (admin:admin)

# Test API 
* Open website in browser at ``http://127.0.0.1:8000/tourlist``, return list of tourist points
* Open website in browser at ``http://127.0.0.1:8000/tourdetails/1/``, return details of tourist points


# Unit Tests 
* should be completed

# Docker
* shoud be completed
```sh

   Build docker container
   docker build -t myapplication .

   Running container
   docker run -p 8000:8000 -d myapplication

  # Dockerfile for Django Rest API development environment
  # Based on Ubuntu Image

  FROM ubuntu
   MAINTAINER NeuralFoundry <neuralfoundry.com>

   RUN echo deb http://archive.ubuntu.com/ubuntu precise universe >> /etc/apt/sources.list
   RUN apt-get update

   ## Python Family
   RUN apt-get install -qy python python-dev python-distribute python-pip ipython


   # Replace 1000 with your user / group id
   RUN export uid=1000 gid=1000 && \
       mkdir -p /home/developer && \
       echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
       echo "developer:x:${uid}:" >> /etc/group && \
       echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
       chmod 0440 /etc/sudoers.d/developer && \
       chown ${uid}:${gid} -R /home/developer

   USER developer
   ENV HOME /home/developer
```

### Deploy ###
1. should be Completed
