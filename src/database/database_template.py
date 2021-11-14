def generate_config(context):
    resources = [
        {
            "name": "mr_president_database",
            "type": "sqladmin.v1beta4.database",
            "properties": {
                "instance": context.properties["instanceId"],
                "charset": "utf8mb4",
                "name": "mr_president",
            },
        }
    ]

    return {"resources": resources}
