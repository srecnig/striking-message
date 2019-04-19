#!/bin/bash

# setup rabbitmq
(
    until [ "$(rabbitmqctl wait $RABBITMQ_PID_FILE --timeout 20 > /dev/null; echo $?)" == "0" ]; do sleep 0.1; done;
    echo 'Setting up rabbitmq...'

    rabbitmqctl add_vhost messages &
    rabbitmqctl add_user striking password &

    wait

    rabbitmqctl set_permissions -p messages striking ".*" ".*" ".*" &
) &

# start rabbitmq server
rabbitmq-server
