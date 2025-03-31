# {{cookiecutter.app_name}}

{{cookiecutter.project_short_description}}

## Installation

### For Users

```bash
# Using pip
pip install {{cookiecutter.app_name}}

# Using uv (recommended)
uv pip install {{cookiecutter.app_name}}
```

### For Developers

We use modern Python packaging with `pyproject.toml` and `uv` for dependency management. Most development tasks are automated in the `Makefile`:

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install development dependencies
make install-dev

# Run tests
make test

# Run tests with coverage
make test-cov

# Run linting
make lint

# Fix linting issues
make lint-fix

# Run type checking
mypy {{cookiecutter.app_name}}

# Build package
make build

# Build documentation
make docs

# Clean build artifacts
make clean
```

## Development Tools

This project uses:

- [uv](https://github.com/astral-sh/uv) for fast, reliable Python packaging
- [pytest](https://docs.pytest.org/) for testing
- [ruff](https://github.com/astral-sh/ruff) for fast Python linting
- [black](https://github.com/psf/black) for code formatting
- [mypy](https://mypy.readthedocs.io/) for static type checking
- [tox](https://tox.wiki/) for test automation
- [GitHub Actions](https://github.com/features/actions) for CI/CD

## License

MIT License - see LICENSE.md for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.