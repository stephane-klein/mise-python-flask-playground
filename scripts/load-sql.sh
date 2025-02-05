#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/../"

psql $(./scripts/get_postgres_url.sh) -f $1
