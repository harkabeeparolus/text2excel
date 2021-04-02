#! /usr/bin/env python3
"""
Converts a TSV (tab delimited) or CSV (comma delimited) text file to an Excel
xlsx file.

If the file name matches *.txt, TSV is assumed. Otherwise, CSV is assumed and
auto-detected.
"""
# By Fredrik Mellström <https://github.com/harkabeeparolus>
# Based on https://gist.github.com/konrad/4154786 by Konrad Förstner
import argparse
import sys

from text2excel import convert, version
from text2excel.fmt import format_paragraphs


def main(arguments=None):
    "Parse arguments and run text2excel from the command line."
    parser = make_argument_parser()
    args = parser.parse_args(arguments)

    errors = 0
    for input_file in args.files:
        xlsxfile = convert.write_excel(input_file, convert_numbers=args.numbers)

        if xlsxfile:
            print(f"Saved to file: {xlsxfile}")
        else:
            print(f"error: Could not convert {input_file}")
            errors += 1

    return 1 if errors else 0


def make_argument_parser():
    "Create and return and argparse parser"
    epilog = "More information: https://github.com/harkabeeparolus/text2excel"
    parser = argparse.ArgumentParser(
        description=format_paragraphs(__doc__),
        epilog=format_paragraphs(epilog),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-n",
        "--numbers",
        action="store_true",
        help="convert integers and floats to Excel numbers",
    )
    parser.add_argument("-V", "--version", action="version", version=version)
    parser.add_argument(
        "files", metavar="INPUT_FILE", nargs="+", help="text file(s) to convert"
    )
    return parser


if __name__ == "__main__":
    sys.exit(main())


# EOF
