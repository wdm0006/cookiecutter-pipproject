"""Regression tests for rendering the Cookiecutter template."""

import configparser
import tempfile
import tomllib
import unittest
from pathlib import Path

from cookiecutter.main import cookiecutter


class TemplateRenderTest(unittest.TestCase):
    """Verify the template can be rendered with its default inputs."""

    def test_default_render_preserves_github_token_expression(self) -> None:
        """Render defaults and retain the GitHub Actions secret expression."""
        template_dir = Path(__file__).resolve().parents[1]

        with tempfile.TemporaryDirectory() as output_dir:
            project_dir = Path(
                cookiecutter(str(template_dir), no_input=True, output_dir=output_dir)
            )
            docs_workflow = project_dir / ".github" / "workflows" / "docs.yml"

            self.assertIn("${{ secrets.GITHUB_TOKEN }}", docs_workflow.read_text())

    def test_default_render_has_consistent_python_support(self) -> None:
        """Keep package metadata, tools, tox, and CI on the supported range."""
        template_dir = Path(__file__).resolve().parents[1]

        with tempfile.TemporaryDirectory() as output_dir:
            project_dir = Path(
                cookiecutter(str(template_dir), no_input=True, output_dir=output_dir)
            )
            config = tomllib.loads((project_dir / "pyproject.toml").read_text())
            classifiers = config["project"]["classifiers"]
            python_classifiers = {
                classifier.removeprefix("Programming Language :: Python :: ")
                for classifier in classifiers
                if classifier.startswith("Programming Language :: Python :: 3.")
            }
            tox_config = config["tool"]["tox"]["legacy_tox_ini"]
            workflow = (project_dir / ".github" / "workflows" / "test.yml").read_text()
            tox = configparser.ConfigParser()
            tox.read_string(tox_config)
            tox_environments = tox["tox"]["env_list"].split()

            self.assertEqual(config["project"]["requires-python"], ">=3.12")
            self.assertEqual(python_classifiers, {"3.12", "3.13", "3.14"})
            self.assertEqual(config["tool"]["ruff"]["target-version"], "py312")
            self.assertEqual(config["tool"]["mypy"]["python_version"], "3.12")
            self.assertEqual(
                tox_environments, ["py312", "py313", "py314", "lint", "type"]
            )
            self.assertIn("python-version: ['3.12', '3.14']", workflow)
            self.assertEqual(workflow.count("make test"), 1)
            self.assertEqual(workflow.count("make lint"), 1)
            for workflow_path in (project_dir / ".github" / "workflows").glob("*.yml"):
                workflow_text = workflow_path.read_text()
                for unsupported in ("'3.8'", "'3.9'", "'3.10'", "'3.11'"):
                    self.assertNotIn(unsupported, workflow_text)


if __name__ == "__main__":
    unittest.main()
