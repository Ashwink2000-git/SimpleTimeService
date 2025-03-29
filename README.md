# SimpleTimeService

A simple microservice that returns current timestamp and visitor's IP address in JSON format.

## Features

- Returns current UTC timestamp in ISO format
- Detects visitor's IP address (handles X-Forwarded-For header)
- Runs as non-root user in container
- Lightweight Flask implementation

## Prerequisites

- Docker installed on your system

## Running the Service

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t simple-time-service .
