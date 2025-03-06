#!/bin/bash

# Check if running under WSL
if grep -qi Microsoft /proc/version; then
  echo "VOLUME_BASE=/mnt/c/Naftaly/WorkMaterials/automation-best-practices/Selenium/volumes" > .env
else
  echo "VOLUME_BASE=C:/Naftaly/WorkMaterials/automation-best-practices/Selenium/volumes" > .env
fi

# Run Docker Compose
# podman-compose -f docker-compose.yml up -d
