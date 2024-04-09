#!/bin/bash

pipelineruns=$(kubectl get pipelineruns -o json --all-namespaces)
echo "$pipelineruns" | jq -r '.items[] | "\(.status.completionTime),\(.status.startTime),\(.metadata.namespace),\(.metadata.name),\(.status.conditions[].status),\(.status.conditions[].reason)"' | while IFS=',' read -r namespace name status reason start end
do
    # if [[ "$status" == "True" ]]; then
        start_s=$(date -d"$start" +%s)
        end_s=$(date -d"$end" +%s)
        duration=$((end_s-start_s))
        pretty_duration=$(printf '%dh:%dm:%ds\n' $((duration/3600)) $((duration%3600/60)) $((duration%60)))

        echo "PipelineRun $name in $namespace: succeeded: $status, reason: $reason, startTime: $start,endTime: $end, ran for $duration seconds ($pretty_duration)"
    # fi
done
