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


if __name__ == "__main__":
    print(format_paragraphs("".join(fileinput.input())))


# EOF
