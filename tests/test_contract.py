from __future__ import annotations

import json
from threading import Thread
from urllib.error import HTTPError
from urllib.request import urlopen

import requests
import urllib3

from app.main import Handler, ThreadingHTTPServer, _service_payload


def test_service_payload_contract_reports_runtime_versions() -> None:
    payload = _service_payload()

    assert payload == {
        "service": "security-tool-e2e-target",
        "requests": requests.__version__,
        "urllib3": urllib3.__version__,
        "status": "ok",
    }


def test_http_health_and_version_endpoints_share_contract() -> None:
    with _running_server() as base_url:
        for path in ("/", "/livez", "/readyz", "/version"):
            response = _get_json(f"{base_url}{path}")

            assert response["service"] == "security-tool-e2e-target"
            assert response["requests"] == requests.__version__
            assert response["urllib3"] == urllib3.__version__
            assert response["status"] == "ok"


def test_unknown_route_returns_json_404() -> None:
    with _running_server() as base_url:
        try:
            _get_json(f"{base_url}/missing")
        except HTTPError as exc:
            assert exc.code == 404
            payload = json.loads(exc.read().decode("utf-8"))
        else:  # pragma: no cover - defensive guard for the contract
            raise AssertionError("/missing should return 404")

    assert payload == {"path": "/missing", "status": "not_found"}


class _running_server:
    def __enter__(self) -> str:
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        host, port = self.server.server_address
        return f"http://{host}:{port}"

    def __exit__(self, exc_type, exc, tb) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)


def _get_json(url: str) -> dict[str, str]:
    with urlopen(url, timeout=5) as response:
        assert response.status == 200
        assert response.headers["Content-Type"] == "application/json"
        return json.loads(response.read().decode("utf-8"))
