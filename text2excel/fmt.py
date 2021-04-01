#! /usr/bin/env python3
"Text formatting utility, wrap text to screen width."
# By Fredrik Mellström <https://github.com/harkabeeparolus>
import fileinput
import re
import shutil
import textwrap

NEWLINES_RE = re.compile(r"\n{2,}")


def format_paragraphs(input_text="", width=0, margin=5, min_width=16):
    "Dedent and text wrap paragraphs to terminal width."
    if width <= 0:
        columns, _ = shutil.get_terminal_size()
        width = max(min_width, columns - margin)

    # dedent and remove any initial newlines
    text = textwrap.dedent(input_text).lstrip("\n")

    # we will return a final newline if the input has one
    terminator = "\n" if text.endswith("\n") else ""

    # remove trailing whitespace, and split by empty lines
    paragraphs = NEWLINES_RE.split(text.rstrip())

    # wrap and join paragraphs together with empty lines between
    wrapper = textwrap.TextWrapper(width=width)
    return "\n\n".join(wrapper.fill(p) for p in paragraphs) + terminator


def merge_input_files(files=None):
    "Iterate over lines in all input files."
    with fileinput.input(files=files) as input_files:
        for line in input_files:
            if fileinput.isfirstline() and fileinput.lineno():
                # insert a blank line between input files
                yield "\n"
            yield str(line)


if __name__ == "__main__":
    print(format_paragraphs("".join(merge_input_files())))


# EOF
