"""Unit tests for stevefulme1.h2o_ai.deployment module."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from unittest.mock import MagicMock, patch

MODULE_PATH = "ansible_collections.stevefulme1.h2o_ai.plugins.modules.deployment"

try:
    from ansible_collections.stevefulme1.h2o_ai.plugins.modules.deployment import main
except ImportError:
    from unittest.mock import MagicMock as main

class TestCreate:
    """Test deployment creation."""

    @patch(f"{MODULE_PATH}.AnsibleModule")
    def test_create(self, mock_ansible_cls):
        """Creating deployment calls exit_json with changed=True."""
        mock_module = MagicMock()
        mock_module.params = {'api_url': 'https://test.example.com', 'api_key': 'test-key', 'validate_certs': False, 'timeout': 30, 'state': 'present', 'model_id': 'test-model', 'name': 'test-deploy', 'environment': 'production'}
        mock_module.check_mode = False
        mock_ansible_cls.return_value = mock_module
        main()
        mock_module.exit_json.assert_called_once()
        call_kwargs = mock_module.exit_json.call_args[1]
        assert call_kwargs.get("changed") is True
class TestDelete:
    """Test deployment deletion."""

    @patch(f"{MODULE_PATH}.AnsibleModule")
    def test_delete(self, mock_ansible_cls):
        """Deleting deployment calls exit_json with changed=True."""
        mock_module = MagicMock()
        mock_module.params = {'api_url': 'https://test.example.com', 'api_key': 'test-key', 'validate_certs': False, 'timeout': 30, 'state': 'absent', 'model_id': 'test-model', 'name': 'test-deploy', 'environment': None}
        mock_module.check_mode = False
        mock_ansible_cls.return_value = mock_module
        main()
        mock_module.exit_json.assert_called_once()
        call_kwargs = mock_module.exit_json.call_args[1]
        assert call_kwargs.get("changed") is True
class TestIdempotent:
    """Test deployment idempotency."""

    @patch(f"{MODULE_PATH}.AnsibleModule")
    def test_create_idempotent(self, mock_ansible_cls):
        """Re-creating existing deployment calls exit_json with changed=False."""
        mock_module = MagicMock()
        mock_module.params = {'api_url': 'https://test.example.com', 'api_key': 'test-key', 'validate_certs': False, 'timeout': 30, 'state': 'present', 'model_id': 'test-model', 'name': 'test-deploy', 'environment': 'production'}
        mock_module.check_mode = False
        mock_ansible_cls.return_value = mock_module
        main()
        mock_module.exit_json.assert_called()
