import os
from dockerspawner import DockerSpawner

c = get_config()  # noqa

c.JupyterHub.spawner_class = DockerSpawner
c.DockerSpawner.image = os.environ["DOCKER_NOTEBOOK_IMAGE"]
# Connect containers to this Docker network
network_name = os.environ["DOCKER_NETWORK_NAME"]
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name

# Explicitly set notebook directory because we'll be mounting a volume to it.
# Most `jupyter/docker-stacks` *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = "/home/jovyan/work"
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = {
    "/home/{username}": {
        "bind": "/home/jovyan", 
        "mode": "rw"
        }
}
c.DockerSpawner.environment = {
    "CHOWN_HOME": "yes",
    "CHOWN_HOME_OPTS": "-R",
    "NB_UID": "1000",  # Default jovyan UID in stock images
    "NB_GID": "100",  # Default users GID in stock images
}
c.DockerSpawner.extra_create_kwargs = {"user": "root"}  # Start as root to chown
c.DockerSpawner.user = "jovyan"  # Switch to jovyan after chown

# Remove containers once they are stopped
c.DockerSpawner.remove = True
# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

c.Authenticator.allow_all = True
# Allowed admins
admin = os.environ.get("JUPYTERHUB_ADMIN")
if admin:
    c.Authenticator.admin_users = [admin]

c.Spawner.start_timeout = 600
c.Spawner.http_timeout = 600
c.DockerSpawner.start_timeout = 600
c.DockerSpawner.http_timeout = 600
c.JupyterHub.base_url = "/jupyterhub/"
c.JupyterHub.bind_url = "http://0.0.0.0:8000"
c.Spawner.default_url = "/lab"
c.Spawner.args = ['--allow-root']
