Role Name
=========

Deploy a local OCI registry using a container image and run it as a systemd quadlet.

Requirements
------------

The following software is required on the target node:

* Systemd
* Podman (installed if absent)
* Firewalld (optional, installed if requested).

The role must run with superuser privileges to configure systemd and install necessary packages.

Role Variables
--------------

The following variables may be set to modify the behavior of the role:

| Name | Description | Required | Default |
| :--- | :---------- | :------: | :------ |
| `registry\_arch`  | The achitecture to download. Valid values are: "arm-6", "x86-64", "aarch64". | no | autodetected |
| `registry\_image`  | The OCI registry image to use. Will override `registry_arch` setting. | no | [registry:latest](https://hub.docker.com/layers/library/registry) |
| `registry\_port`  | The external service TCP port. | no | 80 |
| `registry\_use\_firewalld` | Whether to use firewalld to open ports. | no | true |

Dependencies
------------

This role depends on the collections:

* ansible.posix

Example Playbook
----------------

Deploy an OCI registry using a specific port:

```yaml
- name: Deploy registry
  hosts: registry
  become: true
  gather_facts: false
  roles:
    - role: farrapos.homelab.registry
      vars:
        registry_port: 5000
```

License
-------

GPL-3.0-or later

Author Information
------------------

Rafael Jeffman (@rafasgj)
