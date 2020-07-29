#! /usr/bin/env python3
"Text formatting utility, wrap text to screen width."
# By Fredrik Mellström <https://github.com/harkabeeparolus>
import fileinput
import shutil
import textwrap


def format_paragraphs(input_text="", min_width=16, margin=5):
    "Dedent and text wrap paragraphs to terminal width."
    columns, _ = shutil.get_terminal_size()
    width = max(min_width, columns - margin)

    # dedent and remove any initial newlines
    text = textwrap.dedent(input_text).lstrip("\n")

    # we return a final newline if the input has one
    terminator = "\n" if text.endswith("\n") else ""

    # remove trailing whitespace, and split by empty lines
    paragraphs = "".join(text.rstrip()).split("\n\n")

    # wrap and join paragraphs together with empty lines between
    return "\n\n".join(textwrap.fill(p, width=width) for p in paragraphs) + terminator


def merge_input_files(files=None):
    "Iterate over lines in all input files."
    with fileinput.input(files=files) as input_files:
        for line in input_files:
            if fileinput.isfirstline() and fileinput.lineno():
                # insert a blank line between input files
                yield "\n"
            yield line


if __name__ == "__main__":
    print(format_paragraphs("".join(merge_input_files())))


# EOF
