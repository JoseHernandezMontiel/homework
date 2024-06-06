import os

def get_postgres_uri():
    host = "localhost"
    port = 5432
    password = "abc123"
    user = "postgres"
    return f"postgresql://{user}:{password}@{host}:{port}"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"