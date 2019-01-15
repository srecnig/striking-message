#!/bin/sh

if [ "$#" -eq  "0" ]
  then
    CMD="shell"
 else
  CMD=${@}
fi

docker-compose run --rm consumer ${CMD}
