Gitea
=====

Deploy [Gitea]() using a container image and run it as a systemd quadlet.

Requirements
------------

The following software is required on the target node:

* Systemd
* Podman (installed if absent)
* Firewalld (optional, installed if requested)

Also the collection `ansible.posix` is required if setting ports with `firewalld`.

The roles must run with superuser privileges to configure systemd and install necessary packages.

Role Variables
--------------

The following variables may be set to modify the behavior of the role:

| Name | Description | Required | Default |
| :--- | :---------- | :------: | :------ |
| gitea\_version | The version to dowload. See [https://dl.gitea.com/gitea](https://dl.gitea.com/gitea/) | No | "1.22.3" |
| gitea\_arch | The architecture to download. Valid values are: "arm-6", "x86-64", "aarch64". | No | "arm-6" |
| gitea\_hostname | The hostname to use to connect to Gitea | No | target hostname |
| gitea\_domain | The hostname domain to use to connect to Gitea | No | target domain |
| gitea\_http\_port | The internal container HTTP port. | No | 3080 |
| gitea\_externa\_http\_port | The HTTP port used to access the service. | No | 80 |
| gitea\_enable\_ssh | Weather to enable SSH acces or not. | No | True |
| gitea\_external\_ssh\_port | The SSH used to access the service. | No | 22 |
| gitea\_ssh\_port | The internal container SSH port. | No | 22 |
| gitea\_container\_image | The base container image to use. | No | alpine:latest |


Example Playbook
----------------

Deploy Gitea and open ports using firewalld:

```yaml
- name: Deploy Gitea and configure ports
  hosts: gitserver
  become: true
  gather_facts: false
  roles:
    - role: farrapos.homelab.gitea
      vars:
        gitea_use_firewalld: true
```

Deploy Gitea and define HTTP and SSH ports:

```yaml
- name: Deploy Gitea and configure access ports
  hosts: gitserver
  become: true
  gather_facts: false
  roles:
    - role: farrapos.homelab.gitea
      vars:
        gitea_use_firewalld: true
        gitea_externa_http_port: 3080
        gitea_externa_ssh_port: 3022
```

Deploy Gitea and define architecture:

```yaml
- name: "Deploy Gitea on a Raspberry Pi 1 B+"
  hosts: gitserver
  become: true
  gather_facts: false
  roles:
    - role: farrapos.homelab.gitea
      vars:
        gitea_arch: "arm-6"
```

License
-------

GPL-3.0-or later

Author Information
------------------

Rafael Jeffman (@rafasgj)
