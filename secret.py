from google.cloud import secretmanager


def get_secret_text(project_id, secret_name, secret_ver):
    client = secretmanager.SecretManagerServiceClient()
    name = client.secret_version_path(project_id, secret_name, secret_ver)
    response = client.access_secret_version(name=name)

    return response.payload.data.decode("UTF-8")
