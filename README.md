# text2excel

[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/harkabeeparolus/text2excel/Lint)](https://github.com/harkabeeparolus/text2excel/actions)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/text2excel)
[![PyPI](https://img.shields.io/pypi/v/text2excel)](https://pypi.org/project/text2excel/)
[![GitHub license](https://img.shields.io/github/license/harkabeeparolus/text2excel)](https://github.com/harkabeeparolus/text2excel/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This program converts CSV Or TSV text files to Microsoft Excel format. It
uses [openpyxl] to create Excel files.

As input it takes tab-separated `*.txt` files (TSV), or any CSV files
(Comma-Separated Values) that can be auto-detected by the Python standard
library [csv] module.

* There is a [GitHub page for text2excel][text2excel]

[text2excel]: https://github.com/harkabeeparolus/text2excel
[openpyxl]: https://openpyxl.readthedocs.io/
[csv]: https://docs.python.org/3/library/csv.html

## Example

```bash
$ printf "one\ttwo\tthree\n1\t2\t3\n" | tee my_data_file.txt
one two three
1   2   3

$ text2excel --numbers my_data_file.txt
Saved to file: my_data_file.xlsx
```

## Installation

I recommend installing *text2excel* with [pipx]:

```bash
pipx install text2excel
```

If you don't already have it, a guide for how to install _pipx_ is provided
below on this page.

To upgrade *text2excel* to the latest version, simply run:

```bash
pipx upgrade text2excel
```

Or `pipx upgrade-all` if you want to go crazy. 😉

If you want to bundle up *text2excel* into a single, standalone executable Python
[zipapp], I highly recommend [shiv]. For example:

```bash
shiv -o text2excel -p "/usr/bin/env python3" -c text2excel text2excel
```

If _shiv_ doesn't work for you for some reason, you can also use [PEX]:

```bash
pex -o text2excel -c text2excel text2excel
```

[pipx]: https://github.com/pipxproject/pipx/
[shiv]: https://github.com/linkedin/shiv
[PEX]: https://github.com/pantsbuild/pex
[zipapp]: https://docs.python.org/3/library/zipapp.html

### Installing pipx

I suggest installing everything with [pipx], because it is fantastic. 🙂

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

At this point, you may need to logout to refresh your shell `$PATH` before
proceeding.

For further details, see the official
[pipx installation guide](https://pipxproject.github.io/pipx/installation/).

### Installing shiv

I recommend that you use _pipx_ to install shiv:

```bash
pipx install shiv
```

Alternatively, if you really don't want to use pipx for some reason, you can
simply run `python3 -m pip install --user shiv`. Then, if necessary, manually
reconfigure your shell `$PATH` to find any pip installed binaries.

## News

Please see the [changelog](CHANGELOG.md) for more details.

## Contributing

Do you want to help out with this project?

* Please check the [CONTRIBUTING](CONTRIBUTING.md) guide.

## Credits

This project was originally based on
[a Gist by Konrad Förstner](https://gist.github.com/konrad/4154786).
