# Mr.president

This repository stores the [cloud deployment manager](https://cloud.google.com/?hl=ja) configuration of databases for Flyvase.

## prerequisites

### set project id

```zsh
export PROJECT_ID=<your project id>
```

### enable required apis

```zsh
gcloud services enable \
sqladmin.googleapis.com \
compute.googleapis.com \
secretmanager.googleapis.com \
--project $PROJECT_ID
```

### add passwords to secret manager

Generate the random password (min length 12) and use the command below to deploy to secret manager.
Do not include `-`, `*`, `!`, `#`, `%`, `~`, `|`, `$` and `&` to your password (due to syntax of yaml and printf command)

```zsh
printf "YOUR_PASSWORD" | gcloud secrets create "mr_president_root_password" --data-file=- --project $PROJECT_ID
printf "YOUR_PASSWORD" | gcloud secrets create "mr_president_harvest_password" --data-file=- --project $PROJECT_ID
```

## deploy resources on local env

```zsh
export ROOT_PASSWORD=$(gcloud secrets versions access latest --secret=mr_president_root_password --project $PROJECT_ID) \
export HARVEST_PASSWORD=$(gcloud secrets versions access latest --secret=mr_president_harvest_password --project $PROJECT_ID)
```

```zsh
gcloud deployment-manager deployments create mr-president \
--template src/deployment.py \
--properties \
"rootPassword:'$ROOT_PASSWORD',harvestPassword:'$HARVEST_PASSWORD'" \
--automatic-rollback-on-error \
--project $PROJECT_ID
```

## update resources on local env

```zsh
gcloud deployment-manager deployments update mr-president \
--template src/deployment.py \
--properties \
"rootPassword:'$ROOT_PASSWORD',harvestPassword:'$HARVEST_PASSWORD'" \
--project $PROJECT_ID
```
