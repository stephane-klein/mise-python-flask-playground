POSTGRES_DOCKER_ID=$(docker compose ps postgres --format json | jq .ID -r)
if [ -z "$POSTGRES_DOCKER_ID" ]; then
    echo "Warning: No PostgreSQL Docker container is currently running"
else
    export POSTGRES_USER=$(docker inspect ${POSTGRES_DOCKER_ID} | jq -r '.[] | .Config.Env[] | select(startswith("POSTGRES_USER=")) | split("=")[1]')
    export POSTGRES_PASSWORD=$(docker inspect ${POSTGRES_DOCKER_ID} | jq -r '.[] | .Config.Env[] | select(startswith("POSTGRES_PASSWORD=")) | split("=")[1]')
    export POSTGRES_DB=$(docker inspect ${POSTGRES_DOCKER_ID} | jq -r '.[] | .Config.Env[] | select(startswith("POSTGRES_DB=")) | split("=")[1]')
    export POSTGRES_PORT=$(docker inspect ${POSTGRES_DOCKER_ID} | jq -r '.[].NetworkSettings.Ports["5432/tcp"][0].HostPort')
fi
