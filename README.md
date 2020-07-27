# Convert CSV Or TSV to Excel Files

This program uses [openpyxl] to create Excel files.

As input it takes tab-separated `*.txt` files (TSV), or any CSV files
(Comma-Separated Values) that can be auto-detected by the Python standard
library [csv] module.

[openpyxl]: https://openpyxl.readthedocs.io/
[csv]: https://docs.python.org/3/library/csv.html
[shiv]: https://github.com/linkedin/shiv
[pipx]: https://github.com/pipxproject/pipx/

## Example

```bash
$ printf "one\ttwo\tthree\n1\t2\t3\n" | tee my_data_file.txt
one two three
1   2   3

$ csv2xlsx --numbers my_data_file.txt
Saved to file: my_data_file.xlsx
```

## Installation

I suggest installing this package with [shiv], for example:

```bash
git clone https://github.com/harkabeeparolus/csv2xlsx.git
shiv -p "/usr/bin/env python3" -c csv2xlsx -o ~/bin/csv2xlsx ./csv2xlsx
```

## Getting shiv

If you don't have [shiv] installed, I suggest getting it with [pipx]. In
fact, I suggest installing everything with pipx, because it is fantastic. 🙂

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

At this point, you may need to logout to refresh your shell `$PATH` before
proceeding.

```bash
pipx install shiv
```

Alternatively, if you really don't want to use pipx for some reason, you can
simply run `python3 -m pip install --user shiv`, and if necessary, manually
reconfigure your shell `$PATH` to find any pip installed binaries.

## News

Please see the [changelog](CHANGELOG.md) for more details.

## Contributing

Do you want to help out with this project?

* Please check the [CONTRIBUTING](CONTRIBUTING.md) guide.

## Credits

This project was originally based on
[a Gist by Konrad Förstner](https://gist.github.com/konrad/4154786).
