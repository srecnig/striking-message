import calendar
import datetime
import json
import os
import uuid

from kombu import Connection, Producer

def get_payload(message):
  return json.dumps({
    "queue_name": "messages",
    "actor_name": "shout_something",
    "args": [message],
    "kwargs": {},
    "options": {},
    "message_id": str(uuid.uuid4()),
    "message_timestamp": calendar.timegm(datetime.datetime.utcnow().utctimetuple()),
  })


def get_broker_url():
    return os.environ.get('RABBITMQ_BROKER_URL')


if __name__ == '__main__':
    with Connection(get_broker_url()) as connection:
        with connection.channel() as channel:
            producer = Producer(channel=channel, routing_key='messages')
            producer.publish(get_payload('oida!'))
