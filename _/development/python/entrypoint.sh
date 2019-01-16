#!/bin/bash -e

source /etc/environment

if [ "$#" -eq  "0" ]
  then
    echo "No argument(s) supplied"
    exit 1;
else
  CMD=${1}
fi

chown -R $HOSTUSER:$HOSTUSER /data

if [ "$CMD" == "shell" ]; then
    echo "Welcome to the dev container as unpriviledged user '${HOSTUSER}'"
    su $HOSTUSER -s /bin/bash
elif [ "$CMD" == "root_shell" ]; then
    echo "Welcome to the dev container as root"
    bash
else
    echo "Running ${*} as '${HOSTUSER}'"
    su $HOSTUSER -c "$RUN_COMMAND ${*}"
fi
