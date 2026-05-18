# -*- coding: utf-8 -*-
# Copyright (c) 2025, Red Hat, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Ansible module to query H2O.ai pipeline resources."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module: pipeline_info
short_description: List or retrieve H2O.ai pipelines
description:
    - Retrieve information about H2O.ai pipeline resources.
version_added: "1.0.0"
author:
    - Steve Fulmer (@stevefulme1)
options:
    pipeline_id:
        description:
            - The pipeline id for the H2O.ai resource.
        type: str
extends_documentation_fragment:
    - stevefulme1.h2o_ai.common
requirements:
    - "python >= 3.9"
    - "requests"
"""

EXAMPLES = r"""
- name: List all pipelines
  stevefulme1.h2o_ai.pipeline_info:
    api_url: "https://cloud.h2o.ai"
    api_key: "my-api-key"
"""

RETURN = r"""
pipelines:
    description: List of pipeline resources.
    returned: always
    type: list
    elements: dict
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.stevefulme1.h2o_ai.plugins.module_utils.api_client import (
    COMMON_ARGS,
    ApiClient,
    HAS_REQUESTS,
)


def main():
    argument_spec = dict(
        pipeline_id=dict(type="str"),
    )
    argument_spec.update(COMMON_ARGS)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    if not HAS_REQUESTS:
        module.fail_json(msg="The 'requests' library is required. Install with: pip install requests")

    client = ApiClient(module)

    result = client.get("/api/v1/pipelines")
    items = result if isinstance(result, list) else result.get("data", result.get("items", []))
    module.exit_json(changed=False, pipelines=items)


if __name__ == "__main__":
    main()
