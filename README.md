# csv2xlsx

This program converts CSV Or TSV text files to Microsoft Excel format. It
uses [openpyxl] to create Excel files.

As input it takes tab-separated `*.txt` files (TSV), or any CSV files
(Comma-Separated Values) that can be auto-detected by the Python standard
library [csv] module.

[openpyxl]: https://openpyxl.readthedocs.io/
[csv]: https://docs.python.org/3/library/csv.html

## Example

```bash
$ printf "one\ttwo\tthree\n1\t2\t3\n" | tee my_data_file.txt
one two three
1   2   3

$ csv2xlsx --numbers my_data_file.txt
Saved to file: my_data_file.xlsx
```

## Installation

I recommend installing *csv2xlsx* with [pipx]:

```bash
pipx install git+https://github.com/harkabeeparolus/csv2xlsx.git
```

If you don't already have it, a guide for how to install _pipx_ is provided
below on this page.

To upgrade *csv2xlsx* to the latest version, simply run:

```bash
pipx upgrade csv2xlsx
```

Or `pipx upgrade-all` if you want to go crazy. 😉

If you want to bundle up *csv2xlsx* into a single, standalone executable Python
[zipapp], I highly recommend [shiv]. For example:

```bash
shiv -o csv2xlsx -p "/usr/bin/env python3" -c csv2xlsx git+https://github.com/harkabeeparolus/csv2xlsx.git
```

If _shiv_ doesn't work for you for some reason, you can also use [PEX]:

```bash
pex -o csv2xlsx -c csv2xlsx git+https://github.com/harkabeeparolus/csv2xlsx.git
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
