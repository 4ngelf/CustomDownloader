from pathlib import Path

from invoke.context import Context
from invoke.tasks import task

BASE_DIR = Path(__file__).parent

UI_DIR = BASE_DIR / "ui"

PYTHON_SRC_DIR = BASE_DIR / "src" / "downloader"
PYTHON_UI_DIR = PYTHON_SRC_DIR / "ui"


@task
def uic(c: Context):
    """Compiles UIs build in Qt Designer"""
    PYTHON_UI_DIR.mkdir(parents=True, exist_ok=True)
    for input_f in UI_DIR.glob("*.ui"):
        output_f = PYTHON_UI_DIR / f"{input_f.stem}_ui.py"
        c.run(f"pyside6-uic -o {output_f} {input_f}")

    print("🧪 All UIs compiled!")


@task(help={"cache": "Also cleans this project cache"})
def clean(c: Context, cache: bool = False):
    """Cleans up this project generated files"""
    patterns = [
        PYTHON_UI_DIR,
    ]

    if cache:
        patterns.append(BASE_DIR / "**/__pycache__")
        patterns.append(BASE_DIR / ".pytest_cache")

    for pattern in patterns:
        c.run(f"rm -rf {pattern}")
    print("🧹 Clean up complete!")


@task(clean, uic)
def prepare(c: Context):
    """Prepare the project for distribution"""
    print("🙆 All preparations completed!")
