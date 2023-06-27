# Ansible role - compose_deploy
[![Maintainer](https://img.shields.io/badge/maintained%20by-bngameni-e00000?style=flat-square)](https://github.com/bngameni)
[![License](https://img.shields.io/github/license/bngameni/ansible-role-compose_deploy?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/bngameni/ansible-role-compose_deploy?style=flat-square)](https://github.com/bngameni/ansible-role-compose_deploy/releases)
[![Status](https://img.shields.io/github/actions/workflow/status/bngameni/ansible-role-compose_deploy/molecule.yml?style=flat-square&label=tests&branch=main)](https://github.com/bngameni/ansible-role-compose_deploy/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/bngameni/compose_deploy)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure docker-compose service

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install bngameni.compose_deploy
```

## :gear: Role variables

| Variable                            | Default Value | Description                                                                                       |
|-------------------------------------|---------------|---------------------------------------------------------------------------------------------------|
| compose_deploy_volumes_dir          | []            | Paths to volumes to create (only when using the "bind" type)                                      |
| compose_deploy_manifests            | []            | Path to the docker-compose.yaml file (leave blank if using other files)                           |
| compose_deploy_templates            | []            | Path to the docker-compose.yaml files as Jinja2 templates (leave blank if using other files)      |
| compose_deploy_definition           | []            | Compose definition (content of the docker-compose file)                                           |
| compose_deploy_config_files         | []            | Path to folder or files to copy to the remote for the compose file                                |
| compose_deploy_use_selfsigned_ssl   | false         | Use SSL for installing the compose service. Set the domain name to get self-signed certificates   |
| compose_deploy_domain_name          | []            | Domain name to use for installation                                                               |


&nbsp;

Additionally, here is a structure of items:

* compose_deploy_manifests
* compose_deploy_templates
* compose_deploy_config_files

| Attributes                          | Default Value          | Description                                                                              |
|-------------------------------------|------------------------|------------------------------------------------------------------------------------------|
| src                                 | None **required**      | The source path of the file                                                              |
| dest                                | None **required**      | The destination path on the remote server where the file will be                         |
| mode                                | 0644                   | The file permissions/mode for the file                                                   |

&nbsp;
* compose_deploy_definition

| Attributes                          | Default Value          | Description                                                                              |
|-------------------------------------|------------------------|------------------------------------------------------------------------------------------|
| name                                | None **required**      | The name of service/application                                                          |
| value                               | None **required**      | The docker-compose definition(content of manifest)                                       |

&nbsp;
* compose_deploy_domain_name

| Attributes                        | Default Value        | Description                                                                              |
|-----------------------------------|----------------------|------------------------------------------------------------------------------------------|
| dest_path                         | /etc/ssl             | The destination path on the remote server where the manifest file will be copied.        |
| country_name                      | FR                   | The country name used for generating self-signed certificates.                           |
| common_name                       | None  **required**   | The common name used for generating self-signed certificates.                            |
| state_or_province_name            | None                 | The state or province name used for generating self-signed certificates.                 |
| organization_name                 | None                 | The organization name used for generating self-signed certificates.                      |
| organizational_unit_name          | None                 | The organizational unit name used for generating self-signed certificates.               |
| email_address                     | None                 | The email address used for generating self-signed certificates.                          |


## :arrows_counterclockwise: Dependencies

N/A


## :pencil2: Example Playbook

* Use compose definition

```yaml
---
- name: Converge
  hosts: all
  vars:
    compose_deploy_volumes_dir:
      - /app/nginx
      
    compose_deploy_config_files:
      - src: files/nginx/nginx.conf
        dest: /app/nginx

    compose_deploy_use_selfsigned_ssl: true
    compose_deploy_domain_names:
      - name: "localhost"

    compose_deploy_definition:
      - name: flask
        value:
          version: '3.9'
          services:
            db:
              image: postgres
              restart: always
              environment:
                POSTGRES_PASSWORD: example
              volumes:
                - /app/db:/var/lib/postgresql/data
            adminer:
              image: adminer
              restart: always
            nginx:
              image: nginx
              restart: always
              ports:
                - "80:80/tcp"
                - "443:443/tcp"
              volumes:
                - type: bind
                  source: /app/nginx/nginx.conf
                  target: /etc/nginx/conf.d/nginx.conf
                - type: bind
                  source: /etc/ssl/localhost
                  target: /etc/ssl/localhost

  roles:
    - bngameni.compose_deploy
```

* Use yaml file

```yaml
---
- name: Converge
  hosts: all
  vars:
    compose_deploy_volumes_dir:
      - /app/nginx
      
    compose_deploy_config_files:
      - src: files/nginx/nginx.conf
        dest: /app/nginx

    compose_deploy_use_selfsigned_ssl: true
    compose_deploy_domain_names:
      - name: "localhost"

    compose_deploy_manifests:
      - src: files/compose/docker-compose.yml
        dest: /app/

  roles:
    - bngameni.compose_deploy
```

* Use jinja2 template file

```yaml
---
- name: Converge
  hosts: all
  vars:
    compose_deploy_volumes_dir:
      - /app/nginx
      
    compose_deploy_config_files:
      - src: files/nginx/nginx.conf
        dest: /app/nginx

    compose_deploy_use_selfsigned_ssl: true
    compose_deploy_domain_names:
      - name: "localhost"

    compose_deploy_templates:
      - src: templates/compose/docker-compose.yml.j2
        dest: /app/

  roles:
    - bngameni.compose_deploy
```

&nbsp;
## :closed_lock_with_key: [Hardening](HARDENING.md)

&nbsp;
## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

&nbsp;
## :copyright: [License](LICENSE)
[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
