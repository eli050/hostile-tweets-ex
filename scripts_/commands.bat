# This script builds a Docker image for a FastAPI application.
docker build -t eligil/tweets-app:0.1 .

# This script pushes the Docker image to DockerHub.
docker run -d --name tweets-app -p 8000:8000 eligil/tweets-app:0.1