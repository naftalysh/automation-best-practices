#!/bin/bash

watch_resource() {
  local resource_type=$1
  echo "Watching ${resource_type}"
  kubectl get "${resource_type}" --all-namespaces --watch &
}

# Add the resource types you want to watch
watch_resource namespaces
watch_resource deployments
watch_resource services
watch_resource pods
watch_resource pipelineruns
watch_resource taskruns
# Add more resource types as needed

# Wait for all background watch processes
wait
