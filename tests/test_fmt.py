"pytest tests for fmt"
from text2excel import fmt


def test_format_paragraphs(monkeypatch):
    "Try to dedent and reformat a paragraph."
    lorem1 = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum
    vehicula aliquam felis sed iaculis.

    Integer vulputate dui vulputate metus pulvinar volutpat. Nullam
    eu elementum libero.
    """
    lorem2 = (
        "Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit.\n"
        "Vestibulum vehicula aliquam\nfelis sed iaculis.\n\nInteger "
        "vulputate dui\nvulputate metus pulvinar\nvolutpat. Nullam "
        "eu elementum\nlibero.\n"
    )

    with monkeypatch.context() as monkey:
        monkey.setenv("COLUMNS", "35")
        formatted = fmt.format_paragraphs(lorem1)
    assert formatted == lorem2
    assert fmt.format_paragraphs("foo  bar") == "foo  bar"


# EOF
