import os
os.environ["APP_NAME"] = "pytest"


def get_app_name():
    return os.environ.get("APP_NAME")
