"""Command-line interface for baselinewalk."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create the top-level parser for the baselinewalk CLI."""
    parser = argparse.ArgumentParser(
        prog="baselinewalk",
        description="Ambient audio segment harmonizer and baseline comparison CLI tool",
    )
    subparsers = parser.add_subparsers(dest="command")

    harmonize = subparsers.add_parser(
        "harmonize",
        help="Harmonize ambient audio segments against baseline references.",
    )
    harmonize.add_argument(
        "--input",
        help="Path to the input dataset or audio segment file.",
    )
    harmonize.add_argument(
        "--baseline",
        help="Path to baseline reference data.",
    )
    harmonize.add_argument(
        "--output",
        help="Path to write harmonized output.",
    )

    return parser


def main() -> int:
    """Entry point for the baselinewalk command-line interface."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "harmonize":
        print("Running harmonize...")
        if args.input:
            print(f"Input: {args.input}")
        if args.baseline:
            print(f"Baseline: {args.baseline}")
        if args.output:
            print(f"Output: {args.output}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
