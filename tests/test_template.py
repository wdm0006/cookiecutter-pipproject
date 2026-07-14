"""Regression tests for rendering the Cookiecutter template."""

import tempfile
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


if __name__ == "__main__":
    unittest.main()
