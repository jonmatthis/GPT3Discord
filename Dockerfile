# Use the official Python base image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR .
COPY . .


# Install any needed packages specified in requirements.txt
RUN pip install  -r requirements.txt

# # Copy the rest of the application code into the container
# COPY /cogs /app/cogs
# COPY /models /app/models
# COPY /openers /app/openers
# COPY /services /app/services
# COPY /tests /app/tests
# COPY conversation_starter_pretext.txt /app
# COPY conversation_starter_pretext_minimal.txt /app
# COPY image_optimizer_pretext.txt /app
# COPY language_detection_pretext.txt /app
#
# COPY gptdiscord.py /app
#
# COPY .env /app


# Expose the port the app runs on
EXPOSE 8080

# Run the command to start the application
CMD ["python", "gptdiscord.py"]
