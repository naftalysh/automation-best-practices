## GPG 
Signing a commit with GPG key

# Create my GPG key
# <https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key>
# <https://www.nisum.com/nisum-knows/use-public-and-private-keys-for-git-commits-with-gpg>

# OC commands
oc whoami --show-console # show console


# Getting DOCKER_CONFIG_JSON procedure
export REGISTRY_AUTH_FILE=/home/$USER/auth.json  
REGISTRY_AUTH_FILE=$REGISTRY_AUTH_FILE docker login docker.io -u $USER
DOCKER_CONFIG_JSON=$(cat $REGISTRY_AUTH_FILE | base64 -w 0)

# Getting QUAY_CONFIG_JSON procedure
export REGISTRY_AUTH_FILE=/home/$USER/auth.json  
REGISTRY_AUTH_FILE=$REGISTRY_AUTH_FILE podman login quay.io -u $USER
QUAY_CONFIG_JSON=$(cat $REGISTRY_AUTH_FILE | base64 -w 0)
echo "QUAY_CONFIG_JSON=$QUAY_CONFIG_JSON"

# Docker-IO auth
export DOCKER_IO_AUTH=""


# To use the access token from your Docker CLI client
1. Run docker login -u username
2. At the prompt, enter the personal access token.
#

# method to extract the token
1. go to my user's QUAY settings - https://quay.io/user/username/?tab=settings
2. Click on "Docker Configuration" and click on Download username-auth.json
3. export QUAY_TOKEN=$(base64 < ~/Downloads/username-auth\ \(1\).json

# diving into an image
dive quay.io/  repo_name/repo_name:tag_name

# Fedora 30.04
podman build --layers=false \
 -t fedora-34 -f ./images/cli-fedora-34/Dockerfile .

# Verify image created
podman images

# Tag and push the image to Quay.io
podman tag fedora-34 \
 quay.io/username/fedora-34:v2

podman tag fedora-34 \
 quay.io/username/fedora-34:latest

podman login quay.io -u username

podman push \
 quay.io/username/fedora-34

# Install OC client application (ex: for version 4.11.23)

# version1 for a container

OC_VERSION="4.11.23"
wget <https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/$OC_VERSION/openshift-client-linux-$OC_VERSION.tar.gz> \
 -O /tmp/openshift-client.tar.gz &&\
 tar xzf /tmp/openshift-client.tar.gz -C /usr/local/bin -U oc kubectl &&\
 rm /tmp/openshift-client.tar.gz

# version2 for a computer

OC_VERSION="4.11.23"
wget <https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/$OC_VERSION/openshift-client-linux-$OC_VERSION.tar.gz> \
 -O /tmp/openshift-client.tar.gz &&\
 tar xzf /tmp/openshift-client.tar.gz -C /tmp -U oc kubectl &&\
 sudo cp -P /tmp/oc /usr/local/bin/oc && sudo cp -P /tmp/kubectl /usr/local/bin/kubectl &&\
 rm /tmp/openshift-client.tar.gz /tmp/oc /tmp/kubectl

 1. wget https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/4.11.23/ -O /tmp/openshift-client.tar.gz
 2. tar xzf /tmp/openshift-client.tar.gz -C /tmp -U oc kubectl

# version2 for a computer

wget <https://mirror.openshift.com/pub/openshift-v4/x86_64/clients/ocp/stable-4.11/openshift-client-linux-4.11.25.tar.gz> \
 -O /tmp/openshift-client.tar.gz &&\
 tar xzf /tmp/openshift-client.tar.gz -C /tmp -U oc kubectl &&\
 sudo cp -P /tmp/oc /usr/local/bin/oc && sudo cp -P /tmp/kubectl /usr/local/bin/kubectl &&\
 sudo cp -P /tmp/oc /home/username/.local/bin/oc && sudo cp -P /tmp/kubectl /home/username/.local/bin/kubectl &&\
 rm /tmp/openshift-client.tar.gz /tmp/oc /tmp/kubectl

# To list all Roles on your cluster, you need to use the command line tool (kubectl)

kubectl get rolebindings,clusterrolebindings --all-namespaces -o custom-columns='KIND:kind,NAMESPACE:metadata.namespace,NAME:metadata.name,SERVICE_ACCOUNTS:subjects[?(@.kind=="ServiceAccount")].name'

# Than you can extract the yaml file as in this example

kubectl get clusterrolebindings prometheus -o yaml

# To list all ClusterRoles on the cluster

kubectl get clusterroles --all-namespaces -o custom-columns='KIND:kind,NAMESPACE:metadata.namespace,NAME:metadata.name,SERVICE_ACCOUNTS:subjects[?(@.kind=="ServiceAccount")].name'

# To see which Kubernetes Entity2 are and aren't in a namespace

# In a namespace

kubectl api-Entity2 --namespaced=true

# Not in a namespace

kubectl api-Entity2 --namespaced=false

# To create a local role for a project, run the following command

$ oc create role <name> --verb=<verb> --resource=<resource> -n <project>

In this command, specify:

<name>, the local role’s name
<verb>, a comma-separated list of the verbs to apply to the role
<resource>, the Entity2 that the role applies to
<project>, the project name

echo "Adding cluster-admin role to the group tekton-team-admins"
oc adm policy add-cluster-role-to-group cluster-admin tekton-team-admins

echo "Adding admin role to the group tekton-team in namespace \"pipelines-ci\""
oc adm policy add-role-to-group admin tekton-team -n pipelines-ci

---- Adding ClusterRoleBinding ----
oc adm policy add-cluster-role-to-user <role> user1

Ex: Allowing user1 to create project
oc adm policy add-cluster-role-to-user self-provisioner user1

Ex: Allowing user1 to create namespace
oc adm policy add-cluster-role-to-user nsrole user1

--- Add a clusterRole ---
Ex: ClusterRole for a non-namespaced resource StorageClass (or, sc in short) -
kubectl create clusterrole scrole --verb=create,update,patch,delete --resource=sc

Ex: ClusterRole for namespaces resource (kind = NetNamespace, name = netnamespaces)
kubectl create clusterrole nsrole --verb=list,create,update,delete --resource=ns

---Now, Adding ClusterRoleBinding of the nsrole ClusterRole to user1
oc adm policy add-cluster-role-to-user nsrole user1


# get all role related attributes of namespace resource
kubectl api-Entity2 -o wide | grep "Namespace\|VERBS"
--> namespaces ns v1 false Namespace [create delete get list patch update watch]

# get all role related attributes of ConfigMap resource
kubectl api-Entity2 -o wide | grep "cm\|VERBS"
--> configmaps cm v1 true ConfigMap [create delete deletecollection get list patch update watch]

# remove finalizers from an crd object to let it delete
(<https://kubernetes.io/blog/2021/05/14/using-finalizers-to-control-deletion/>
<https://kubernetes.io/docs/tasks/manage-kubernetes-objects/update-api-object-kubectl-patch/>)

# Here's a demonstration of using the patch command to remove finalizers. If we want to delete an object, we can simply patch it on the command line to remove the finalizers. In this way, the deletion that was running in the background will complete and the object will be deleted. When we attempt to get that configmap, it will be gone.

kubectl patch configmap/mymap \
 --type json \
 --patch='[ { "op": "remove", "path": "/metadata/finalizers" } ]'
configmap/mymap patched
[1]+ Done kubectl delete configmap/mymap

kubectl get configmap/mymap -o yaml
Error from server (NotFound): configmaps "mymap" not found

--------------- Technical procedures ------------------------------

1. # Moving vault image from Docker into my personal repo in quay - <https://quay.io/username/vault:1.9.2>
   a. podman pull hashicorp/vault:1.9.2
   b. podman tag hashicorp/vault quay.io/username/vault:1.9.2
   c. podman login quay.io -u username
   d. podman push quay.io/username/vault:1.9.2
   e. Go into quay.io into my repo and change its settings to make it public

--------------- Problems and Mitigations ---------------------------
1. Worker node is overcommited for some resource
   Ex:
   "
   This node’s CPU Entity2 are overcommitted.
   The total CPU resource limit of all pods exceeds the node’s total capacity. Pod performance will be throttled under high load.
   "

Solution
---

Setup openshift or kubernetes to allow 200% overcommiting of a resource
Need to search for the Solution..
<https://docs.openshift.com/container-platform/4.9/nodes/clusters/nodes-cluster-overcommit.html>


GO installation
###

install npm - sudo install npm
install gauge - npm install -g @getgauge/cli --unsafe-perm

## Install Plugins
Install go plugin
> gauge install go

Install html plugin
> gauge install html-report

Install xml-report
> gauge install xml-report


--------------------- Utilities
# Creating a tar compressed file from a directory
tar -cvzf {tar-filename} /path/to/dir

# Extracting a compressed tar file
tar -xvzf tarfile.tar.gz

# How to recursively find and list the latest modified files in a directory with subdirectories and times
<https://stackoverflow.com/questions/5566310/how-to-recursively-find-and-list-the-latest-modified-files-in-a-directory-with-s>

find $1 -type f -print0 | xargs -0 stat --format '%Y :%y %n' | sort -nr | cut -d: -f2- | head
find $1 -type f -exec stat --format '%Y :%y %n' "{}" \; | sort -nr | cut -d: -f2- | head

# How to recursively find and list the kubeconfig file in a directory with subdirectories and times

sudo find /. -name kubeconfig -type f -printf "%T@ %Tc %p\n" | sort -n

# find shell scripts (\*.sh) that includes the string "code" , search from root (/)

find / -type f -name '\*.sh' -exec grep -l 'code' {} +

# the script file to be found as the substring "code" in it's name

find / -type f -name '_code_.sh'

# Exclude erronuous lines
find / -type f -name '_code_.sh' 2>&1 | grep -v 'Permission denied\|Invalid argument'  
Or
find / -type f -name '\*code.sh' 2>&1 | grep -v 'Permission denied\|Invalid argument'

# sort results descending
find / -type f -name 'tests*.list' 2>&1 | grep -v 'Permission denied\|Invalid argument' | sort -r

# sort results descending and print file modified date
find / -type f -name 'tests*.list' 2>&1 | grep -v 'Permission denied\|Invalid argument' | xargs -I {} ls -lt {} | sort -k 6,7r



# GinkGo suit "testSuit" tests
# ============================

make build && ./bin/e2e-test --ginkgo.show-node-events --ginkgo.v --ginkgo.focus="suit-name"
make build && ./bin/e2e-test --ginkgo.v --ginkgo.focus="suit-name"
make build && ./bin/e2e-test --ginkgo.show-node-events --ginkgo.trace --ginkgo.focus="suit-name"

make build && ./bin/e2e-test --ginkgo.v --ginkgo.focus="suit-name"
make build && ./bin/e2e-test --ginkgo.v --ginkgo.label-filter="suit-name"

# Another command

${WORKSPACE}/tmp/e2e-tests/bin/e2e-test  --ginkgo.junit-report="${ARTIFACTS_DIR}"/e2e-report.xml -webhookConfigPath="./webhookConfig.yml" -config-suites="${WORKSPACE}/tmp/e2e-tests/tests/e2e-demos/config/default.yaml"

# Snippets

# ========

// wait until both namespaces have been created
// Eventually(func() bool {
// // demo and managed namespaces should not exist and status = active
// ret1 := framework.CommonController.CheckIfNamespaceExists(failure1SourceNamespace)
// ret2 := framework.CommonController.CheckIfNamespaceExists(failure1ManagedNamespace)

// // return True if only one namespace still exists
// // return False if both demo and managed namespaces don't exist
// return ret1 && ret2

// }, avgPipelineCompletionTime, defaultInterval).Should(BeTrue(), "Timedout creating namespaces")

      // in common cntroller.go file
     //CheckIfNamespaceExists - find if a namespace exists
        func (h *SuiteController) CheckIfNamespaceExists(name string) bool {
          _, err := h.KubeInterface().CoreV1().Namespaces().Get(context.TODO(), name, metav1.GetOptions{})
          return err == nil
        }

# Tech Solutions
# ==============

# TEKTON
# ======
# TEKTON Bundle

Web link: <https://vinamra-jain.medium.com/publishing-tekton-Entity2-as-bundles-on-oci-registry-c4644d2af83f>

0. Tekton bundle help
   tkn bundle --help

1. List contents of a bundle
   tkn bundle list quay.io/organization/repository-name:tag-name

2. Extract contents of a task within the Bundle
   tkn bundle list quay.io/organization/repository-name:tag-name task task-name -o yaml

3. Extract contents of a pipeline within the Bundle
   quay.io/organization/repository-name:tag-name pipeline pipeline-name -o yaml
   
4. And if you want to install the Task on cluster then you can just pipe it with kubectl :
   tkn bundle list quay.io/organization/repository-name:tag-name task task-name -o yaml | kubectl create -f -
   --> task.tekton.dev/task-name created

5. Publish a new Tekton Bundle to a registry by passing in a set of Tekton objects via files, arguments or standard in:
   - tkn bundle push docker.io/myorg/mybundle:latest "apiVersion: tekton.dev/v1beta1 kind: Pipeline..."
   - tkn bundle push docker.io/myorg/mybundle:1.0 -f path/to/my/file.json
   - cat path/to/my/unified_yaml_file.yaml | tkn bundle push myprivateregistry.com/myorg/mybundle -f -

# GINKGO

make build && ./bin/e2e-test --ginkgo.progress --ginkgo.v --ginkgo.focus="test-suite"
make build && ./bin/e2e-test --ginkgo.v --ginkgo.focus="test-suite"
make build && ./bin/e2e-test --ginkgo.progress --ginkgo.trace --ginkgo.focus="test-suite"

# It failed on the go mod vendor part

# Solution
git restore go.mod
git restore go.sum
go mod tidy -compat=1.17

Now: go mod vendor works

Controlling Output Formatting
--ginkgo.no-color
If set, suppress color output in default reporter.
--ginkgo.slow-spec-threshold [duration] (default: 5s)
Specs that take longer to run than this threshold are flagged as slow by the
default reporter.
--ginkgo.v
If set, emits more output including GinkgoWriter contents.
--ginkgo.vv
If set, emits with maximal verbosity - includes skipped and pending tests.
--ginkgo.succinct
If set, default reporter prints out a very succinct report
--ginkgo.trace
If set, default reporter prints out the full stack trace when a failure
occurs
--ginkgo.always-emit-ginkgo-writer
If set, default reporter prints out captured output of passed tests.
--ginkgo.json-report [filename.json]
If set, Ginkgo will generate a JSON-formatted test report at the specified
location.
--ginkgo.junit-report [filename.xml]
If set, Ginkgo will generate a conformant junit test report in the specified
file.
--ginkgo.teamcity-report [filename]
If set, Ginkgo will generate a Teamcity-formatted test report at the
specified location.

# Debugging Tests
In addition to these flags, Ginkgo supports a few debugging environment
variables. To change the parallel server protocol set GINKGO_PARALLEL_PROTOCOL
to HTTP. To avoid pruning callstacks set GINKGO_PRUNE_STACK to FALSE.
--ginkgo.dry-run
If set, ginkgo will walk the test hierarchy without actually running
anything. Best paired with -v.
--ginkgo.progress
If set, ginkgo will emit progress information as each spec runs to the
GinkgoWriter.
--ginkgo.timeout [duration] (default: 1h)
Test suite fails if it does not complete within the specified timeout.
--ginkgo.output-interceptor-mode [dup, swap, or none]
If set, ginkgo will use the specified output interception strategy when
running in parallel. Defaults to dup on unix and swap on windows.

Go test flags

# GO tests coverage
# =================
go tool cover -func cover.out to show the test coverage per function. Pretty helpful.
go tool cover -html=cover.out

# GO
# ==

Installing Packages - (<https://www.digitalocean.com/community/tutorials/importing-packages-in-go>)

# Linux
# =====

Copy directories and exclude specific directories
# Method 1
rsync -av --progress --exclude=".git" --exclude=".github" /home/username/Setup/project-name/sub-directory1/ /home/username/Setup/project-name/sub-directory2/

Repeatedly run a shell command until it fails?

Solution#1:
My current solution is to write an untilfail script:

# !/bin/bash
$@
while [ $? -eq 0 ]; do
$@
done
Then use it:

untilfail ./runtest

Solution #2:
while ./runtest; do :; done

# This will stop the loop when ./runtest returns a nonzero exit code (which is usually indicative of failure)


# ===============================================
# Utilities installation
# ===============================================
cosign -
<https://docs.sigstore.dev/cosign/installation/>


# diving into an image
dive quay.io/image-path

# =====
# Linux
# =====
- How do I find out what shell I am using on Linux/Unix?
echo $SHELL (<https://www.cyberciti.biz/tips/how-do-i-find-out-what-shell-im-using.html>)


# ==================================
# Testing yaml policies with datress
# ==================================
datree test ./config/manager/network_policy.yaml
datree test ~/.datree/k8s-demo.yaml

# =====================================
# Testing yaml policies with kube-score
# =====================================
./home/username/Setup/krew/kube-score score ./config/manager/network_policy.yaml

# ==================================
# Show kubernetes version
# ==================================

kubectl version --output=yaml
-->
clientVersion:
buildDate: "2022-12-08T19:58:30Z"
compiler: gc
gitCommit: b46a3f887ca979b1a5d14fd39cb1af43e7e5d12d
gitTreeState: clean
gitVersion: v1.26.0
goVersion: go1.19.4
major: "1"
minor: "26"
platform: linux/amd64
kustomizeVersion: v4.5.7
serverVersion:
buildDate: "2022-11-09T10:31:39Z"
compiler: gc
gitCommit: eddac29feb4bb46b99fb570999324e582d761a66
gitTreeState: clean
gitVersion: v1.24.6+5658434
goVersion: go1.18.7
major: "1"
minor: "24"
platform: linux/amd64

# ==================================
# Add a new path to the .bashrc
# ==================================
/home/username/Setup/krew/kube-score

export PATH=$PATH:/home/username/Setup/krew/kube-score
echo 'export PATH=$PATH:/home/username/Setup/krew/kube-score' >> ~/.bashrc

# ====================================
# To get a list of all pods in your cluster and filter the results to only show pods with a specific label, you can use the oc get pods command with the --selector flag
# ====================================
For example, to get a list of all pods with a label named "app" and a value of "my-app", you can use the following command:
# oc get pods --selector app=my-app

This will return a list of all pods in the cluster that have the label "app" with a value of "my-app". If no pods match the selector, the command will return an empty list.

You can also use the --selector flag to filter the results by multiple labels. For example, to get a list of all pods with a label named "app" with a value of "my-app" and a label named "environment" with a value of "production", you can use the following command:

# oc get pods --selector app=my-app,environment=production
# kube-score errors
kube-score score show the following error - [CRITICAL] NetworkPolicy targets Pod · The NetworkPolicys selector doesn't match any pods but there actual pods
It sounds like you are trying to use a NetworkPolicy to control communication between pods in your cluster, but the NetworkPolicy is giving you an error saying that it does not match any pods. This could be happening for a few different

# reasons
# -------
# 1. There are no pods with the label specified in the NetworkPolicy's selector. Make sure that you have created some pods with the correct label, and that they are in the same namespace as the NetworkPolicy
# You can use the kubectl get pods --show-labels command to list all of the pods in the cluster and their labels

# 2. The syntax of the NetworkPolicy is incorrect. Make sure that the syntax of the NetworkPolicy is correct
# and that there are no typos or other mistakes in the file
# You can use the kubectl apply -f command to try and apply the NetworkPolicy, and see if it gives you any error messages that might help to identify the problem

# 3. The NetworkPolicy is in a different namespace than the pods it is trying to target
# Make sure that the NetworkPolicy is in the same namespace as the pods it is trying to target
# You can use the kubectl get networkpolicies --namespace=<namespace> command to list all of the NetworkPolicies in a particular namespace

# 4. There is a problem with the selector in the NetworkPolicy. Make sure that the selector in the NetworkPolicy is correctly specifying the pods it is trying to target
# You can use the kubectl describe pod command to see the labels of a particular pod, and compare them to the selector in the NetworkPolicy

# =============================
# network policy related errors
# =============================

# why matchExpressions is not recognized in network policy for openshift 4.11.20?

# It is possible that the matchExpressions field is not recognized in NetworkPolicy objects for OpenShift 4.11.20 because it is not a valid field for NetworkPolicy objects in that version of OpenShift

# In Kubernetes, the matchExpressions field is used in NetworkPolicy objects to specify a list of label selector expressions

# that are used to determine which pods the policy should apply to. However, the syntax and fields of NetworkPolicy # objects can vary between different versions of Kubernetes and OpenShift

# It is important to consult the documentation for the specific version of Kubernetes or OpenShift that you are using to determine which fields are valid for NetworkPolicy objects

# You can also use the oc explain command to view the # documentation for the fields of a specific resource in OpenShift. For example

# oc explain networkpolicy --recursive=true

# This will display the documentation for the fields of NetworkPolicy objects in OpenShift, including a description of each field and its usage

# oc explain networkpolicy.spec.ingress --recursive=true

# This will display the documentation for the fields of NetworkPolicy objects in a certian inner hierarchy

# ===============================
# network policy related commands
# ===============================

# 1. Apply a network policy
# oc apply -f ./config/manager/network_policy.yaml

# 2. Delete a network policy
# oc delete -f ./config/manager/network_policy.yaml

# 3. Get a printing of the network policy
# oc get networkpolicy allow-https-only-for-specific-ports-ingress -n test-service -o yaml

# 3. Describe a network policy
# oc describe networkpolicy allow-https-only-for-specific-ports-ingress -n test-service

# 4. Look for pods and labels
# kubectl get pods --show-labels -n test-service

# Get cluster network config
# ==========================
oc describe network.config/cluster

# Trying to open a bash console in a pod's container

# Trying to execute a command from within the test-service pod
# ===============================================================

# Get test-service pod
POD_NAME=$(oc get pods -n test-service | awk '{print $1}' | tail -n 1)

# Execute a command
oc exec $POD_NAME -n test-service -c manager -- ls -ltra
oc exec $POD_NAME -n test-service -c manager -- find . -name "bash"

# curl to an egress site with 15 seconds timeout

oc exec $POD_NAME -n test-service -c manager -- curl -v -m 15 www.microsoft.com

--> curl: (28) Resolving timed out after 15000 milliseconds
command terminated with exit code 28


# In OpenShift, you can get the namespace, service name, and type of services
# using the oc command-line tool or the OpenShift web console
Here are the steps to get the namespace, service name, and type of services using the oc command-line tool:
oc get services --all-namespaces -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.spec.type}{"\n"}{end}' 
command to get the namespace, service name and type of all services in your cluster across all namespaces.
You can also use oc get services --all-namespaces -o wide command which will give you more information about the services including the namespace, service name and type.

Alternatively, you can also use the OpenShift web console to get the namespace, service name and type of services:

Open the OpenShift web console and navigate to the Networking section.
Select the Services tab
You can see the namespace, service name and type of each service in the table.
Please note that, the above commands will give you the information about all services across all namespaces, if you want to limit the output to a specific namespace you can specify it with -n option, for example oc get services -n my-namespace -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.spec.type}{"\n"}{end}'

# ==============================================================================
# In OpenShift, you can get the IP address of services along with the namespace
# service name, and type using the oc command-line tool
# ==============================================================================
Here are the steps to get the IP address, namespace, service name, and type of services using the oc command-line tool:

Run
oc get services --all-namespaces -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.spec.clusterIP}{"\t"}{.spec.type}{"\n"}{end}' 
command to get the IP address, namespace, service name and type of all services in your cluster across all namespaces

# You can align the display of the IP address, namespace, service name
# and type of services in equal column widths
# by using the printf command along with the oc command-line tool

Here's an example command that uses the printf command to align the display in equal column widths:
oc get services --all-namespaces -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.spec.clusterIP}{"\t"}{.spec.type}{"\n"}{end}' | awk '{printf "%-20s %-20s %-20s %-20s\n",$1,$2,$3,$4}'

This command uses the -o jsonpath option of the oc get services command to get the information about the services, and then pipes the output to awk command. The awk command uses the printf function to align the columns with a width of 20 characters each.

You can adjust the width of the columns as per your requirement.
#
# I meant to consider the column width per the longest value in all the rows in the same column
#

You can use the awk command to align the display of the IP address, namespace, service name, and type of services in columns with widths that are equal to the longest value per column among all the rows in the same column.

Here's an example command that uses the awk command to align the display in columns with widths that are equal to the longest value per column among all the rows in the same column:

# Another approach to align the columns in equal widths to the longest value per column among all the rows in the same column is by using the column command
# This command is a Unix command-line tool to align text in columns. Here's an example command that uses column command to align the display

# in columns with # widths that are equal to the longest value per column among all the rows in the same column
oc get services --all-namespaces -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{.spec.clusterIP}{"\t"}{.spec.type}{"\n"}{end}' | column -t -s $'\t'

This command uses the -o jsonpath option of the oc get services command to get the information about the services, and then pipes the output to column command.
The -t option tells column command to format the input as a table, and the -s option is used to specify the separator which is \t in this case.

# To access a service in a specific namespace in OpenShift, you need to know the service's IP address and port, and then you can use the curl command or a web browser to send a request to the service
Here's an example of how to use the curl command to access a service:
curl <http://<service-ip>:<service-port>>

# --> You can get the service's IP address and port by using the oc get services command along with the -n option to specify the namespace, for example
oc get services -n test-service -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.clusterIP}{"\t"}{.spec.ports[0].name}{"\t"}{.spec.ports[0].port}{"\t"}{.spec.type}{"\n"}{end}' | column -t -s $'\t'

--> This command will give you the services name, IP address, port name and port number in the test-service namespace.

Alternatively, you can use the OpenShift web console to access the service, you need to go to the Networking section, select the Services tab and then select the service that you want to access.

If the service is running inside the cluster and you want to access it from outside the cluster, you need to create a route for the service and expose it to the outside world. In OpenShift you can use oc expose command or from the web console you can create a route for the service with type NodePort or LoadBalancer then you can access it with the IP address of the node or the LoadBalancer and the service's port.

            "metadata": {

oc get services -n test-service -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.clusterIP}{"\t"}{.spec.ports[0].name}{"\t"}{.spec.ports[0].port}{"\t"}{.spec.type}{"\t"}

{metadata.annotations.service.alpha.openshift.io/serving-cert-signed-by}{"\t"}{metadata.annotations.service.beta.openshift.io/serving-cert-secret-name}{"\n"}{"\t"}{metadata.annotations.service.alpha.openshift.io/serving-cert-signed-by}{end}' | column -t -s $'\t'

--> This command will give you the services name, IP address, port name, port number and service type in the test-service namespace.
# Secrets related info

# secret types
# ? # What is the difference between these secret types

kubernetes.io/dockercfg and kubernetes.io/service-account-token?
# A # kubernetes.io/dockercfg and kubernetes.io/service-account-token are two different types of secrets in Kubernetes

kubernetes.io/dockercfg secrets are used to authenticate with a private Docker registry.
These secrets contain a .dockercfg file which contains the authentication information required to pull images from a private registry.

kubernetes.io/service-account-token secrets are used to authenticate pods and service accounts within the Kubernetes cluster. These secrets contain a token that is used to authenticate with the Kubernetes API.

In summary, kubernetes.io/dockercfg secrets are used to authenticate with a private Docker registry to pull images, while kubernetes.io/service-account-token secrets are used to authenticate pods and service accounts within the Kubernetes cluster to access the Kubernetes API.

##

# ? # Which type of secret uses a certificate?
# A # In Kubernetes, secrets of type kubernetes.io/tls are used to store a certificate and its associated private key

      This type of secret is typically used to secure communication between pods and other Entity2 within the cluster,
      Such as securing communication between pods using Transport Layer Security (TLS).

      The secret holds the x509 certificate in PEM format and it's key in the format you've specified when you created the secret.

      Here's an example of how you can create a secret of type kubernetes.io/tls:
      ==========================================================================
      oc create secret tls mysecret --cert=path/to/cert.pem --key=path/to/key.pem

      This command creates a secret named 'mysecret' of type 'kubernetes.io/tls' and stores the certificate and key in the secret.
      The '--cert' and '--key' options specify the paths to the certificate and key files, respectively.

      Please note that you have to have the certificate and key file ready in your local system before creating the secret.

# DOCKER HUB
<https://hub.docker.com/>

DOCKER_CONFIG_JSON is an environment variable used by Docker to configure the Docker client. It is used to specify the location of the Docker client configuration file, which is usually located at ~/.docker/config.json. The file contains information about Docker client settings such as the default registry to use for images and authentication information for accessing private registries.

GitHub, on the other hand, is a web-based platform for version control and collaboration that uses Git as its version control system. It is not directly related to the DOCKER_CONFIG_JSON environment variable. However, if you are using GitHub as a source code repository and Docker to build and run your application, you may use the DOCKER_CONFIG_JSON environment variable to specify the location of the Docker client configuration file, which can contain information needed to authenticate with your private registries.

In other words, DOCKER_CONFIG_JSON is used to configure the Docker client, and it is not directly related to GitHub. However, if you use both Docker and GitHub in your workflow, the DOCKER_CONFIG_JSON variable may be used to authenticate with private registries, which could include a private registry hosted on GitHub.

export DOCKER_CONFIG_JSON=~/.docker/config.json

# get cluster events
oc get events -n default --sort-by='.metadata.creationTimestamp' -o custom-columns=TIME:.metadata.creationTimestamp,TYPE:.type,REASON:.reason,OBJECT:.involvedObject.name,MESSAGE:.message


# Update golang version to 1.19.6
curl -LO https://go.dev/dl/go1.21.4.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.21.4.linux-amd64.tar.gz
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
source ~/.bashrc

# Update golang version to 1.20.4
curl -LO https://go.dev/dl/go1.20.4.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.20.4.linux-amd64.tar.gz

# local can be used inside a function
local -xzf go1.20.4.linux-amd64.tar.gz
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
source ~/.bashrc

# Another type of installation
sudo rm -rf ~/go
curl -LSO https://go.dev/dl/go1.20.4.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.20.4.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
go version

# VSCode addition
Add "go.goroot": "/usr/local/go" into VSCode settings.json

# rollout the test-service deployment
oc scale deployment/test-manager --replicas=0 -n test-service

# Wait for the replicas to terminate and then scale up again with:
oc rollout status deployment/test-manager -n test-service

# scale up again with
oc scale deployment/test-manager --replicas=1 -n test-service

## the same for grafana service deployment

# get the deployments, use the manager one

oc get deployment -n test-grafana

oc scale deployment/grafana-operator-controller-manager --replicas=0 -n test-grafana
oc rollout status deployment/grafana-operator-controller-manager -n test-grafana
oc scale deployment/grafana-operator-controller-manager --replicas=1 -n test-grafana

# describe deployment
oc describe deployment/grafana-deployment -n test-grafana


# print all failed pipelineruns logs in tenant namespaces
kubectl get namespaces --no-headers | awk '/tenant/ {print $1}' | xargs -I {} sh -c 'if [ $(kubectl get pipelinerun -n {} --no-headers 2>/dev/null | wc -l) -gt 0 ]; then echo "{}"; fi' | xargs -I {} sh -c 'kubectl get pipelinerun -n {} --no-headers | awk "/Failed/ {print \$1, \"-n\", \"{}\"}"' | xargs -I {} sh -c 'echo "PipelineRun: {}"; kubectl logs -n $(echo {} | awk "{print \$3}") $(kubectl get pods -n $(echo {} | awk "{print \$3}") --selector=tekton.dev/pipelineRun=$(echo {} | awk "{print \$1}") -o jsonpath="{.items[0].metadata.name}") --all-containers; echo ""'

# print all the tenant namespaces failing pipelineruns and for each print it's failed Taskrun name
kubectl get pipelinerun --all-namespaces --no-headers | awk '/Failed/ {print $1, $2, $3}' | xargs -I {} sh -c 'echo "PipelineRun: {}"; kubectl get taskrun -n $(echo {} | awk "{print \$1}") --selector=tekton.dev/pipelineRun=$(echo {} | awk "{print \$2}") -o jsonpath="{range .items[*]}{.metadata.name}{\": \"}{.status.conditions[0].status}{\"\n\"}{end}" | awk "/False/ {print \"TaskRun: \"\$1}"'

# Show the show-summery taskrun logs
tkn taskrun logs devfile-sample-code-with-quarkus-123abc-show-summary -n loadx-0123-tenant

# Same with filterring for Error
tkn taskrun logs devfile-sample-code-with-quarkus-123abc-show-summary -n loadx-0123-tenant | grep -i error -B 3 -A 3

# show the task1-name taskrun logs
tkn taskrun logs devfile-sample-code-with-quarkus-123abc-task1-name -n loadx-0123-tenant

# Same with filterring for Error
tkn taskrun logs devfile-sample-code-with-quarkus-123abc-task1-name -n loadx-0123-tenant | grep -i error -B 3 -A 3

#
# GO best practices
#

# Every sometime we need to do the following per working repo

# Clear GO modules cache in the disk

go clean --modcache

# Updates GO modules in disk

go mod vendor

#

go mod tidy

# ======================================
# PromQL queries
# ======================================

# Get a list of all available metrics
count({__name__=~".+"}) by (__name__)

# Statistics per a metric

# overall statistics
avg(example_metric)
max(example_metric)
min(example_metric)
sum(example_metric)
stddev(example_metric)
quantile(0.95, example_metric)


# statistics 
avg_over_time(example_metric[5m])
max_over_time(example_metric[1h])
min_over_time(example_metric[30m])
sum_over_time(example_metric[10m])
stddev_over_time(example_metric[15m])
quantile_over_time(0.95, example_metric[5m])

avg_over_time(example_metric[1d])
max_over_time(example_metric[1d])
min_over_time(example_metric[1d])
sum_over_time(example_metric[1d])

avg_over_time(example_metric[1w])
max_over_time(example_metric[1w])
min_over_time(example_metric[1w])
sum_over_time(example_metric[1w])

avg_over_time(example_metric[1d] offset 1d)  // Average for 1 day ago
avg_over_time(example_metric[1d] offset 2d)  // Average for 2 days ago
avg_over_time(example_metric[1d] offset 7d)  // Average for 7 days ago

Let's use an example metric - actual_creation_time_metric
avg_over_time(actual_creation_time_metric[5m])
max_over_time(actual_creation_time_metric[1h])
min_over_time(actual_creation_time_metric[30m])
sum_over_time(actual_creation_time_metric[10m])

quantile_over_time(0.5, actual_creation_time_metric[5m])
quantile_over_time(0.95, actual_creation_time_metric[5m])

avg_over_time(actual_creation_time_metric[1w])
max_over_time(actual_creation_time_metric[1w])
min_over_time(actual_creation_time_metric[1w])

avg_over_time(actual_creation_time_metric[1d] offset 7d)  // Average for 7 days ago

avg(actual_creation_time_metric)
max(actual_creation_time_metric)
min(actual_creation_time_metric)
quantile(0.95, actual_creation_time_metric)
quantile(0.5, actual_creation_time_metric) // median


# Total cluster CPU average usage per 2 minutes
sum(
1 - sum without (mode) (rate(node_cpu_seconds_total{mode=~"idle|iowait|steal"}[2m]))
_
on(instance) group_left() (
label_replace(avg by (node) (kube_node_role{role=~".+"}), "instance", "$1", "node","(._)")
)
)

# Total cluster CPU maximum usage per 2 minutes
sum(
1 - sum without (mode) (rate(node_cpu_seconds_total{mode=~"idle|iowait|steal"}[2m]))
_
on(instance) group_left() (
label_replace(max by (node) (kube_node_role{role=~".+"}), "instance", "$1", "node","(._)")
)
)

# Total cluster Memory average usage per 2 minutes

# Total cluster Memory usage v1
(sum(node_memory_MemTotal_bytes) - sum(node_memory_MemAvailable_bytes)) / 1024 / 1024 / 1024

# Total memory usage per each node
(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / 1024 / 1024 / 1024


## scripts
# deleteQuayRobots
python ./deleteQuayRobots.py $QUAY_TOKEN nafta_org "load"  
python ./deleteQuayRobots.py $QUAY_TOKEN nafta_org "nafta_org+load"  
python ./deleteQuayRobots.py $QUAY_OAUTH_TOKEN nafta_org "nafta_org+load"



# Query JIRA (example)
(reporter = currentUser() or assignee = currentUser()) and (project = project_name)  and (description ~ "*description*" OR summary ~ "*description*") ORDER BY created DESC



# Wait for Openshift Entity2 to be created/deleted/updated on all namespaces
oc get customresource --watch -A -o wide

# store the output into an output file, disregard errors
oc get customresource --watch -A -o wide > customresource.txt 2>/dev/null &

# Also allow killing the processes

oc get ns --watch -A -o wide > namespace_output.txt 2>/dev/null &
export NS_PID=$!
echo "Process ID for Namespace: $NS_PID"
echo "To kill: kill $NS_PID"

#
# Prometheus
#

# Get available metrics
# prometheus-k8s route
https://prometheus-prometheus-k8s-route/api
curl https://prometheus-prometheus-k8s-route:9090/api/v1/label/__name__/values

# PR search - search for PRs
is:pr author:username is:open label:bug


# Horreum
# AggregatedTimeAvg combination function

value => {
// Extract individual average times from the value object
const createEntity1TimeAvg = value.createEntity1TimeAvg;
const createEntity2TimeAvg = value.createEntity2TimeAvg
const createEntity3TimeAvg = value.createEntity3TimeAvg;

// Create an array of the average times
const averageTimes = [
createEntity1TimeAvg,
createEntity2TimeAvg,
createEntity3TimeAvg
];

// Filter out any undefined or null values
const filteredAverageTimes = averageTimes.filter(time => time !== undefined && time !== null);

// Check if the array is empty
if (filteredAverageTimes.length === 0) {
return 'N/A';
}

// Calculate the sum of the average times
const sum = filteredAverageTimes.reduce((acc, curr) => acc + curr, 0);

// Calculate and return the overall average time
return (sum / filteredAverageTimes.length).toFixed(2);
}



## Calculate clocks time skew between the loadtests running machine and the openshift cluster used

# Get the time from the machine running the test
date +"%Y-%m-%dT%H:%M:%S%z"

## Bash script debug
# Print commands and their output:
steps:

- name: Run script
  run: |
  set -e
  set -x
  ./your-script.sh
  shell: bash

# Add error handling in the script
#!/bin/bash
set -e
trap 'catch $? $LINENO' EXIT

catch() {
echo "Error $1 occurred on $2"
}

# Your script's commands here
echo "Script executed successfully"


## JSONPath
# This function will return the numeric value itself if it's not null or undefined, and 0 otherwise
value => {
  return value ?? 0;
}



# multi component repo example
https://github.com/maysunfaisal/multi-components-dockerfile

# multi arch repo example
https://github.com/spork-madness/multi-platform-test



## another command to extract GITHUB repo commit list sorted desc by date
curl -H "Accept: application/vnd.github.v3+json" \                                                                                                                                                                                                                ─╯
"https://api.github.com/repos/organization-name/project-name/pulls/pr-number/commits"  | jq '[.[] | {sha: .sha, date: .commit.committer.date}] | sort_by(.date) | reverse'


## JQ - traverse and print field hierarical names and values     
jq --raw-output '
  paths(scalars) as $p | 
  {path: $p | map(tostring) | join("."), value: getpath($p)} | 
  "\(.path): \(.value)"
' test.json


## JQ - print field names values with header containing the field names
cat test.json | jq --raw-output '
["field1", "field2", 
"field3", "field4", "field5", 
"field6"], 
[
    .field1,
    .field2,
    .field3,
    .field4,
    .field5,
    .field6
] | @csv'


## get all the recordsets in a ZoneID=Z0123456789 like the below (in AWS)
aws route53 list-resource-record-sets --hosted-zone-id /hostedzone/Z0123456789 > prev-dns-records.json

## JQ - convert a json containing AWS DNS records from a Zone into a json ready for batch deletion
jq '{ChangeBatch: {Changes: [.ResourceRecordSets[] | {Action: "DELETE", ResourceRecordSet: .}]}}' input.json > output.json


## JQ - convert a json containing AWS DNS records from a Zone for DNS names related to servers named like: "server-\\d{2}" into a json ready for batch deletion
jq '{Comment: "Batch delete of records", Changes: [.ResourceRecordSets[] | select(.Name | test("server-\\d{2}")) | {Action: "DELETE", ResourceRecordSet: .}]}' prev-dns-records.json > delete-dns-records.json


## Count the number of DNS records in the output.json file
jq '.Changes | length' delete-dns-records.json 

## actually delete the DNS records of the "ChangeBatch" records in delete-d.json 
aws route53 change-resource-record-sets --hosted-zone-id /hostedzone/Z0123456789 --change-batch file://delete-dns-records.json

receiving a dispaly like the below:
{
    "ChangeInfo": {
        "Id": "/change/C123456789",
        "Status": "PENDING",
        "SubmittedAt": "2023-04-12T13:11:09.470000+00:00",
        "Comment": "Batch delete of records"
    }
}

## To check the current status of your change request, you can use the following AWS CLI command, 
aws route53 get-change --id C123456789

seeing "Status": "INSYNC" is the goal when you're making DNS changes in AWS Route 53, as it means your changes have been fully applied.


## To transform the structure by changing the "Action" from "DELETE" to "UPSERT" for each record (create the DNS records in another zone)
jq '.Comment = "Batch UPSERT of records" | .Changes[] |= (.Action = "UPSERT")' delete-dns-records.json > upsert-dns-records.json

## To transform the structure by changing the "Action" from "DELETE" to "UPSERT" and update subdomain from subdomain1 to subdomain2 for each record (create the DNS records in another zone)
jq '.Comment = "Batch UPSERT of records" | .Changes[].ResourceRecordSet.Name |= gsub("subdomain1"; "subdomain2") | .Changes[] |= (.Action = "UPSERT")' delete-dns-records.json > upsert-dns-records.json

## actually upsert the DNS records of the "ChangeBatch" records in upsert-dns-records.json into the new zoneID Z02456789789
aws route53 change-resource-record-sets --hosted-zone-id /hostedzone/Z02456789789 --change-batch file://upsert-dns-records.json




## Misc procedures
# caching issues related to golangci tools
for id in $(gh cache list | grep golangci | awk '{print $1}'); do gh cache delete  $id; done



### installation in Fedora
Update and exclude google-chrome-stable
sudo dnf update --exclude=google-chrome-stable



## User's test-user PRs in a repo test-repo in organization test-org
https://github.com/search?q=repo%3Atest-org%2Ftest-repo++from%3A+test-user&type=pullrequests&p=4


