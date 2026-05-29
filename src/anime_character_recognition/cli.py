"""Command-line entry point."""

from __future__ import annotations

import argparse

from anime_character_recognition import __version__

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="anime_character_recognition",
        description="Recognizes anime characters.",
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
