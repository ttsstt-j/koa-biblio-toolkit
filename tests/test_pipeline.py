from koa_biblio_toolkit.pipeline import (
    list_comorbidity_templates,
    load_comorbidity_template,
)


def test_list_comorbidity_templates_contains_required_templates() -> None:
    templates = list_comorbidity_templates()
    assert "koa_sleep_disorders" in templates
    assert "koa_depression" in templates
    assert "koa_sarcopenia" in templates
    assert "koa_obesity" in templates


def test_load_comorbidity_template_returns_expected_content() -> None:
    template = load_comorbidity_template("koa_sleep_disorders")
    assert template["base_condition"] == "knee osteoarthritis"
    assert "insomnia" in template["search_terms"]
