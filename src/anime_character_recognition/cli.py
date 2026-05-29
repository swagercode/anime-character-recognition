"""Command-line entry point."""

from __future__ import annotations

import argparse

from guh_logs_auto_processing import __version__
from guh_logs_auto_processing import classifier

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="guh-logs",
        description="Process GUH log files.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    classify_parser = subparsers.add_parser("classify")
    classify_parser.add_argument("--image", required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command == "classify":
        print(classification)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
