FROM python:3.7.2-slim

ARG HOSTUID=1000
ARG HOSTGID=1000

# add host user
RUN addgroup --gid $HOSTGID consumer
RUN adduser --uid $HOSTUID --gid $HOSTGID  --gecos "" --disabled-password --quiet consumer
RUN echo "HOSTUSER=consumer" >> /etc/environment;

# create mount directory
RUN mkdir /source
RUN chown -R $HOSTUID:$HOSTGID /source
VOLUME /source

RUN mkdir /data
RUN chown -R $HOSTUID:$HOSTGID /data
VOLUME /data

RUN pip install virtualenv

RUN echo "source /data/virtualenv/bin/activate" >> /home/consumer/.bashrc
WORKDIR /source/consumer/
ENTRYPOINT ["/source/_/development/consumer/entrypoint.sh"]
