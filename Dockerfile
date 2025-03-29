# Use official Python image
FROM python:3.9-slim

# Create a non-root user and switch to it
RUN useradd -m myuser
WORKDIR /home/myuser/app
COPY --chown=myuser:myuser . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Switch to non-root user
USER myuser

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "-m", "app.main"]
