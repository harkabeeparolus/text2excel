"Python package file for csv2xlsx."
# source: https://packaging.python.org/guides/single-sourcing-package-version/
try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata

version = metadata.version("csv2xlsx")
