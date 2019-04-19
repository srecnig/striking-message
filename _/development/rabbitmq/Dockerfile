FROM rabbitmq:3.7.9-alpine

ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbit.pid

COPY rabbitmq.conf /etc/rabbitmq/rabbitmq.conf
COPY .erlang.cookie /var/lib/rabbitmq/.erlang.cookie
COPY start.sh /start.sh

CMD /start.sh
