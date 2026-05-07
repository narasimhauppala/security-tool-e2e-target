from __future__ import annotations

from jinja2 import Environment, contextfilter


@contextfilter
def prefix_with_template_name(context, value: str) -> str:
    template_name = context.name or "inline"
    return f"{template_name}:{value}"


def test_legacy_contextfilter_extension_contract() -> None:
    environment = Environment(autoescape=True)
    environment.filters["prefix_with_template_name"] = prefix_with_template_name
    template = environment.from_string("{{ 'ok'|prefix_with_template_name }}")
    template.name = "contract"

    assert template.render() == "contract:ok"
