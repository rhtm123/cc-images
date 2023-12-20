# Use a base image with Node.js and code-server pre-installed
FROM codercom/code-server:latest

# Set the working directory
WORKDIR /home/coder/project

# Copy the project files into the container
COPY . /home/coder/project

# Install additional dependencies if needed
# RUN apt-get update && apt-get install -y your-package-name

# Set up the code-server settings and extensions
# You can customize this part based on your requirements
RUN code-server --install-extension ms-python.python

# Expose the code-server port
EXPOSE 80

# Start code-server on container startup
ENTRYPOINT ["code-server", "--auth", "none", "--host", "0.0.0.0", "--port", "80", "--link"]
