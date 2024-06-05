def get_postgres_connection():
    host = "db"
    port = 5432
    database = "grocery"
    username = "postgres"
    password = "password"
    return f"postgresql://{username}:{password}@{host}:{port}/{database}"