import json
import os
from dotenv import load_dotenv


def load_environment():
    # 1. Determine the active environment (defaults to 'development')
    env = os.getenv("APP_ENV", "development").lower()

    if env == "production":
        # Fetch from AWS Secrets Manager on EC2
        import boto3

        secret_name = os.getenv("AWS_SECRET_NAME", "prod/db_engine/credentials")
        region_name = os.getenv("AWS_REGION", "us-east-1")

        client = boto3.client("secretsmanager", region_name=region_name)
        response = client.get_secret_value(SecretId=secret_name)
        secrets = json.loads(response["SecretString"])

        # Map secrets directly into os.environ
        for key, val in secrets.items():
            os.environ[key] = str(val)

    else:
        # Load local .env file when developing locally in PyCharm
        load_dotenv(override=True)