#!/bin/bash

(
    until [ "$(timeout -t 5 rabbitmqctl list_users &> /dev/null; echo $?)" == "0" ]; do sleep 0.1; done;
    echo 'Setting up rabbitmq...'

    rabbitmqctl add_vhost messages &
    rabbitmqctl add_user striking password &

    wait

    rabbitmqctl set_permissions -p messages striking ".*" ".*" ".*" &
) &

rabbitmq-server
