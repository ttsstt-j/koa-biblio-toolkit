from koa_biblio_toolkit.parsers.endnote import parse_endnote_records
from koa_biblio_toolkit.parsers.pubmed import parse_pubmed_nbib_records
from koa_biblio_toolkit.parsers.ris import parse_ris_records


def test_parse_ris_records_extracts_common_fields() -> None:
    text = (
        "TY  - JOUR\n"
        "TI  - KOA acupuncture outcomes\n"
        "AU  - Li, Ming\n"
        "AU  - Wang, Yu\n"
        "KW  - knee osteoarthritis\n"
        "ER  -\n"
    )
    records = parse_ris_records(text)
    assert len(records) == 1
    assert records[0]["title"] == "KOA acupuncture outcomes"
    assert records[0]["authors"] == ["Li, Ming", "Wang, Yu"]


def test_parse_endnote_records_extracts_common_fields() -> None:
    text = (
        "%0 Journal Article\n"
        "%T KOA with depression study\n"
        "%A Zhang, Lin\n"
        "%K depression\n"
        "\n"
    )
    records = parse_endnote_records(text)
    assert len(records) == 1
    assert records[0]["title"] == "KOA with depression study"
    assert records[0]["authors"] == ["Zhang, Lin"]


def test_parse_pubmed_nbib_records_extracts_common_fields() -> None:
    text = (
        "PMID- 123456\n"
        "TI  - Acupuncture for KOA and obesity\n"
        "FAU - Chen, Yu\n"
        "OT  - obesity\n"
        "\n"
    )
    records = parse_pubmed_nbib_records(text)
    assert len(records) == 1
    assert records[0]["title"] == "Acupuncture for KOA and obesity"
    assert records[0]["authors"] == ["Chen, Yu"]
