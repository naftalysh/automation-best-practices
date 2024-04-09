#!/bin/bash

clear

kubectl get pods --all-namespaces -o json > resources.json
kubectl get services --all-namespaces -o json >> resources.json
kubectl get deployments --all-namespaces -o json >> resources.json
# Add more resource types as needed

jq -s '.[0].items as $pods | .[1].items as $services | .[2].items as $deployments | $pods + $services + $deployments | sort_by(.metadata.creationTimestamp) | reverse | .[]' resources.json 
