from __future__ import annotations

import json

import requests
import urllib3


def main() -> None:
    payload = {
        "service": "security-tool-e2e-target",
        "requests": requests.__version__,
        "urllib3": urllib3.__version__,
        "status": "ok",
    }
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()

