#!/bin/bash

if [ ${DEV:-False} = 'true' ]; then
  # Run celery worker in the background
  poetry run celery -A lwca.entry.celery worker --loglevel=info --pidfile=/var/run/celery/worker.pid &

  # Run celery beat in the background
  poetry run celery -A lwca.entry.celery beat --loglevel=info --pidfile=/var/run/celery/beat.pid &
else
  # Run celery worker in the foreground
  poetry run celery -A lwca.entry.celery worker --loglevel=info &

  # Run celery beat in the foreground
  poetry run celery -A lwca.entry.celery beat --loglevel=info
fi

# Wait for background processes to finish if in DEV mode
if [ ${DEV:-False} = 'true' ]; then
  wait
fi