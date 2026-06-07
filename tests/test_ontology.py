from koa_biblio_toolkit.ontology import load_acupuncture_ontology


def test_load_acupuncture_ontology_contains_core_variants() -> None:
    ontology = load_acupuncture_ontology()
    terms = ontology["canonical_terms"]
    assert "electroacupuncture" in terms
    assert "moxibustion" in terms
    assert "电针" in terms["electroacupuncture"]
