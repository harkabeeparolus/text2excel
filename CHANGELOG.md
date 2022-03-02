# Changelog for text2excel

All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## unreleased

- Nothing yet.

## 0.4.3 - 2022-03-02

Maintenance release.

### Changed

- Updated versions of dependencies.
- Minor code and documentation cleanups.

## 0.4.2 - 2021-04-01

### Changed

- Slightly more robust paragraph text wrapping for help output. Also made
  dedenting optional.
- Improved test case, read back contents from generated xlsx file.
- Installed a default gitignore file instead of rolling my own.
- Upgraded project dependencies to latest versions.
- Fixed mypy and Pylance warnings, and added some type hints.

## 0.4.1 - 2020-07-29

### Fixed

- Correct _requirements.txt_ file, for people who still use those.

### Changed

- Prettier text wrapping for the `--help` output.
- Slightly improved test cases.
- Refactored the main cli script, for cleaner code.
- Updated to Pytest version 6.
- Compatible with Python 3.6 and up.

## 0.4.0 - 2020-07-28

### Changed

- Changed project name from _csv2xlsx_ to _text2excel_, since the former was
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

- Recommend **pre-commit** to automate code formatting and linting.

## 0.2.0 - 2020-07-24

### Added

- Tests. Running `poetry run pytest` actually does something useful now.

### Changed

- Added some more help to the command line interface.

## 0.1.0 - 2020-07-23

Initial Github release — <https://github.com/harkabeeparolus/text2excel>

### Added

- Proper Poetry project structure
- Wrote documentation; added the [README](README.md)
  and [CONTRIBUTING](CONTRIBUTING.md) files.

### Changed

- Changed the `--no-numbers` option to `--numbers`, since I almost never
  want to auto-convert numerical values.
