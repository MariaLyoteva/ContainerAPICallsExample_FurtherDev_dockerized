# Docker-based Example Project

This is a simple example project that demonstrates the use of Docker and Docker Compose to set up a frontend, backend, and Nginx reverse proxy.

## Project Structure

The project consists of the following components:

1. **Frontend**: A frontend application, located in the `frontend` directory.
2. **Backend**: A backend application, located in the `backend` directory.
3. **Nginx Reverse Proxy**: An Nginx server that acts as a reverse proxy, forwarding requests to the frontend and backend services.

Because of the NGINX reverse-proxy, we are able to call our backend with just `/api/` (the reverse-proxy is the only one exposed to the public and forwards requests with `/` to the fontend and requests with `/api` to the backend). This allows us to not worry about CORS-issues as everything is on the same domain. A good tutorial on this setup can be found [here](https://codingwithmanny.medium.com/create-an-nginx-reverse-proxy-with-docker-a1c0aa9078f1).

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository

2. Navigate to the project directory

3. Build and start the Docker containers with `docker compose up`


This command will build the Docker images for the frontend, backend, and Nginx reverse proxy, and start the containers.

4. Open your web browser and visit `http://localhost`. You should see the frontend application being served by the Nginx reverse proxy.

## Project Structure Explanation

- The `frontend` and `backend` directories contain the respective application code and Dockerfiles.
- The `nginx.conf` file is the Nginx configuration file that defines the reverse proxy settings.
- The `docker-compose.yml` file defines the services, networks, and volumes for the project.

## Accessing the Services

- **Frontend**: The frontend application is accessible at `http://localhost`.
- **Backend**: The backend application is not directly accessible from the outside. It can be accessed by the frontend application through the `app-network` network.
- **Nginx Reverse Proxy**: The Nginx reverse proxy is listening on port 80 (HTTP) and forwarding requests to the frontend and backend services.

## Stopping the Project

To stop the project, run the command `docker compose down`


This will stop and remove the containers, networks, and volumes created by the Docker Compose setup.

## Troubleshooting

If you encounter any issues, you can check the logs of the individual containers using `docker logs myexamplefrontend`

Make sure that the Dockerfiles and the `nginx.conf` file are correctly configured for your specific application requirements.

## Conclusion

This project demonstrates a basic setup of a Docker-based application with a frontend, backend, and Nginx reverse proxy. You can use this as a starting point to build more complex applications and explore the benefits of containerization and Docker Compose.






