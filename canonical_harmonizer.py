import argparse
from pathlib import Path

import pandas as pd


DEFAULT_INPUT_PATH = Path("dataset_canonical/canonical_dataset_v1_2025-12-28T05_46_27Z.csv")
DEFAULT_OUTPUT_PATH = Path("dataset_release/canonical_v1/data/canonical_harmonized.csv")


def main() -> None:
    parser = argparse.ArgumentParser(description="Harmonize canonical dataset CSV fields.")
    parser.add_argument(
        "input_csv",
        nargs="?",
        default=DEFAULT_INPUT_PATH,
        type=Path,
        help=f"Input CSV path (default: {DEFAULT_INPUT_PATH})",
    )
    parser.add_argument(
        "output_csv",
        nargs="?",
        default=DEFAULT_OUTPUT_PATH,
        type=Path,
        help=f"Output CSV path (default: {DEFAULT_OUTPUT_PATH})",
    )
    args = parser.parse_args()

    # Load the canonical dataset
    df = pd.read_csv(args.input_csv)

    # Rename fields to canonical names
    rename_map = {
        "t_start_sec": "start_s",
        "t_end_sec": "end_s",
        "file": "file_name",
        # Optional harmonization
        "chunk_index": "segment_index",
    }
    df = df.rename(columns=rename_map)

    # Add missing expected fields (with defaults or inferred values)
    if "duration_s" not in df.columns:
        df["duration_s"] = df["end_s"] - df["start_s"]

    if "regime_label" not in df.columns:
        df["regime_label"] = "unlabeled"

    if "confidence" not in df.columns:
        df["confidence"] = 1.0  # default full confidence for now

    if "audio_path" not in df.columns:
        df["audio_path"] = df["file_name"].apply(lambda x: f"audio/{x}")

    # Reorder columns if desired
    preferred_order_base = [
        "file_name",
        "audio_path",
        "segment_index",
        "start_s",
        "end_s",
        "duration_s",
        "regime_label",
        "confidence",
    ]
    preferred_order = preferred_order_base + [
        col for col in df.columns if col not in preferred_order_base
    ]
    df = df[preferred_order]

    # Save the harmonized dataset
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output_csv, index=False)

    print(f"Harmonized dataset saved to: {args.output_csv}")
    print(f"DataFrame shape: {df.shape}")
    print("First 3 rows:")
    print(df.head(3))


if __name__ == "__main__":
    main()
