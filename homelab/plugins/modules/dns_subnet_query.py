# -*- coding: utf-8 -*-

# Authors:
#   Rafael Guterres Jeffman <rafasgj@gmail.com>
#
# Copyright (C) 2025 Rafael Guterres Jeffman <rafasgj@gmail.com>
# see file 'COPYING' for use and warranty information
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Retrieve the network, gateway, nameserver and dns filter ips."""

from ansible.module_utils.basic import AnsibleModule

__metaclass__ = type   # pylint: disable=invalid-name

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'supported_by': 'community',
    'status': ['preview'],
}

DOCUMENTATION = '''
---
module: dns_query_ip_addr
short_description: Retrieve IP addresses from a CIDR to deploy Farrapos DNS.
description: Retrieve IP addresses from a CIDR to deploy Farrapos DNS.
options:
  dns_subnet:
    description: The IPv4 subnet CIDR to query
    type: str
    required: yes
  dns_ip_query:
    description: ntp server pool to use
    type: str
    choices: ["network", "gateway", "nameserver", "filter"]
    required: yes
author:
    - Rafael Jeffman (@rafasgj)
'''

EXAMPLES = '''
- name: Query POD gateway address
  dns_subnet_query:
    dns_subnet: "172.16.53.255/30"
'''

RETURN = '''
dns_ips:
  dns_subnet: "172.16.53.248/29"
  dns_gateway: "172.16.53.249"
  dns_nameserver: "172.16.53.250"
  dns_filter: "172.16.53.251"
'''

# pylint: disable=wrong-import-position, wrong-import-order
import ipaddress

# pylint: enable=wrong-import-position, wrong-import-order


def main():
    """Module entry point."""
    ansible_module = AnsibleModule(
        argument_spec={"dns_subnet": {"required": True, "type": "str"}},
        supports_check_mode=False,
    )
    ansible_module._ansible_debug = True  # pylint: disable=protected-access

    cidr = ansible_module.params.get('dns_subnet')
    try:
        iface = ipaddress.IPv4Interface(cidr)
    except ipaddress.AddressValueError:
        ansible_module.fail_json(msg=f"Invalid CIDR: '{cidr}'")

    net = iface.network
    result = {
        "dns_subnet": str(net),
        "dns_gateway": str(net[1]),
        "dns_nameserver": str(net[2]),
        "dns_filter": str(net[3]),
    }

    ansible_module.exit_json(changed=False, dns_ips=result)


if __name__ == "__main__":
    main()
