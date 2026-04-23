# [1.1.0](https://github.com/bngameni/ansible-role-compose_deploy/compare/v1.0.0...v1.1.0) (2026-04-23)


### Features

* **role:** render j2 files in compose projects ([#6](https://github.com/bngameni/ansible-role-compose_deploy/issues/6)) ([b0b91af](https://github.com/bngameni/ansible-role-compose_deploy/commit/b0b91afbec5965a751f7188ac1770c28f4f04706))

# 1.0.0 (2026-04-04)


* feat!: drop legacy compose_deploy role inputs ([adf9860](https://github.com/bngameni/ansible-role-compose_deploy/commit/adf98609e42198637c34359e19b7bb1dffd0b589))


### Bug Fixes

* add execution mode to folder creation for allow navigation in folder ([edf23cc](https://github.com/bngameni/ansible-role-compose_deploy/commit/edf23cc08c5451a1d9130a5b203b711d1e11d8a2))
* **ci:** rollback to molecule action 4.0.9 ([ea7d377](https://github.com/bngameni/ansible-role-compose_deploy/commit/ea7d3771133bfcf846c0ab4aae2860b0b6d97609))
* **release:** support semantic-release on protected main ([8d91bf0](https://github.com/bngameni/ansible-role-compose_deploy/commit/8d91bf07772489d7b1e7cb7e2cf6c1241f89d02a))
* update release configuration to include changelog and Git steps ([#4](https://github.com/bngameni/ansible-role-compose_deploy/issues/4)) ([4daf2ca](https://github.com/bngameni/ansible-role-compose_deploy/commit/4daf2ca76abc9f59e5ef143dc7ce488f3619f905))


### Features

* add semantic-release configuration ([2b1651c](https://github.com/bngameni/ansible-role-compose_deploy/commit/2b1651c3046b54d5931e444c4b990ff3e7272089))
* allow setting mode of volume dir to create ([30ed628](https://github.com/bngameni/ansible-role-compose_deploy/commit/30ed628e6b2240e3e75fd3228701aaf1f8d7b46b))
* ansible-lint configuration ([d38651a](https://github.com/bngameni/ansible-role-compose_deploy/commit/d38651a5ae3db8b2cf1b9518647d16a61d746c36))
* **ci:** push role in galaxy ([45ab10e](https://github.com/bngameni/ansible-role-compose_deploy/commit/45ab10e919848617453f42be34f818b3e09300cd))
* default vars for launch role ([f7eec5e](https://github.com/bngameni/ansible-role-compose_deploy/commit/f7eec5ed184d180aabd2af0327f3ef9e4f37c7a1))
* deploy service with docker compose ([2689eee](https://github.com/bngameni/ansible-role-compose_deploy/commit/2689eee0094ea675ef8052b0609e0715c8313039))
* generate self-signed certificated when enabled ([8bddc5e](https://github.com/bngameni/ansible-role-compose_deploy/commit/8bddc5eff88c646f48f7ab0a9e90ee62feef2076))
* **git:** create gitignore file ([d163b6e](https://github.com/bngameni/ansible-role-compose_deploy/commit/d163b6edfa3b27cdd5f9c44e1cee50256429eb3a))
* **git:** retrieve file from claranet cookiecutter ([df2b89e](https://github.com/bngameni/ansible-role-compose_deploy/commit/df2b89eb6be7a4c50b9663404bbb53cf3a81a063))
* **role:** adopt project-based compose deployment ([7cd426c](https://github.com/bngameni/ansible-role-compose_deploy/commit/7cd426cf94149350e1b3a0d5ebe39489e8e1bbb2))
* setup compose directory using input data ([ef49f57](https://github.com/bngameni/ansible-role-compose_deploy/commit/ef49f573c77b9a56b6f489c352373fa197282eb0))


### BREAKING CHANGES

* the role no longer supports compose_deploy_manifests, compose_deploy_templates, compose_deploy_definition, compose_deploy_config_files, compose_deploy_use_selfsigned_ssl, or compose_deploy_domain_names. Use compose_deploy_projects for project directories and compose_deploy_volumes_dir for bind-mount directories.
