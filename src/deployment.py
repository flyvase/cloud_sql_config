import env_variables


def generate_config(context):
    imports = [
        {"path": "env_variables.py"},
    ]
    variables = env_variables.get_variables(context.properties["environment"])
    resources = [
        {
            "name": "cloud_sql_main_instance",
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
                "name": "main-instance",
                "region": "asia-northeast1",
                "rootPassword": context.properties["rootUserPassword"],
            },
        },
        {
            "name": "cloud_sql_main_database",
            "type": "sqladmin.v1beta4.database",
            "properties": {
                "instance": "$(ref.cloud_sql_main_instance.name)",
                "charset": "utf8mb4",
                "collation": "utf8mb4_bin",
                "name": "main_database",
            },
        },
        {
            "name": "cloud_sql_user_api_server",
            "type": "sqladmin.v1beta4.user",
            "properties": {
                "instance": "$(ref.cloud_sql_main_instance.name)",
                "name": "api_server",
                "password": context.properties["apiServerUserPassword"],
            },
            "metadata": {"dependsOn": ["cloud_sql_main_database"]},
        },
    ]

    return {"imports": imports, "resources": resources}
