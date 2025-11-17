# Kubernetes

## Build and push your Docker image:
    docker build -t himanshud05/consumer:latest -f src/consumer/Dockerfile .
    docker push himanshud05/consumer:latest

## To check status of Kubernetes cluster please run below command
    kubectl cluster-info

## Steps to Enable Kubernetes in Docker
1. Open Docker Desktop.
2. Go to Settings (the gear icon in the top right).
3. Select the Kubernetes tab.
4. Make sure the Enable Kubernetes checkbox is ticked. If it's not, check it and click Apply & Restart. This will take a few minutes to start the cluster.
5. If it is already enabled, try disabling it, apply, and then re-enabling it

## To verify that the cluster is running run following command 
    kubectl get nodes

## If it returns a node with a Ready status you can then go ahead and apply your configuration
    kubectl apply -f k8s/consumer.yaml

## Verify pod and service are running:
    kubectl get pods
    kubectl get svc consumer-service

## Access consumer logs for troubleshooting:
    kubectl logs -l app=consumer
