import os

import dramatiq
import pika

from dramatiq.brokers.rabbitmq import RabbitmqBroker

# wrangle parameters
credentials = pika.PlainCredentials(
    os.environ.get('RABBITMQ_USER'),
    os.environ.get('RABBITMQ_PASSWORD')
)
default_params = dict(
    virtual_host=os.environ.get('RABBITMQ_VHOST'),
    port=os.environ.get('RABBITMQ_PORT'),
    credentials=credentials,
)
parameters = [
    dict(host=host, **default_params)
    for host in os.environ.get('RABBITMQ_HOSTS').split(',')
]

# initialize broker
rabbitmq_broker = RabbitmqBroker(parameters=parameters)
dramatiq.set_broker(rabbitmq_broker)

# import the tasks
from .shout import shout_something
