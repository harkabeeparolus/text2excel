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
import shutil
import sys
import textwrap

from text2excel import convert
from text2excel import version


def main(arguments=None):
    "Parse arguments and run text2excel from the command line."
    if arguments is None:
        arguments = sys.argv[1:]

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


def format_paragraphs(input_text="", min_width=16):
    "Dedent and text wrap paragraphs to terminal width."
    width = max(min_width, shutil.get_terminal_size()[0] - 2)
    # dedent and remove any initial newlines
    text = textwrap.dedent(input_text).lstrip("\n")
    # we return a final newline if the input has one
    terminator = "\n" if text.endswith("\n") else ""
    # remove trailing whitespace, and split by empty lines
    paragraphs = "".join(text.rstrip()).split("\n\n")
    # wrap and join paragraphs together with empty lines between
    return "\n\n".join(textwrap.fill(p, width=width) for p in paragraphs) + terminator


if __name__ == "__main__":
    sys.exit(main())


# EOF
