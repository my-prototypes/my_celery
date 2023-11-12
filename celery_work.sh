#!/bin/bash

# Start the Celery worker
celery -A consumer worker -l info