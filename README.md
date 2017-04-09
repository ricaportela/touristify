Touristify REST API with Django
=========================

Getting Started
---------------

### Initial Setup ###
1. Make a new virtualenv: ``virtualenv .venv``
2. Activate the virtualenv: ``source env/bin/activate``
3. Install Django: ``pip install -r requirements.txt``
4. Edit ``drf_tour_points/settings.py:108`` to match your LANGUAGE_CODE
5. Run the server: ``python manage.py runserver``
6. Admin Site at ``http://127.0.0.1:8000/admin`` (admin:admin)


### Test API ###

6. Open website in browser at ``http://127.0.0.1:8000/tourlist``, return list of tourist points
7. Open website in browser at ``http://127.0.0.1:8000/tourdetails/1/``, return details of tourist points


### Unit Tests ###
1. must be completed

### Docker ###
1. Must be Completed

   Build docker container
   docker build -t myapplication .

   Running container
   docker run -p 8000:8000 -d myapplication

   ############################################################
   # Dockerfile for a Scrapy development environment
   # Based on Ubuntu Image
   ############################################################

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


### Deploy ###
1. Must be Completed