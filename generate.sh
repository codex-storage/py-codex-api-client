#!/bin/sh

openapi-generator-cli generate \
  -g python \
  -i codex.yaml \
  --additional-properties="packageName=codex_client,projectName=Codex\ API\ Client,packageUrl=https://github.com/AuHau/py-codex-api" \
  --git-repo-id py-codex-api --git-user-id auhau \
  --http-user-agent py_codex_client
