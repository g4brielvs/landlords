from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("landlords")
except PackageNotFoundError:
    # package is not installed
    pass
