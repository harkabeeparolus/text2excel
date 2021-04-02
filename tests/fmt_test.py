"pytest tests for fmt"
from text2excel import fmt


def test_format_paragraphs(monkeypatch):
    "Try to dedent and reformat a paragraph."

    lorem_before = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum
    vehicula aliquam felis sed iaculis.

    Integer vulputate dui vulputate metus pulvinar volutpat. Nullam
    eu elementum libero.
    """

    lorem_width35 = (
        "Lorem ipsum dolor sit amet,\n"
        "consectetur adipiscing elit.\n"
        "Vestibulum vehicula aliquam\n"
        "felis sed iaculis.\n"
        "\n"
        "Integer vulputate dui\n"
        "vulputate metus pulvinar\n"
        "volutpat. Nullam eu elementum\n"
        "libero.\n"
    )

    with monkeypatch.context() as monkey:
        monkey.setenv("COLUMNS", "35")
        formatted = fmt.format_paragraphs(lorem_before)

    assert formatted == lorem_width35


def test_newlines():
    "Make sure we strip and reapply newlines correctly."

    assert fmt.format_paragraphs("\n\nfoo  bar") == "foo  bar"
    assert fmt.format_paragraphs("\n\nfoo bar baz\n\n") == "foo bar baz\n"


# EOF
