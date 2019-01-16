# striking-message
a basic docker(compose) setup to play around with [dramatiq](https://dramatiq.io).

# running this

to try this out, do the following:

* you need [docker](https://docs.docker.com/get-started/) and [docker-compose](https://docs.docker.com/compose/) 
* call `docker-compose up` in `_/development` to start up rabbitmq and the dramatiq consumer
* to enqueue a job, start a shell in the consumer container using `_/development/consumer_run.sh`. once in there, run `ipython`
* import the job and run it with `shout_something.send('supercool')`
* the consumer should have picked up the job and printed out `SUPERCOOL`

