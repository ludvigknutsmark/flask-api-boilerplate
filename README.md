# flask-api-boilerplate
A simple setup for an API written in Flask.

# Build the docker image
```
docker build -t <tag name> .
```

# Run tests
```
docker run -t <tag name> pytest
```

# Start the app with the default port 5000
```
docker run -p 127.0.0.1:5000:5000/tcp -t <tag name>
```