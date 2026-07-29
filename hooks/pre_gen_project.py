"""Validate Cookiecutter answers before the project is generated."""

import keyword
import sys

APP_NAME = {{ cookiecutter.app_name | jsonify }}


def main() -> None:
    """Reject app_name values that cannot be used as a Python package."""
    if (
        not APP_NAME.isascii()
        or not APP_NAME.isidentifier()
        or keyword.iskeyword(APP_NAME)
    ):
        sys.stderr.write(
            f"ERROR: app_name {APP_NAME!r} is not a valid Python package name.\n"
            "It is used as both the import package and the distribution name, so "
            "it must be a valid Python identifier: ASCII letters, digits and "
            "underscores only, not starting with a digit, and not a Python "
            "keyword. For example: 'mypippkg' or 'my_package'.\n"
        )
        raise SystemExit(1)


main()
