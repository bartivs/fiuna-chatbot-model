#!/usr/bin/env bash

kubectl delete namespace rasa-x
kubectl create namespace rasa-x  

helm repo add rasa-x https://rasahq.github.io/rasa-x-helm 

helm install generate-name \
    --namespace rasa-x \
    --values secret/rasa-x-values.yml \
    rasa-x/rasa-x

echo "Waiting for rasa-x"

kubectl --namespace rasa-x \
    wait \
    --for=condition=available \
    --timeout=20m \
    --selector app.kubernetes.io/component=rasa-x \
    deployment


echo "Rasa-x intalled"


kubectl --namespace rasa-x get services

