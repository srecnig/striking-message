FROM rabbitmq:3.7.14-management

COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf
COPY rabbitmq_definitions.json /etc/rabbitmq/rabbitmq_definitions.json
COPY .erlang.cookie /var/lib/rabbitmq/.erlang.cookie
