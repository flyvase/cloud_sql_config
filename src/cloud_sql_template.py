import env_variables

# see https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance for properties
def generate_config(context):
    imports = [{"path": "env_variables.py"}]
    variables = env_variables.get_env_variables(context.properties["environment"])
    resources = [
        {
            "name": "mr_president",
            "type": "sqladmin.v1beta4.instance",
            "properties": {
                "databaseVersion": "MYSQL_8_0",
                "settings": {
                    "tier": variables["instanceType"],
                    "availabilityType": variables["availabilityType"],
                    "backupConfiguration": {
                        "enabled": variables["enableBackup"],
                        "binaryLogEnabled": variables["enableBackup"]
                        and variables["enableBinaryLog"],
                        "location": "asia-northeast1",
                    },
                    "dataDiskSizeGb": variables["diskSize"],
                },
                "name": "mr-president1",
                "region": "asia-northeast1",
                "rootPassword": context.properties["rootPassword"],
            },
        },
    ]

    return {"imports": imports, "resources": resources}
