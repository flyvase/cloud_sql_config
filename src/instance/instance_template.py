import env_variables


def generate_config(context):
    imports = [{"path": "env_variables.py"}]
    variables = env_variables.get_variables(context.properties["environment"])
    resources = [
        {
            "name": "mr_president_instance",
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
                "name": "mr-president2",
                "region": "asia-northeast1",
                "rootPassword": context.properties["rootPassword"],
            },
        }
    ]
    outputs = [
        {"name": "createdInstanceId", "value": "$(ref.mr_president_instance.name)"}
    ]

    return {"imports": imports, "resources": resources, "outputs": outputs}
