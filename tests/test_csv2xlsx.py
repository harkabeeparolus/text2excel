"pytest tests for csv2xlsx"
import csv
import tempfile

import openpyxl
import pytest

from csv2xlsx import __version__
from csv2xlsx import cli
from csv2xlsx import convert


def test_version():
    "Check package structure and version number"
    assert __version__ == "0.3.0"


def test_argparse(capsys):
    "Make sure argparse works"
    with pytest.raises(SystemExit):
        cli.main(["--version"])

    captured = capsys.readouterr()
    assert captured.out == f"{__version__}\n"


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


# EOF
