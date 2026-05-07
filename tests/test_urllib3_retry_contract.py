from __future__ import annotations

from urllib3.util.retry import Retry


def test_legacy_method_whitelist_retry_contract() -> None:
    retry = Retry(total=2, method_whitelist={"GET", "HEAD"})

    assert retry.total == 2
    assert retry.method_whitelist == {"GET", "HEAD"}
