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

    print("🙆 All UIs compiled!")


@task
def clean(c: Context):
    """Cleans up this project generated files"""
    patterns = [
        PYTHON_UI_DIR,
    ]

    for pattern in patterns:
        c.run(f"rm -rf {pattern}")

    print("🙆 Clean up complete!")
