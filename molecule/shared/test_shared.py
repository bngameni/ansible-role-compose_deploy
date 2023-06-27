#!/usr/bin/env python
import requests


def test_http_socket_listening(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
    assert host.socket("tcp://0.0.0.0:443").is_listening


def test_nginx_volumes_files_exists(host):
    nginx_volume = host.file("/app/nginx/nginx.conf")
    db_volume = host.file("/app/db")

    assert nginx_volume.exists
    assert db_volume.exists


def test_http_service_is_ok(host):
    ip_address = host.interface("eth0").addresses[0]
    adminer_request = requests.get(
        url=f"https://{ip_address}/",
        headers={"Host": "localhost"},
        verify=False,
    )

    assert adminer_request.status_code == 200
