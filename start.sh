#!/bin/bash

export FLASK_APP=app.py
if [ -z "$PORT" ]
then
  flask run --host=0.0.0.0 --port=5000
else
  flask run --host=0.0.0.0 --port="$PORT"
fi
