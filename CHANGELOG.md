# Changelog for text2excel

All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## unreleased

- Nothing yet

## 0.4.0 - 2020-07-28

### Changed

- Changed project name from *csv2xlsx* to *text2excel*, since the former was
  not available on PyPI.

## 0.3.1 - 2020-07-27

### Changed

- Single-source package version number from _pyproject.toml_, instead of
  manually duplicating it in several different places.

## 0.3.0 - 2020-07-27

### Added

- Handle multiple input files from the command line, instead of just one.
- pytest: Test that an output file is actually created.
  (No tests yet for correct file contents, however.)

### Changed

- Recommend __pre-commit__ to automate code formatting and linting.

## 0.2.0 - 2020-07-24

### Added

- Tests. Running `poetry run pytest` actually does something useful now.

### Changed

- Added some more help to the command line interface.

## 0.1.0 - 2020-07-23

Initial Github release — <https://github.com/harkabeeparolus/csv2xlsx>

### Added

- Proper Poetry project structure
- Wrote documentation; added the [README](README.md)
  and [CONTRIBUTING](CONTRIBUTING.md) files.

### Changed

- Changed the `--no-numbers` option to `--numbers`, since I almost never
  want to auto-convert numerical values.
