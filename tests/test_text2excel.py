"pytest tests for text2excel"
import csv
import tempfile

import openpyxl
import pytest

from text2excel import cli
from text2excel import convert
from text2excel import version


def test_argparse(capsys):
    "Make sure argparse works, and verify version"
    with pytest.raises(SystemExit):
        cli.main(["--version"])

    captured = capsys.readouterr()
    assert captured.out == f"{version}\n"


def test_get_dialect_filename():
    "Select csv dialect based on filename"
    dialect = convert.get_dialect(filename="foo.txt")
    assert dialect is csv.excel_tab


def test_convert_int():
    "Convert strings to integers"
    assert convert.convert_to_number("42") == 42
    assert convert.convert_to_number("42x") == "42x"


def test_convert_float():
    "Convert strings to floats"
    assert convert.convert_to_number("42.47") == 42.47
    assert convert.convert_to_number("42,47") == "42,47"


def test_openpyxl_alive():
    "Make sure we can create openpyxl Workbook objects"
    workbook = openpyxl.Workbook()
    assert hasattr(workbook, "worksheets")


def test_create_file():
    "Try to convert a file, check that outfile is >0 bytes"
    ntf = tempfile.NamedTemporaryFile
    with ntf(suffix=".txt", mode="w+") as infile, ntf(suffix=".xlsx") as outfile:
        print("one\ttwo\tthree\n1\t2\t3", file=infile)
        infile.flush()
        result = convert.write_excel(csv_filename=infile.name, outfilename=outfile.name)
        assert hasattr(result, "exists")
        assert result.exists()
        assert result.stat().st_size > 0


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
        monkey.setenv("COLUMNS", "32")
        formatted = cli.format_paragraphs(lorem1)
    assert formatted == lorem2
    assert cli.format_paragraphs("foo  bar") == "foo  bar"


# EOF
