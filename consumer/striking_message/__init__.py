import dramatiq

from dramatiq.brokers.rabbitmq import RabbitmqBroker

rabbitmq_broker = RabbitmqBroker(url='amqp://striking:password@rabbitmq:5672/messages')
dramatiq.set_broker(rabbitmq_broker)

# import the tasks
from .shout import shout_something
