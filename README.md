# text2excel

[myactions]: https://github.com/harkabeeparolus/text2excel/actions
[mypypi]: https://pypi.org/project/text2excel/
[mylicense]: https://github.com/harkabeeparolus/text2excel/blob/master/LICENSE
[black]: https://github.com/psf/black

[![Lint and Test](https://github.com/harkabeeparolus/text2excel/actions/workflows/python-package.yml/badge.svg)][myactions]
[![PyPI - Python Versions](https://img.shields.io/pypi/pyversions/text2excel)][mypypi]
[![PyPI](https://img.shields.io/pypi/v/text2excel)][mypypi]
[![GitHub license](https://img.shields.io/github/license/harkabeeparolus/text2excel)][mylicense]
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]
[![CodeQL](https://github.com/harkabeeparolus/text2excel/actions/workflows/codeql-analysis.yml/badge.svg)][myactions]

This program converts CSV Or TSV text files to Microsoft Excel format. It
uses [openpyxl] to create Excel files.

As input it takes tab-separated `*.txt` files (TSV), or any CSV files
(Comma-Separated Values) that can be auto-detected by the Python standard
library [csv] module.

* You'll find the [text2excel source on GitHub][text2excel]

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

[pipx]: https://github.com/pypa/pipx

To install or upgrade *text2excel* from [PyPI][mypypi], I recommend using [pipx]:

```bash
pipx install text2excel
pipx upgrade text2excel
```

If you don't have _pipx_, you could also use _pip_ with your preferred Python version:

```bash
python3 -m pip install --user --upgrade-strategy eager --upgrade text2excel
```

## News

Please see the [changelog](CHANGELOG.md) for more details.

## Contributing

Do you want to help out with this project?

* Please check the [CONTRIBUTING](CONTRIBUTING.md) guide.

## Credits

This project was originally based on
[a Gist by Konrad Förstner](https://gist.github.com/konrad/4154786).
