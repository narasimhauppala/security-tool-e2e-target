from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os

import jinja2


def _render_legacy_template() -> str:
    from jinja2 import Environment, contextfilter

    @contextfilter
    def legacy_upper(context: object, value: str) -> str:
        return value.upper()

    env = Environment(autoescape=True)
    env.filters["legacy_upper"] = legacy_upper
    return env.from_string("{{ 'legacy'|legacy_upper }}").render()


def _service_payload() -> dict[str, str]:
    return {
        "service": "security-tool-e2e-target",
        "jinja2": jinja2.__version__,
        "status": "ok",
    }


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path in {"/", "/livez", "/readyz", "/version"}:
            self._send_json(_service_payload())
            return
        if self.path == "/legacy-render":
            self._send_json({"status": "ok", "rendered": _render_legacy_template()})
            return
        self._send_json({"status": "not_found", "path": self.path}, status=404)

    def log_message(self, format: str, *args: object) -> None:
        return

    def _send_json(self, payload: dict[str, str], *, status: int = 200) -> None:
        body = json.dumps(payload, sort_keys=True).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> None:
    port = int(os.environ.get("PORT", "8080"))
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
