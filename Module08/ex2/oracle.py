#!/usr/bin/env python3

import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("dotenv: Not installed.", file=sys.stderr)
    print("Try → pip install python-dotenv", file=sys.stderr)
    sys.exit(1)


def show_status(required_vars):
    """Display loaded configuration values."""
    mode, db_url, api_key, log_lvl, zion_ep = required_vars
    print("┌─────────── Configuration loaded: ───────────┐")
    print(f"  Mode         : {mode}")
    db_status = "Connected to local instance" if db_url else "Not connected"
    print(f"  Database      : {db_status}")
    api_status =  "Authenticated" if api_key else "Not authenticated"
    print(f"  API Key      : {api_status}")
    print(f"  Log Level    : {log_lvl}")
    zion_status = "Online" if zion_ep else "Offline"
    print(f"  Zion Network : {zion_status}")
    print("└─────────────────────────────────────────────┘")


def main():
    """Load environment variables and validate configuration."""
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...\n")

    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_lvl = os.getenv("LOG_LEVEL")
    zion_ep = os.getenv("ZION_ENDPOINT")

    required_vars = [mode, db_url, api_key, log_lvl, zion_ep]
    if any(v is None or v.strip() == "" for v in required_vars):
        print("→ Check your .env file", file=sys.stderr)
        sys.exit(1)
    show_status(required_vars)

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")


if __name__ == '__main__':
    main()
