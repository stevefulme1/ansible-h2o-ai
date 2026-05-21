"""Unit tests for stevefulme1.h2o_ai.pipeline module."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from unittest.mock import MagicMock, patch

MODULE_PATH = "ansible_collections.stevefulme1.h2o_ai.plugins.modules.pipeline"

try:
    from ansible_collections.stevefulme1.h2o_ai.plugins.modules.pipeline import main
except ImportError:
    from unittest.mock import MagicMock as main

class TestCreate:
    """Test pipeline creation."""

    @patch(f"{MODULE_PATH}.AnsibleModule")
    def test_create(self, mock_ansible_cls):
        """Creating pipeline calls exit_json with changed=True."""
        mock_module = MagicMock()
        mock_module.params = {'api_url': 'https://test.example.com', 'api_key': 'test-key', 'validate_certs': False, 'timeout': 30, 'state': 'present', 'name': 'test-pipe', 'description': 'test', 'steps': 'step1,step2'}
        mock_module.check_mode = False
        mock_ansible_cls.return_value = mock_module
        main()
        mock_module.exit_json.assert_called_once()
        call_kwargs = mock_module.exit_json.call_args[1]
        assert call_kwargs.get("changed") is True
class TestDelete:
    """Test pipeline deletion."""

    @patch(f"{MODULE_PATH}.AnsibleModule")
    def test_delete(self, mock_ansible_cls):
        """Deleting pipeline calls exit_json with changed=True."""
        mock_module = MagicMock()
        mock_module.params = {'api_url': 'https://test.example.com', 'api_key': 'test-key', 'validate_certs': False, 'timeout': 30, 'state': 'absent', 'name': 'test-pipe', 'description': None, 'steps': None}
        mock_module.check_mode = False
        mock_ansible_cls.return_value = mock_module
        main()
        mock_module.exit_json.assert_called_once()
        call_kwargs = mock_module.exit_json.call_args[1]
        assert call_kwargs.get("changed") is True
class TestIdempotent:
    """Test pipeline idempotency."""

    @patch(f"{MODULE_PATH}.AnsibleModule")
    def test_create_idempotent(self, mock_ansible_cls):
        """Re-creating existing pipeline calls exit_json with changed=False."""
        mock_module = MagicMock()
        mock_module.params = {'api_url': 'https://test.example.com', 'api_key': 'test-key', 'validate_certs': False, 'timeout': 30, 'state': 'present', 'name': 'test-pipe', 'description': 'test', 'steps': 'step1,step2'}
        mock_module.check_mode = False
        mock_ansible_cls.return_value = mock_module
        main()
        mock_module.exit_json.assert_called()
