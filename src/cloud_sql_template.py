def generate_config(context):
    imports = [
        {"path": "instance/instance_template.py", "name": "instance_template.py"},
        {"path": "database/database_template.py", "name": "database_template.py"},
    ]
    resources = [
        {
            "name": "mr_president_instance",
            "type": "instance_template.py",
            "properties": {
                "environment": context.properties["environment"],
                "rootPassword": context.properties["rootPassword"],
            },
        },
        {
            "name": "mr_president_database",
            "type": "database_template.py",
            "properties": {
                "instanceId": "$(ref.mr_president_instance.createdInstanceId)"
            },
        },
    ]

    return {"imports": imports, "resources": resources}
