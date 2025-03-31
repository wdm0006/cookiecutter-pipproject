# Modern Python Project Template 🐍

A modern, production-ready cookiecutter template for Python packages that follows best practices. This template sets up a complete development environment with all the tools you need to build, test, and publish professional Python libraries.

## Features

### 📦 Modern Python Packaging
- **pyproject.toml**: Uses the modern Python packaging standard ([PEP 517](https://peps.python.org/pep-0517/)/[PEP 621](https://peps.python.org/pep-0621/))
- **[Hatch](https://hatch.pypa.io/)**: Fast, modern project management and build tool
- **[uv](https://github.com/astral-sh/uv)**: Ultra-fast Python package installer and resolver
- Automatic version management
- Development and production dependency separation
- Proper package metadata and classifiers

### 🧪 Testing & Quality Assurance
- **[pytest](https://docs.pytest.org/)**: Modern testing framework
- **[tox](https://tox.wiki/)**: Automated testing across Python versions
- **[Coverage.py](https://coverage.readthedocs.io/)**: Code coverage tracking
- Configured for both unit and integration tests
- Test fixtures and helpers included

### 📝 Code Quality Tools
- **[ruff](https://github.com/astral-sh/ruff)**: Ultra-fast Python linter and formatter
  - Code style enforcement (PEP 8)
  - Import sorting
  - Dead code detection
  - Best practice enforcement
- **[mypy](https://mypy.readthedocs.io/)**: Static type checking
- Pre-configured with sensible defaults
- Easy to customize rules

### 📚 Documentation
- **[Sphinx](https://www.sphinx-doc.org/)**: Professional documentation generator
- **ReadTheDocs** theme
- Automatic API documentation
- Versioned documentation support
- Example documentation included

### 🔄 CI/CD Automation
- **GitHub Actions** workflows for:
  - Testing across Python versions
  - Code quality checks
  - Documentation builds
  - Automated PyPI releases
  - Security scanning
- **Codecov** integration for coverage reporting
- Automated dependency updates

### 🤝 Community & Contribution Tools
- Structured issue templates for:
  - Bug reports
  - Feature requests
  - Documentation improvements
- Pull request template
- Contributing guidelines
- Code of conduct
- Security policy
- Support resources

### 🛠️ Development Workflow
- **Makefile** with common development commands:
  ```bash
  make install-dev    # Install development dependencies
  make test          # Run tests
  make lint          # Check code quality
  make format        # Format code
  make docs          # Build documentation
  make clean         # Clean build artifacts
  ```
- **pre-commit** hooks for code quality
- VS Code/PyCharm configurations
- Debug configurations

## Quick Start

1. Install Cookiecutter:
   ```bash
   pip install cookiecutter
   ```

2. Create your project:
   ```bash
   cookiecutter gh:{{cookiecutter.github_username}}/cookiecutter-pipproject
   ```

3. Initialize your development environment:
   ```bash
   cd your-project-name
   curl -LsSf https://astral.sh/uv/install.sh | sh  # Install uv
   make install-dev
   ```

4. Start developing:
   ```bash
   # Run tests
   make test

   # Check code quality
   make lint

   # Format code
   make format

   # Build docs
   make docs
   ```

## Why These Tools?

### Modern Packaging (pyproject.toml + hatch + uv)
- **Why**: Traditional `setup.py` is being phased out in favor of declarative configuration
- **Benefits**: 
  - Cleaner, more maintainable package configuration
  - Faster, more reliable dependency resolution
  - Better reproducibility
  - Improved build isolation

### Code Quality (ruff + mypy)
- **Why**: Python's dynamic nature requires strong tooling to catch issues early
- **Benefits**:
  - Catch bugs before they reach production
  - Maintain consistent code style
  - Improve code maintainability
  - Speed up code reviews
  - Ultra-fast performance (Rust-based tools)

### Testing (pytest + tox)
- **Why**: Comprehensive testing across environments is crucial for libraries
- **Benefits**:
  - Ensure compatibility across Python versions
  - Isolate tests from system dependencies
  - Parallel test execution
  - Rich plugin ecosystem

### CI/CD (GitHub Actions)
- **Why**: Automation is key to maintaining quality and velocity
- **Benefits**:
  - Catch issues early
  - Ensure quality on every change
  - Automate releases
  - Reduce manual work
  - Build trust with users

### Documentation (Sphinx)
- **Why**: Good documentation is crucial for library adoption
- **Benefits**:
  - Professional-looking documentation
  - API documentation from docstrings
  - Versioned documentation
  - Search functionality
  - Multiple output formats

## Template Updates

This template is actively maintained and regularly updated with the latest Python best practices. Key updates include:

- 🔄 Regular dependency version updates
- 🔒 Security patches and updates
- 🛠️ New tool integrations
- 📚 Documentation improvements
- 🐛 Bug fixes

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

This template builds on the work of many in the Python community and incorporates modern best practices from various sources. Special thanks to:
- [Python Packaging Authority](https://www.pypa.io/)
- [Astral](https://astral.sh/) for uv and ruff
- [pytest](https://docs.pytest.org/) team
- [GitHub](https://github.com/) for Actions and security tools