import os

import dramatiq

from dramatiq.brokers.rabbitmq import RabbitmqBroker

# initialize broker
rabbitmq_broker = RabbitmqBroker(url=os.environ.get('RABBITMQ_BROKER_URL'))
dramatiq.set_broker(rabbitmq_broker)

# import the tasks
from .shout import shout_something
