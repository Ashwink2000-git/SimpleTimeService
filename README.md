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
    ```
2.Run the container:
 ```bash
   docker run -p 8080:8080 simple-time-service
 ```
3.Access the service:
```bash
   curl http://localhost:8080
 ```


## How to Use This Service

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/SimpleTimeService.git
   cd SimpleTimeService
   ```
2. Build and run the Docker container as shown in the README.
3. Test the service:
   ```bash
   curl http://localhost:8080
   ```
4.To stop the service:
   ```bash
   docker stop <container-id>
   ```

   

