#!/bin/bash

watch_resource() {
  local resource_type=$1
  kubectl get "${resource_type}" --all-namespaces --watch --output-watch-events -o json | jq --unbuffered --arg type "${resource_type}" 'select(.type == "ADDED" or .type == "MODIFIED" or .type == "DELETED") | {time: .object.metadata.creationTimestamp, type: .type, resource: $type, object: .object}' &
}

export -f watch_resource

# Add the resource types you want to watch
resources=(
  "namespaces"
  "deployments"
  "services"
  "pods"
  "pipelineruns"
  "taskruns"
  # Add more resource types as needed
)

printf "%s\n" "${resources[@]}" | xargs -I % -P "${#resources[@]}" bash -c "watch_resource %"

wait


# The xargs command will run the watch_resource function for each resource type specified in the resources array, using the -P option to run them in parallel.