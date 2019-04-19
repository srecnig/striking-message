FROM python:3.7.2-slim-stretch

ARG HOSTUID=1000
ARG HOSTGID=1000

# install dependencies
RUN apt-get update
RUN apt-get install -y git

# add host user
RUN addgroup --gid $HOSTGID python
RUN adduser --uid $HOSTUID --gid $HOSTGID  --gecos "" --disabled-password --quiet python
RUN echo "HOSTUSER=python" >> /etc/environment;

# create mount directory
RUN mkdir /source
RUN chown -R $HOSTUID:$HOSTGID /source
VOLUME /source

RUN mkdir /data
RUN chown -R $HOSTUID:$HOSTGID /data
VOLUME /data

RUN pip install virtualenv

RUN echo "source /data/virtualenv/bin/activate" >> /home/python/.bashrc
WORKDIR /source
ENTRYPOINT ["/source/_/development/python/entrypoint.sh"]
