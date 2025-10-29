# Lab

This repository contains the configuration for a server environment that integrates **JupyterHub**, **NGINX**, and **Ollama** using **Docker**.

## Overview

The **Lab** setup provides a flexible and containerized environment for running multi-user Jupyter notebooks with secure proxying via NGINX and AI model serving through Ollama.

### Components

- **JupyterHub** – Manages multiple Jupyter notebook servers for users.
- **NGINX** – Acts as a reverse proxy for handling HTTPS, load balancing, and routing.
- **Ollama** – Provides access to locally hosted LLMs for AI-powered notebooks.

## Structure

```

lab/
├── docker-compose.yml     # Main Docker Compose configuration
├── jupyterhub/
│   └── jupyterhub_config.py
├── nginx/
│   └── default.conf
└── Dockerfile

````

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Adequate hardware for Ollama model inference (GPU recommended)

### Setup

1. Clone the repository:
   ```bash
     git clone https://github.com/<your-username>/Lab.git
     cd Lab
   ```

2. Start all services:

   ```bash
     docker compose up -d
   ```

3. Access the services:

   * **JupyterHub**: [http://localhost:8000](http://localhost:8000)
   * **NGINX (Proxy)**: [http://localhost](http://localhost)
   * **Ollama API**: [http://localhost:11434](http://localhost:11434)

### Stopping Services

```bash
  docker compose down
```

## Customization

* Modify `nginx/default.conf` for custom routes or SSL setup.
* Update `jupyterhub_config.py` to change authentication or spawner settings.

## License

This project is licensed under the [MIT License](LICENSE).

```
