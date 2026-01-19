#!/usr/bin/env python3

import sys
import importlib
from typing import Tuple

REQUIRED_PACKAGES = ['pandas', 'requests', 'matplotlib']


def check_packages(package_name) -> Tuple[bool, str]:
    """
    Check if a package is installed and
    return its status and version.
    """
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'unknown')
        return True, version
    except ImportError:
        return False, 'not installed'
    except Exception as e:
        return False, f'error: {e}'


def main() -> None:
    """
    Check dependencies, test connection,
    and generate pill choice chart.
    """
    print("LOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    all_ok = True

    info = {
            'pandas': 'Data manipulation ready',
            'requests': 'Network access ready',
            'matplotlib': 'Visualization ready'
            }

    for pkg in REQUIRED_PACKAGES:
        ok, version = check_packages(pkg)
        status = '[OK]' if ok else '[MISSING]'
        if ok:
            print(f"{status} {pkg} ({version}) - {info.get(pkg, 'ready')}")
        else:
            print(f"{status} {pkg} ({version})")
            all_ok = False

    if not all_ok:
        print("\nERROR: Missing necessary packages.")
        print("Pip install: pip install -r requirements.txt")
        print("Poetry install: poetry install")
        sys.exit(1)

    import pandas as pd
    import requests
    import matplotlib.pyplot as plt

    try:
        response = requests.get("https://www.python.org")
        print(f"Connection established: Status code -> {response.status_code}")
    except Exception as e:
        print("Connection failed: ", e)

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")
    data = {
            'Pill': ['Blue', 'Red'],
            'Agent Choice': [720, 280]
            }
    chart = pd.DataFrame(data)
    print(chart)

    print("Generating visualization...")
    colors = ['blue', 'red']

    plt.bar(chart['Pill'], chart['Agent Choice'], color=colors)
    plt.title("Choice of pills in 1000 agents")
    plt.ylabel("Number of agents")
    plt.xlabel("Pill chosen")
    plt.ylim(0, 1000)
    plt.savefig("matrix_pills.png")
    print("Saved as matrix_pills.png")


if __name__ == '__main__':
    main()
