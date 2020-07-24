import csv

import pytest

from csv2xlsx import __version__
from csv2xlsx import cli
from csv2xlsx import convert


def test_version():
    assert __version__ == "0.1.0"


def test_argparse(capsys):
    with pytest.raises(SystemExit):
        cli.main(["--version"])

    captured = capsys.readouterr()
    assert captured.out == f"{__version__}\n"


def test_get_dialect_filename():
    dialect = convert.get_dialect(filename="foo.txt")
    assert dialect is csv.excel_tab


def test_convert_int():
    assert convert.convert_to_number("42") == 42
    assert convert.convert_to_number("42x") == "42x"


def test_convert_float():
    assert convert.convert_to_number("42.47") == 42.47
    assert convert.convert_to_number("42,47") == "42,47"


# EOF