# Contributing to csv2xlsx

Please feel free to send a pull request.  🙂

Make sure to read the [README](README.md) for general installation
instructions.

* To edit the source code, make sure to install into a virtual environment!

There are some __TODO:__ comments in the source that indicate a wishlist of
sorts, or planned upcoming features.

## Git

I will assume that you are using a personal `~/.config/git/ignore` to avoid
checking in your editor or IDE files. If you are not certain what this means,
please check the well-written guide here:

* [Properly managing your .gitignore file][gitignore]
  by Julien Danjou, 2 Dec 2019

[gitignore]: https://julien.danjou.info/properly-managing-your-gitignore/

## Package Dependencies

Use [Poetry] to install and manage your virtual environments:

```bash
mkdir .venv
poetry install
```

[Poetry]: https://python-poetry.org

To upgrade the packages to the latest versions, and generate a new
*requirements.txt*, simply:

```bash
poetry update
poetry export -f requirements.txt >requirements.txt
```

Make sure to run `pytest`, and then check in:

* pyproject.toml
* poetry.lock
* requirements.txt

## Coding Style

You can use any coding style you want, as long as it's [Black]. 😉

[Black]: https://black.readthedocs.io/

## Code Quality

Use pylint, flake8 and black before checking in your code.

```bash
black csv2xlsx
poetry run pylint csv2xlsx
flake8 csv2xlsx
```

* I should probably add this as a Git pre-commit hook, but I haven't
  yet done so.

* After that, I should also setup automated testing with
  [tox](https://tox.readthedocs.io/)
  or [nox](https://github.com/theacodes/nox)

## Getting Python Software with pipx

Use [pipx] for everything -- pipx is great! 🌟

[pipx]: https://pipxproject.github.io/pipx/

Either follow the official
[_installation guide_](https://pipxproject.github.io/pipx/installation/),
or just run:

```bash
python3 -m pip install --user --upgrade-strategy eager --upgrade pipx
python3 -m pipx ensurepath
```

Then you can install stuff such as **pipenv**, **black** or **shiv** using
pipx!

```bash
pipx install pipenv
pipx install black
pipx install pylint
pipx install flake8
pipx install shiv
```

To automagically upgrade all your pipx packages, run:

```bash
pipx upgrade-all
```

And if you are having trouble 💣, such as after a Python major version
upgrade, just reinstall:

```bash
pipx reinstall-all
```

### Upgrading pipx (and Other PyPI Packages)

To see if you have any outdated pip packages that need upgrading, run:

```bash
python3 -m pip list --outdated
```

Then, if necessary, to upgrade **pipx** itself, just re-run:

```bash
python3 -m pip install --user --upgrade-strategy eager --upgrade pipx
```

Also, you should upgrade **pip** itself this way, or **setuptools**, whenever
there is a newer version.
