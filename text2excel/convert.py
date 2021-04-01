#! /usr/bin/env python3
"""
Converts a CSV (tab delimited) file to an Excel xlsx file.
"""
import csv
import sys
from pathlib import Path
from typing import Optional
from typing import TextIO
from typing import Type

import openpyxl

# By Fredrik Mellström <https://github.com/harkabeeparolus>
# Based on https://gist.github.com/konrad/4154786 by Konrad Förstner


def write_excel(
    csv_filename: str, outfilename: str = "", convert_numbers: bool = False
) -> Path:
    """Read data from a csv text file, write output to an Excel xlsx file,
    and return a pathlib Path to it.

    If outfilename is not provided, it will be the same as csv_filename,
    but with a .xlsx suffix.
    """

    infile = Path(csv_filename)
    if outfilename:
        outfile = Path(outfilename)
    else:
        outfile = infile.with_suffix(".xlsx")

    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    with open(infile, newline="") as csvfile:
        dialect = get_dialect(csv_filename, csvfile)
        if not dialect:
            raise RuntimeError(f"Unable to determine dialect for {infile}")
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            if convert_numbers:
                worksheet.append([convert_to_number(cell) for cell in row])
            else:
                worksheet.append(list(row))

    workbook.save(str(outfile))

    return outfile


def get_dialect(
    filename: str, filehandle: Optional[TextIO] = None
) -> Type[csv.Dialect]:
    """Try to guess dialect based on file name or contents."""
    dialect: Type[csv.Dialect] = csv.excel_tab

    file_path = Path(filename)
    if file_path.suffix == ".txt":
        pass
    elif file_path.suffix == ".csv":
        if filehandle:
            dialect = csv.Sniffer().sniff(filehandle.read(4 * 1024))
            filehandle.seek(0)
    else:
        sys.stderr.write("Error: File does not have the ending csv or txt.\n")
        sys.exit(2)

    return dialect


def convert_to_number(cell: str):
    "Try to convert a string to an int or a float, else return unmodified."
    if cell.isnumeric():
        return int(cell)
    try:
        return float(cell)
    except ValueError:
        pass
    return cell


# EOF
