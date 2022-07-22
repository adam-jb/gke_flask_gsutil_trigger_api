# Run gsutil commands on flask, triggered by API call




### To deploy in Cloud Shell, where 'volatility-portfolio-bot' is my project ID
```
git clone https://github.com/adam-jb//gke_flask_gsutil_trigger_api.git
cd gke_flask_gsutil_trigger_api

# get ID of current GCP project
PROJECT_ID=$(gcloud config get-value project) 

# set default location to store repo
gcloud config set artifacts/location europe-west2


# making artifact repo
gcloud artifacts repositories create gke-flask-example \
    --repository-format=docker \
    --project=$PROJECT_ID \
    --description="docker repository"


# building image
 gcloud builds submit \
    --tag europe-west2-docker.pkg.dev/$PROJECT_ID/gke-flask-example/gke_flask_example .


# make GKE cluster using manual number of modes, instead of 'autopilot' which autoscales
gcloud container clusters create gke-flask-example \
    --num-nodes 2 \
    --zone europe-west2-b


# deploy resource to cluster
kubectl apply -f deployment.yaml

# monitor how deployment is going
kubectl get deployments

# another way to see how its going is looking at the status of pods:
kubectl get pods


# to update a given deployment just reapply the yaml file
kubectl apply -f deployment.yaml


# deploy service resource
kubectl apply -f service.yaml


# view status of service and IP addresses it provides
kubectl get services


```




### To delete cluster and image
```
gcloud container clusters delete gke-flask-example --region=europe-west2-b --quiet

gcloud artifacts docker images delete \
    europe-west2-docker.pkg.dev/$PROJECT_ID/gke-flask-example/gke_flask_example

```






# gke_flask_gsutil_trigger_api
