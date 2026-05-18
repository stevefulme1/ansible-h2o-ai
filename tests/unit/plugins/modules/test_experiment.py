"""Unit tests for stevefulme1.h2o_ai.experiment module."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from unittest.mock import MagicMock, patch


MODULE_PATH = "ansible_collections.stevefulme1.h2o_ai.plugins.modules.experiment"
CLIENT_PATH = "ansible_collections.stevefulme1.h2o_ai.plugins.module_utils.api_client"


def _build_experiment(**kwargs):
    """Return a mock experiment dict."""
    defaults = {"id": "test-id", "name": "test-experiment"}
    defaults.update(kwargs)
    return defaults


class TestCreate:
    """Test experiment creation."""

    @patch(f"{CLIENT_PATH}.requests")
    def test_create_experiment(self, mock_requests, module_args):
        """Creating a experiment sends POST request."""
        mock_response = MagicMock()
        created = _build_experiment()
        mock_response.json.return_value = created
        mock_response.raise_for_status.return_value = None
        mock_response.content = b'{"id":"test-id"}'

        list_response = MagicMock()
        list_response.json.return_value = []
        list_response.raise_for_status.return_value = None
        list_response.content = b'[]'

        session = MagicMock()
        session.request.side_effect = [list_response, mock_response]
        mock_requests.Session.return_value = session

        from ansible_collections.stevefulme1.h2o_ai.plugins.module_utils.api_client import ApiClient

        mock_module = MagicMock()
        mock_module.params = module_args
        client = ApiClient(mock_module)
        result = client.post("/api/v1/experiments", data={"name": "test"})
        assert result is not None
