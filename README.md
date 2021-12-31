# Cloud SQL config

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
Do not include `-`, `*`, `!`, `#`, `%`, `~`, `|`, `$` and `&` to your password (due to limitations of yaml and printf command)

```zsh
printf "YOUR_PASSWORD" | gcloud secrets create "cloud_sql_root_user_password" --data-file=- --project $PROJECT_ID
printf "YOUR_PASSWORD" | gcloud secrets create "cloud_sql_api_server_user_password" --data-file=- --project $PROJECT_ID
```

## deploy resources on local env

```zsh
export ROOT_USER_PASSWORD=$(gcloud secrets versions access latest --secret=cloud_sql_root_user_password --project $PROJECT_ID) \
export API_SERVER_USER_PASSWORD=$(gcloud secrets versions access latest --secret=cloud_sql_api_server_user_password --project $PROJECT_ID)
```

```zsh
gcloud deployment-manager deployments create cloud-sql \
--template src/deployment.py \
--properties \
"rootUserPassword:'$ROOT_USER_PASSWORD',apiServerUserPassword:'$API_SERVER_USER_PASSWORD'" \
--automatic-rollback-on-error \
--project $PROJECT_ID
```

## update resources on local env

```zsh
gcloud deployment-manager deployments update cloud-sql \
--template src/deployment.py \
--properties \
"rootUserPassword:'$ROOT_USER_PASSWORD',apiServerUserPassword:'$API_SERVER_USER_PASSWORD'" \
--project $PROJECT_ID
```
