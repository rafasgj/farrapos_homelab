# Farrapos Homelab

This is an Ansible collection to setup services for a home network focusing on small low-powered, low-spec'ed devices like the Raspberry Pi.

## DNS filter sink and nameserver

[Manage deployment](homelab/roles/dns/README.md) of a DNS filter sink using [AdGuard Home Container](https://github.com/AdguardTeam/AdGuardHome/wiki/Docker) with private domains managed by [Unbound](https://nlnetlabs.nl/projects/unbound/about/).

## Git Server

[Deploy a Git server](homelab/roles/gitea/README.md) with a web interface that allows management of repositories, review and approval of Pull Requests, and more using [Gitea](https://about.gitea.com).

## OCI Registry

[Deploy an OCI regitry](homelab/roles/registry/README.md) using [Docker registry image](https://hub.docker.com/_/registry).

## Authors

Rafael Guterres Jeffman (@rafasgj)
