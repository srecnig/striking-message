# striking-message
a basic docker(compose) setup to play around with [dramatiq](https://dramatiq.io). we'll enqueue dramatic jobs with the celery stack (kombu).

# running this

to try this out, do the following:

* you need [docker](https://docs.docker.com/get-started/) and [docker-compose](https://docs.docker.com/compose/)
* call `docker-compose up` in `_/development` to start up rabbitmq and the dramatiq consumer
* to enqueue a job, start a shell in the sender container using `_/development/sender_run.sh`. once in there, run `ipython`. import `send_message` and run it with a message to have the consumer print it out.

