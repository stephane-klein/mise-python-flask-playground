#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../"

source ./scripts/load_postgres_variables.sh
if [ -z "$POSTGRES_PORT" ]; then
    exit 1
fi

echo postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:${POSTGRES_PORT}/${POSTGRES_DB}
