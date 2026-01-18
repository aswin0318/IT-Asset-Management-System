from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from xhtml2pdf import pisa


BASE_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = BASE_DIR / "templates"

env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))


def render_pdf(template_name: str, context: dict, output_path: str):
    template = env.get_template(template_name)
    html = template.render(**context)

    with open(output_path, "wb") as result_file:
        pisa.CreatePDF(
            src=html,
            dest=result_file
        )
