#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import dotenv
import os
from pathlib import Path


def main():

    BASE_DIR = Path(__file__).resolve().parent.parent

    dotenv_path = BASE_DIR / '.env'
    dotenv.read_dotenv(dotenv_path)

    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'freelance_app.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHON PATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
