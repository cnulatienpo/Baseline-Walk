import pandas as pd
from pathlib import Path

# Load the canonical dataset
src_path = Path("dataset_canonical/canonical_dataset_v1_2025-12-28T05_46_27Z.csv")
df = pd.read_csv(src_path)

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
preferred_order = [
    "file_name", "audio_path", "segment_index", "start_s", "end_s", "duration_s",
    "regime_label", "confidence"
] + [col for col in df.columns if col not in preferred_order]
df = df[preferred_order]

# Save the harmonized dataset
output_path = Path("dataset_release/canonical_v1/data/canonical_harmonized.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Harmonized dataset saved to: {output_path}")
