#! /usr/bin/env python3
"""
FUNCTION: Converts a CSV (tab delimited) file to an Excel xlsx file.

Copyright (c) 2016, Konrad Foerstner <konrad@foerstner.org>

Permission to use, copy, modify, and/or distribute this software for
any purpose with or without fee is hereby granted, provided that the
above copyright notice and this permission notice appear in all
copies.

THE SOFTWARE IS PROVIDED 'AS IS' AND THE AUTHOR DISCLAIMS ALL
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE
AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL
DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR
PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER
TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

"""
# https://gist.github.com/konrad/4154786

import sys
import argparse
from pathlib import Path
import csv
import openpyxl


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--no-numbers", action="store_true")
    parser.add_argument("input_file")
    args = parser.parse_args(argv)

    dialect = None
    mypath = Path(args.input_file)
    if mypath.suffix == ".txt":
        dialect = csv.excel_tab
    elif mypath.suffix == ".csv":
        pass
    else:
        sys.stderr.write("Error: File does not have the ending csv or txt.\n")
        sys.exit(2)

    wb = openpyxl.Workbook()
    worksheet = wb.active
    with open(mypath, newline="") as csvfile:
        if dialect is None:
            dialect = csv.Sniffer().sniff(csvfile.read(4 * 1024))
            csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)
        for row in reader:
            if args.no_numbers:
                worksheet.append([cell for cell in row])
            else:
                worksheet.append([convert_to_number(cell) for cell in row])
    outfile = mypath.with_suffix(".xlsx")
    wb.save(str(outfile))
    print("Saved to file: %s" % outfile)
    return 0


def convert_to_number(cell):
    if cell.isnumeric():
        return int(cell)
    try:
        return float(cell)
    except ValueError:
        pass
    return cell


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))


# EOF
