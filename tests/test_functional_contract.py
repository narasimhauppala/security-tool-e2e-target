import json
from pathlib import Path


def test_lodash_version_contract_is_unchanged():
    package_json = json.loads((Path(__file__).resolve().parents[1] / "package.json").read_text())

    assert package_json["dependencies"]["lodash"] == "4.17.20"
