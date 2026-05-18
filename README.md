        # stevefulme1.h2o_ai

        Ansible Collection for **H2O.ai**.

        ## Modules

        - `stevefulme1.h2o_ai.project` -- Manage H2O.ai projects
- `stevefulme1.h2o_ai.project_info` -- List or retrieve H2O.ai projects
- `stevefulme1.h2o_ai.experiment` -- Manage H2O Driverless AI experiments
- `stevefulme1.h2o_ai.experiment_info` -- List or retrieve H2O experiments
- `stevefulme1.h2o_ai.model` -- Manage H2O.ai models
- `stevefulme1.h2o_ai.model_info` -- List or retrieve H2O.ai models
- `stevefulme1.h2o_ai.deployment` -- Manage H2O.ai model deployments
- `stevefulme1.h2o_ai.deployment_info` -- List or retrieve H2O.ai deployments
- `stevefulme1.h2o_ai.dataset` -- Manage H2O.ai datasets
- `stevefulme1.h2o_ai.dataset_info` -- List or retrieve H2O.ai datasets
- `stevefulme1.h2o_ai.pipeline` -- Manage H2O.ai ML pipelines
- `stevefulme1.h2o_ai.pipeline_info` -- List or retrieve H2O.ai pipelines
- `stevefulme1.h2o_ai.wave_app` -- Manage H2O Wave applications
- `stevefulme1.h2o_ai.wave_app_info` -- List or retrieve H2O Wave applications

        ## Roles

        - `h2o_install` -- Install and configure H2O.ai platform
- `driverless_ai_deploy` -- Deploy H2O Driverless AI instances
- `wave_deploy` -- Deploy H2O Wave applications

        ## EDA Event Source

        - `stevefulme1.h2o_ai.h2o_events` -- Poll H2O.ai for events

        ## Requirements

        - Python >= 3.9
        - `requests` library
        - ansible-core >= 2.16

        ## Installation

        ```bash
        ansible-galaxy collection install stevefulme1.h2o_ai
        ```

        ## License

        GPL-3.0-or-later
