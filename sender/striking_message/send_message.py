import calendar
import datetime
import json
import os
import uuid

from kombu import Connection, Producer

def send_message(message):
    with Connection(_broker_url()) as connection:
        with connection.channel() as channel:
            producer = Producer(channel=channel, routing_key='messages')
            producer.publish(_dramatiq_shout_payload(message))


def _dramatiq_shout_payload(message):
  return json.dumps({
    "queue_name": "messages",
    "actor_name": "shout_something",
    "args": [message],
    "kwargs": {},
    "options": {},
    "message_id": str(uuid.uuid4()),
    "message_timestamp": calendar.timegm(datetime.datetime.utcnow().utctimetuple()),
  })


def _broker_url():
    environment = os.environ
    user = environment.get('RABBITMQ_USER')
    password = environment.get('RABBITMQ_PASSWORD')
    port = environment.get('RABBITMQ_PORT')
    vhost = environment.get('RABBITMQ_VHOST')
    hosts = environment.get('RABBITMQ_HOSTS').split(',')
    return ';'.join([f'amqp://{user}:{password}@{host}:{port}/{vhost}' for host in hosts])
