#!/bin/bash

# Start solr
cd /home/blacklight/blacklight && bundle exec solr_wrapper&
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start solr_wrapper: $status"
  exit $status
fi
sleep 120
# Start blacklight
cd /home/blacklight/blacklight && rails server -p 3000 -b 0.0.0.0&
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start blacklight: $status"
  exit $status
fi
sudo python3 /home/blacklight/blacklight/dirwatch.py&
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start blacklight: $status"
  exit $status
fi
while sleep 60; do
  ps aux |grep solr_wrapper |grep -q -v grep
  PROCESS_1_STATUS=$?
  ps aux |grep blacklight |grep -q -v grep
  PROCESS_2_STATUS=$?
  ps aux |grep dirwatch |grep -q -v grep
  PROCESS_3_STATUS=$?
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    exit 1
  fi
done
