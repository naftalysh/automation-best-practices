# TEKTON Bundle

Web link: <https://vinamra-jain.medium.com/publishing-tekton-resources-as-bundles-on-oci-registry-c4644d2af83f>

0. Tekton bundle help
   tkn bundle --help

1. List contents of a bundle
   tkn bundle list quay.io/organization_name/repository_name:tag_name

2. Extract contents of a task within the Bundle
   tkn bundle list quay.io/organization_name/repository_name:tag_name task test_task -o yaml

3. Extract contents of a pipeline within the Bundle
   tkn bundle list quay.io/organization_name/repository_name:tag_name pipeline pipeline_name -o yaml

4. And if you want to install the Task on cluster then you can just pipe it with kubectl :
   tkn bundle list quay.io/organization_name/repository_name:tag_name task test_task -o yaml | kubectl create -f -
   --> task.tekton.dev/test_task created

5. Publish a new Tekton Bundle to a registry by passing in a set of Tekton objects via files, arguments or standard in:
   - tkn bundle push docker.io/myorg/mybundle:latest "apiVersion: tekton.dev/v1beta1 kind: Pipeline..."
   - tkn bundle push docker.io/myorg/mybundle:1.0 -f path/to/my/file.json
   - cat path/to/my/unified_yaml_file.yaml | tkn bundle push myprivateregistry.com/myorg/mybundle -f -

