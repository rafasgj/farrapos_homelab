DNS
===

Manage deployment of a DNS filter sink and an embedded DNS nameserver for local networks.

Requirements
------------

The following software is required on the target node:

* Systemd
* Podman (installed if absent)
* Firewalld (optional, installed if requested)

The role must run with superuser privileges to configure systemd and install necessary packages.


Role Variables
--------------

The following variables may be set to modify the behavior of the role:

| Name | Description | Required | Default |
| :--- | :---------- | :------: | :------ |
| `state` | Define the state to ensure. One of 'present', 'absent', 'updated'. | no | `present` |

**DNS Nameserver variables**

| Name | Description | Required | Default |
| :--- | :---------- | :------: | :------ |
| `dns_deploy_nameserver` | When set to true deploy the emebeded nameserver (Unbound). | no | `true` |
| `dns_domain` | List of domains managed by the nameserver. | When `dns_deploy_nameserver` is `true` | - |
| `dns_zones` | A list of zone names and files with the DNS zone configuration. The `name` attribute is required. The `file` attribute is not, if the file name is `<zone name>.zone`. | When `dns_deploy_nameserver` is `true` | - |
| `dns_verbosity` | Set the nameserver log verbosity. | no | 3 |

**DNS filter sink variables**

| Name | Description | Required | Default |
| :--- | :---------- | :------: | :------ |
| `dns_deploy_filter` | When set to true deploy the DNS filter sink (AdGuard Home). | no | `true` |
| `dns_credentials` | Define the credentials (`username` and `password`) for the Web configuration tool. `password` is given in clear text, and is hashed to be stored. | When `dns_deploy_filter` is `true` | - |
| `dns_dashboard_port` | The port to bind the Web configuration tool. | no | 5380 |

**Notes**

- In case you already use the subnet `172.16.53.0/24`, you should set `dns_subnet` to a subnet CIDR available on your network.
- One can choose the AdGuard Home container image by setting `dns_adguard_image`.
- The `updated` state will replace domains and zones by the ones provided.

Dependencies
------------

This role depends on the collections:

* ansible.posix

Example Playbook
----------------

Deploy both DNS filter and nameserver:

```yaml
- name: Deploy AdGuard and Unbound
  hosts: dnssink
  become: true
  gather_facts: false
  roles:
    - role: farrapos.homelab.dns
      vars:
        dns_deploy_nameserver: true
        dns_domain:  ["example.com"]
        dns_zones:
          - name: example.com.
          - name: 173.168.192.in-addr.arpa.
        dns_deploy_filter: true
        dns_credentials:
          username: admin
          password: secret123
```

Update zone files:

```yaml
- name: Deploy AdGuard and Unbound
  hosts: dnssink
  become: true
  gather_facts: false
  roles:
    - role: farrapos.homelab.dns
      state: updated
      vars:
        dns_domain: ["example.test"]
        dns_zones:
          - name: example.test.
            file: data/my-zone-file
          - name: 173.168.192.in-addr.arpa.
```

Undeploy DNS sink and nameserver:

```yaml
- name: Deploy AdGuard and Unbound
  hosts: dnssink
  become: true
  gather_facts: false
  roles:
    - role: farrapos.homelab.dns
      state: absent
```

License
-------

GPL-3.0-or later

Author Information
------------------

Rafael Jeffman (@rafasgj)
