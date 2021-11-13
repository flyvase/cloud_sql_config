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

### add database password to secret manager

You should generate strong random password on generator first.

```zsh
printf "YOUR_PASSWORD" | gcloud secrets create "mr_president_root_password" --data-file=- --project $PROJECT_ID
```

## deploy resources to local env

```zsh
gcloud deployment-manager deployments create mr-president \
--template src/cloud_sql_template.py \
--properties \
"rootPassword:'$(gcloud secrets versions access latest --secret=mr_president_root_password --project $PROJECT_ID)'" \
--automatic-rollback-on-error \
--project $PROJECT_ID
```
