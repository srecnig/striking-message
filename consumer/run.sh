#!/bin/bash

VENV_PATH=/data/virtualenv

if [ ! -d ${VENV_PATH} ]; then
  echo "virtualenv does not exist yet"
  virtualenv ${VENV_PATH}
fi

source ${VENV_PATH}/bin/activate

echo 'Installing requirements'
pip install -r requirements.txt

if [ "${1}" = "run_dramatiq" ]; then
  echo "Starting dramatiq consumer"
  delay=1
  while true; do
    dramatiq striking_message --watch . --processes 1 --queues messages
    if [ $? -eq 3 ]; then
      echo "Connection error encountered on startup. Retrying in $delay second(s)..."
      sleep $delay
      delay=$((delay * 2))
    else
      exit $?
    fi
  done
else
  if [ -z "${1}" ]; then
    echo "Please provide what you want to start (run_dramatiq)..."
    exit 1;
  fi

  # just execute given command (e.g. bash)
  ${@}
fi
