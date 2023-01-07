#!/usr/bin/env bash

kubectl delete namespace rasa-x
kubectl create namespace rasa-x  

kubectl delete namespace rasa
kubectl create namespace rasa

# helm repo add rasa-x https://rasahq.github.io/rasa-x-helm 
helm repo add rasa https://helm.rasa.com

# helm install --generate-name \
#     --namespace rasa-x \
#     --values secret/rasa-values.yml \
#     rasa-x/rasa-x

echo "Waiting for rasa-x"

# kubectl --namespace rasa-x \
#     wait \
#     --for=condition=available \
#     --timeout=20m \
#     --selector app.kubernetes.io/component=rasa-x \
#     deployment


echo "Rasa-x deployed"


kubectl --namespace rasa-x get services


echo "Deploying Rasa Opensource"

helm install  --generate-name \
   --namespace rasa-x \
   --values secret/rasa-values.yml \
   rasa/rasa


echo "Rasa-opensource deployed"
