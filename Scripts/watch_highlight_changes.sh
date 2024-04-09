#!/bin/bash

watch_resource() {
  local resource_type=$1
  kubectl get "${resource_type}" --all-namespaces --watch --output-watch-events -o json |
    jq --unbuffered --arg type "${resource_type}" 'select(.type == "MODIFIED") | {time: .object.metadata.creationTimestamp, type: .type, resource: $type, object: .object, prevObject: .prevObject}' |
    jq --unbuffered -r '@json' |
    while IFS=$'\n' read -r line; do
      echo "$line" | diff -u <(echo "$line" | jq -r .prevObject) <(echo "$line" | jq -r .object) --label "Previous" --label "Current" | tail -n +3
    done
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
