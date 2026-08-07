import requests
from dataclasses import dataclass

from data_forge.context.context import Context


@dataclass(frozen=True)
class Auth:
    context: Context

    def get_token(self):
        post_kwargs = {
            "url": f"{self.context.base_url}/services/oauth2/token",
            "data": {
                "client_id": self.context.client_id,
                "client_secret": self.context.client_secret,
                "grant_type": self.context.grant_type,
            }
        }

        sec_response = requests.post(**post_kwargs)
        sec_response.raise_for_status()

        token_data = sec_response.json()
        return token_data["access_token"]
