#! /usr/bin/env python3

"""
Converts a CSV (tab delimited) file to an Excel xlsx file.
"""

import csv
import sys
from pathlib import Path

import openpyxl

# By Fredrik Mellström <https://github.com/harkabeeparolus>
# Based on https://gist.github.com/konrad/4154786


def write_excel(csv_filename=None, convert_numbers=False):
    """Read data from the csv.reader, and write to xlsxfile."""

    infile = Path(csv_filename)
    wb = openpyxl.Workbook()
    worksheet = wb.active
    with open(infile, newline="") as csvfile:
        dialect = get_dialect(csv_filename, csvfile)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            if convert_numbers:
                worksheet.append([convert_to_number(cell) for cell in row])
            else:
                worksheet.append([cell for cell in row])
    outfile = infile.with_suffix(".xlsx")

    wb.save(str(outfile))
    return outfile


def get_dialect(filename=None, filehandle=None):
    """Try to guess dialect based on file name."""
    dialect = None

    mypath = Path(filename)
    if mypath.suffix == ".txt":
        dialect = csv.excel_tab
    elif mypath.suffix == ".csv":
        pass
    else:
        sys.stderr.write("Error: File does not have the ending csv or txt.\n")
        sys.exit(2)

    if dialect is None and filehandle is not None:
        dialect = csv.Sniffer().sniff(filehandle.read(4 * 1024))
        filehandle.seek(0)

    return dialect


def convert_to_number(cell):
    "Try to convert a string to an int or a float, else return unmodified."
    if cell.isnumeric():
        return int(cell)
    try:
        return float(cell)
    except ValueError:
        pass
    return cell


# EOF
