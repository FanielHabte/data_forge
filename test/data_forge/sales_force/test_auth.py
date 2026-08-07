from pathlib import Path

from data_forge.sales_force.auth import Auth
from data_forge.context.context import Context
from unittest.mock import patch


@patch("data_forge.sales_force.auth.requests.post")
def test_auth(mock_post):
    config_path = Path(__file__).resolve().parent.parent.parent / "resources/manifest/valid_manifest.json"

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "access_token": "test_access_token",
        "expires_in": 36000
    }

    auth = Auth(context=Context.load_context_from(file_path=config_path))
    token = auth.get_token()

    assert token == "test_access_token"
    mock_post.assert_called_once()
