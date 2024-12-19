#!/bin/sh

if [ -z "$1" ]; then
  echo "No version supplied"
  exit 1
fi


openapi-generator-cli generate \
  -t .openapi-generator/templates \
  -g python \
  -i codex.yaml \
  --additional-properties="packageName=codex_api_client,projectName=codex-api-client,packageUrl=https://github.com/codex-storage/py-codex-api-client,packageVersion=$1" \
  --git-repo-id py-codex-api-client --git-user-id codex-storage \
  --http-user-agent py_codex_api_client
