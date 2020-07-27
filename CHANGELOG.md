# Changelog for csv2xlsx

All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## unreleased

### Added

- Handle multiple input files from the command line, instead of just one.
- pytest: Test that an output file is created.

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
