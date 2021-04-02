"pytest tests for text2excel"
import csv
import tempfile

import openpyxl
import pytest

from text2excel import cli, convert, version


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


def read_xlsx_file(filename):
    "Read from an Excel file and return tuples"
    workbook = openpyxl.load_workbook(filename)
    return tuple(tuple(cell.value for cell in row) for row in workbook.active.rows)


def test_create_file():
    "Try to convert a file, check that outfile is >0 bytes"
    input_data = "one\ttwo\tthree\n1\t2\t3"
    output_data = (("one", "two", "three"), (1, 2, 3))

    ntf = tempfile.NamedTemporaryFile
    with ntf(suffix=".txt", mode="w+") as infile, ntf(suffix=".xlsx") as outfile:
        print(input_data, file=infile)
        infile.flush()
        outpath = convert.write_excel(
            infile.name, outfilename=outfile.name, convert_numbers=True
        )
        assert hasattr(outpath, "exists")
        assert outpath.exists()
        assert outpath.stat().st_size > 0
        assert read_xlsx_file(outpath) == output_data


# EOF
