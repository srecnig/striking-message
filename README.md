# striking-message
a basic docker(compose) setup to play around with [dramatiq](https://dramatiq.io). it includes a high availablity rabbitmq cluster with two nodes, and two python containers for consuming and sending dramatiq jobs. dramatiq jobs will be enqueued using the celery stack ([kombu](https://github.com/celery/kombu)).

# running this

to try this out, do the following:

* you need [docker](https://docs.docker.com/get-started/) and [docker-compose](https://docs.docker.com/compose/)
* call `docker-compose up` in `_/development` to start up the rabbitmq nodes and the dramatiq consumer, and to prepare the sender.
* to enqueue a job, start a shell in the sender container using `_/development/sender_run.sh`. once in there, run `ipython`. `from striking_message import send_message` and run it with some message to have the consumer print it out.
* the rabbitmq cluster and dramatiq are configured for high availability. stopping the rabbitmq app (`rabbitmqctl stop_app`) in the currently connected rabbitmq node results in a reconnect of the dramatiq consumer to the other node, making everything still work.

