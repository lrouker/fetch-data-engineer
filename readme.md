docker build --pull --rm -f "Dockerfile.dockerfile" -t fetch:latest "."

docker run -p 5000:5000 fetch:latest