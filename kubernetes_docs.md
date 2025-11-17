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


# Create Docker Build
docker build -t k8s-fast-api .

# Run the Docker Container
docker run -p 5000:5000 k8s-fast-api

# Docker Login 
- Login to Docker Hub
- Create Repository
- Copy the docker push command tag name

# Build using Tag Name
docker build -t himanshud05/k8s-getting-started:0.0.1 .

# Docker Push Commands
docker push himanshud05/k8s-getting-started:0.0.1

Till now we have created the super simple api we bundled it up as a container image and we pushed it
to the registry and now we will create cluster to deploy it.

# Kubernetes Deployment
kubectl apply -f kubernetes/deployment.yaml

kubectl get deployments

Once the deployment is successful, you need to expose it as a service to access it. You can do this with the following command, which will create a service of type LoadBalancer:

kubectl expose deployment my-flask-app-deployment --type=LoadBalancer --port=80 --target-port=5000
kubectl delete service my-flask-app-deployment

docker build -t himanshud05/consumer:latest -f src/Consumer/Dockerfile .
docker push himanshud05/consumer:latest

docker build -t himanshud05/producer:latest -f src/KafkaFiles/Dockerfile .
docker push himanshud05/producer:latest

docker build -t himanshud05/frontend:latest -f src/web/Dockerfile .
docker push himanshud05/frontend:latest

kubectl apply -f k8s/zookeeper.yaml
kubectl apply -f k8s/kafka.yaml
kubectl apply -f k8s/redis.yaml
kubectl apply -f k8s/producer.yaml
kubectl apply -f k8s/consumer.yaml
kubectl apply -f k8s/frontend.yaml

kubectl logs producer-deployment-596754b77f-r82rl
kubectl logs frontend-deployment-5b89d7f777-d5cr9
kubectl logs consumer-deployment-57bd4bf457-4lxrh

kubectl delete service consumer-service frontend-service kafka-service kubernetes redis-service zookeeper-service

kubectl delete deployment consumer-deployment frontend-deployment kafka-deployment my-flask-app-deployment producer-deployment redis-deployment zookeeper-deployment
