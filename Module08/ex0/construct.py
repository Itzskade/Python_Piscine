#!/usr/bin/env python3

import sys
import os
import site


def main() -> None:
    """Detect and display the current Python environment status."""
    in_venv = sys.prefix != sys.base_prefix

    if not in_venv:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate # On Windows\n")
        print("Then run this program again.")
    else:
        venv_path = sys.prefix
        venv_name = os.path.basename(venv_path)

        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv_path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without "
              "affecting the global system.\n")

        try:
            path = site.getsitepackages()
            if path:
                print(f"Package installation path:\n {path[0]}")
            else:
                print("Package installation path: (No site-package found)")
        except Exception:
            print("Package installation path: (Unable to determine)")


if __name__ == "__main__":
    main()
