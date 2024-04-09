#!/bin/bash

clear

# If kubectl port-forward -n $NS $PROMETHEUS_POD 9090:9090  & returns 
# Unable to listen on port 9090: Listeners failed to create with the following errors: 
#  [unable to create listener: Error listen tcp4 127.0.0.1:9090: bind: address already in use unable to create listener: Error listen tcp6 [::1]:9090: bind: address already in use]  
# find which processes are using that port with - 
# lsof -i :9090    

# app: prometheus

# To kill the process running on port 9090
runningProcessesOnPort9090=$(lsof -t -i:9090)
if [ -n "$runningProcessesOnPort9090" ]; then
    pkill -9 $runningProcessesOnPort9090
fi


NS=performance-monitoring # openshift-monitoring, performance-monitoring, appstudio-workload-monitoring, openshift-customer-monitoring
# PROMETHEUS_POD=$(oc get pods -n $NS -l app.kubernetes.io/component=prometheus -o jsonpath='{.items[0].metadata.name}')

#This will retrieve the name of the first pod in the specified namespace that has either the label app.kubernetes.io/component=prometheus or app=prometheus.
PROMETHEUS_POD=$(oc get pods -n $NS -l 'app.kubernetes.io/component=prometheus' -o jsonpath='{.items[0].metadata.name}' --ignore-not-found)

# trimming PROMETHEUS_POD
PROMETHEUS_POD=$(echo "$PROMETHEUS_POD" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//')
PODS=$(oc get pods -n $NS -l app.kubernetes.io/component=prometheus --output=name)

if [ -z "$PROMETHEUS_POD" ]; then
    PROMETHEUS_POD=$(oc get pods -n $NS -l 'app=prometheus' -o jsonpath='{.items[0].metadata.name}')
    PODS=$(oc get pods -n $NS -l app=prometheus --output=name)
    echo "PROMETHEUS_POD=$PROMETHEUS_POD"
else
    echo "PROMETHEUS_POD with labels of app.kubernetes.io/component=prometheus or app=prometheus are not found"
    echo "existings prometheus named pod labels are:"
    echo "$(oc get pods -n $NS -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.metadata.labels}{"\n"}{end}' | grep -i prometheus)" 
  exit 1
fi

# FIRST_POD=$(echo $PODS | tr ' ' '\n' | head -n 1)

metricsFilename="metrics-$NS.csv"
targetsFilename="targets-$NS.json"

echo "namespace=$NS"
echo "metrics file is: $metricsFilename"
echo "targets file is: $targetsFilename"

rm $targetsFilename 2>/dev/null

# metrics=$(oc rsh -n $NS PROMETHEUS_POD curl -s http://localhost:9090/api/v1/label/__name__/values | jq -r '.data[]')

# this could work if the pod has curl utility installed
# metrics=$(oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq -r '.data | to_entries[] | select(.value[].type and .value[].help) | [.key, .value[].type, .value[].help] | @csv' | sort -u)

# Otherwise use the following:
kubectl port-forward -n $NS $PROMETHEUS_POD 9090:9090 >/dev/null &      
PID=$(ps aux | grep "kubectl port-forward -n $NS $PROMETHEUS_POD 9090:9090" | grep -v grep | awk '{print $2}')      
metrics=$(curl -s http://localhost:9090/api/v1/metadata | jq -r '.data | to_entries[] | select(.value[].type and .value[].help) | [.key, .value[].type, .value[].help] | @csv' | sort -u)
pkill -P $PID

echo "$metrics" > $metricsFilename 

for pod in $PODS; do
    echo "Retrieving metrics targets metadata from $pod..."
    sleep 1 

    podname=$(basename $pod)
    podTargetsFilename="targets-$NS-$podname.json"

    # targets=$(oc rsh -n $NS $pod curl -s http://localhost:9090/api/v1/targets/metadata | jq -r .)
     
    kubectl port-forward -n $NS $pod 9090:9090 >/dev/null &      
    PID=$(ps aux | grep "kubectl port-forward -n $NS $pod 9090:9090" | grep -v grep | awk '{print $2}')   
    targets=$(curl -s http://localhost:9090/api/v1/targets/metadata | jq -r .)
    pkill -P $PID

    echo $targets > $podTargetsFilename
    
    # beutify targets json file
    jq --indent 4 . $podTargetsFilename > tmpfile.json && sleep 1 && mv tmpfile.json $podTargetsFilename

    # append metrics to all metrics file
    cat $podTargetsFilename >> $targetsFilename
    rm $podTargetsFilename

    # separate metrics to one per line
    # cat $metricsFilename | tr ' ' '\n' > tmpfile.json && sleep 1 && mv tmpfile.json $metricsFilename   
done




# fetch unique mand sorted metrics list
# cat $allMetricsFilename  | sort -u | uniq -u > $uniqueMetricsFGilename

ls -ltra *.json *.csv

# fetch metric names, type and help field
# oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq -r '.data | to_entries[] | select(.value[].type and .value[].help) | [.key, .value[].type, .value[].help] | @csv' | sort -u

# oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq -r '.data | to_entries[] | select(.value[].type and .value[].help) | [.key, .value[].type, .value[].help] | @csv' | sort -u | tee all_unique_metrics.txt 

# This command sometimes displays 4 fields in a line with two type field values, we need to fix it to discard in this case the third field
# fix it
# awk -F',' 'NF==4{$3=""; print $0} NF==3{print $0}' input.csv > output.csv



# fetch metric names, type and help field in table format
# oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq -r '.data | to_entries[] | select(.value[].type and .value[].help) | [.key, .value[].type, .value[].help] | @tsv' | sort -u



# Variables
# NS=openshift-monitoring
# PROMETHEUS_POD=$(oc get pods -n $NS -l app.kubernetes.io/component=prometheus -o jsonpath='{.items[0].metadata.name}')
# METRICS_FILE=$uniqueMetricsFGilename
# METRICS_URL="http://localhost:9090/api/v1/targets/metadata"

# example metric is "workqueue_work_duration_seconds"
# METRIC_NAME="http_requests_total"
# metric="http_requests_total"

# 
# Read all metrics names from file
# while read METRIC_NAME; do
#   Fetch metric attributes

#   The following outputs one row with two fields one per the metric's type and the other for it's help field
    # metric_attributes=$(oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq -r '.data["$METRIC_NAME"][0] | [.type, .help] | @csv')


#   The below displays all occurences of the metric related records (more than 1)
#   metric_attributes=$(oc rsh -n $NS $PROMETHEUS_POD curl -s $METRICS_URL | jq -r ".data[] | select(.metric == \"$metric\")")

#   The followoing returns a json output with no hierarchies - all fields in the same level
#   oc rsh -n $NS $PROMETHEUS_POD curl -sG "http://localhost:9090/api/v1/query" --data-urlencode "query=http_requests_total" | jq '.data.result[] | .metric'

#   The following returns a csv output of the metrics with multiple records
#   oc rsh -n $NS $PROMETHEUS_POD curl -s $METRICS_URL \                                                                                                                                                                                     ─╯
#     | jq -r ".data[] | select(.metric == \"$metric\") | {metric: .metric, value: .value, type: .type, help: .help} | [.] \
#     | group_by(.metric, .value) | .[] | first | [.metric, .value, .type, .help] | @csv"


#   The following outputs two rows one per the metric's type and the other for it's help field
#   oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq '.["data"]["workqueue_work_duration_seconds"][0]["type", "help"]'  

#   as above in csv format for all metrics
#   oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq -r '.data[][0] | [.metric, .type, .help] | @csv'


#   output all valid metrics records as csv with only the type and help fields
#   oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq -r '.data[][0] | [.type, .help] | @csv'  | sort -u | grep -v "unknown" | grep "\"" | wc -l 

#   output all metricses type and help fields in a table format
#   oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq -r '.data[][0] | [.type, .help] | @csv' | column -t -s ','

#   return as above but for all the metrics in json format
#   oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq '.["data"][][0] | {type, help}' | column -t -s $'\t'

#   return as above but for all the metrics in csv format
#   oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata | jq '.["data"][][0] | {type, help} | @csv' | column -t -s $'\t'

# output table output of all metrics type and help fields
#   oc rsh -n $NS $PROMETHEUS_POD curl -s http://localhost:9090/api/v1/metadata \                                                                                                                                                            ─╯
    # | jq -r '.data[][0] | [.type, .help] | @csv' \
    # | cut -d',' -f1,2 \
    # | awk -F',' '{printf "%-20s%-150s\n", $1, substr($2, 0, 150)}'


#   Output metric attributes
#   echo "Attributes for metric $metric:"
#   echo "$metric_attributes"
#   echo "============================="
# done < "$METRICS_FILE"

