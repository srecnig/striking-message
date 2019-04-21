#!/bin/bash -e

VENV_PATH=/data/virtualenv

if [ ! -d ${VENV_PATH} ]; then
  echo "virtualenv does not exist yet"
  virtualenv ${VENV_PATH}
fi

source ${VENV_PATH}/bin/activate

echo 'Installing requirements'
pip install -r requirements.txt

if [ "${1}" = "nothing" ]; then
  echo "Starting nothing..."
else
  if [ -z "${1}" ]; then
    echo "Please provide what you want to start (nothing)..."
    exit 1;
  fi

  # just execute given command (e.g. bash)
  ${@}
fi
