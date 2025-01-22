#!/bin/bash
# wait for web service to be available
until curl -s http://web:5000; do
  echo "Waiting for web to be ready..."
  sleep 3
done
