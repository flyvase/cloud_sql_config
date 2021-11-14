def get_variables(env):
    if env == "dev" or env == "stg":
        return {
            "instanceType": "db-custom-1-3840",
            "availabilityType": "ZONAL",
            "enableBackup": False,
            "enableBinaryLog": False,
            "diskSize": 10,
        }
    elif env == "prod":
        return {
            "instanceType": "db-custom-1-3840",
            "availabilityType": "ZONAL",
            "enableBackup": True,
            "enableBinaryLog": True,
            "diskSize": 10,
        }
