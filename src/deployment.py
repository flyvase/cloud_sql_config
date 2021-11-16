import env_variables


def generate_config(context):
    imports = [
        {"path": "env_variables.py"},
    ]
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
                "name": "mr-president13",
                "region": "asia-northeast1",
                "rootPassword": context.properties["rootPassword"],
            },
        },
        {
            "name": "mr_president_database",
            "type": "sqladmin.v1beta4.database",
            "properties": {
                "instance": "$(ref.mr_president_instance.name)",
                "charset": "utf8mb4",
                "name": "mr_president",
            },
        },
        {
            "name": "mr_president_user_harvest",
            "type": "sqladmin.v1beta4.user",
            "properties": {
                "instance": "$(ref.mr_president_instance.name)",
                "name": "harvest",
                "password": context.properties["harvestPassword"],
            },
            "metadata": {"dependsOn": ["mr_president_database"]},
        },
    ]

    return {"imports": imports, "resources": resources}
