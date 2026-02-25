# Canonical Acoustic Regime Dataset v1.0

## Overview

This dataset captures the **structural acoustic behavior of real-world environments** using a nested, multi-layer analysis pipeline.

Rather than labeling sounds by semantic category (e.g. speech, music, noise), the dataset describes **how sound behaves over time**—its energy, texture, stability, and transitions—at multiple resolutions.

The canonical dataset represents **fixed-duration acoustic chunks (~30 seconds)**, each enriched with signal-level truth and temporal context.

## Unit of Observation

- **One row = one fixed-duration audio chunk**
- Chunks are derived from continuous field recordings
- Chunk boundaries are mechanical, not semantic

## Data Sources

- Source audio: long-form `.m4a` field recordings
- Audio is treated as immutable ground truth
- No audio is modified during analysis

## Feature Layers (Nested Design)

This dataset is derived from multiple nested analysis layers:

- **Layer 0**: Raw audio existence
- **Layer 1**: Container metadata
- **Layer 2**: Signal truth (duration, silence ratios)
- **Layer 3**: Acoustic regimes (chunk-level texture)
- **Layer 4**: Temporal volatility (file-level context)

The canonical dataset joins Layers 2–4 onto the chunk-level regime layer.

## Columns

- **file** (`object`)
- **chunk_index** (`int64`)
- **t_start_sec** (`float64`)
- **t_end_sec** (`float64`)
- **bursty** (`bool`)
- **wideband** (`bool`)
- **rms_variance** (`float64`)
- **spectral_flatness** (`float64`)
- **spectral_bandwidth** (`float64`)
- **spectral_centroid** (`float64`)
- **file_duration_sec** (`float64`)
- **file_silence_ratio** (`float64`)
- **file_volatility** (`float64`)

## What This Dataset Is

- A **structural description** of acoustic environments
- A dataset designed for **representation learning**
- Suitable for unsupervised, self-supervised, or weakly supervised models
- Compatible with nested or curriculum learning approaches

## What This Dataset Is Not

- Not a speech recognition dataset
- Not a sound event classification dataset
- Not semantically labeled
- Not intended for direct human annotation

## Intended Uses

- Learning acoustic representations
- Studying environmental sound structure
- Training models to handle ambiguity and regime shifts
- Benchmarking robustness on non-semantic audio

## Known Limitations

- Acoustic regimes are heuristic, not ground truth
- Chunk boundaries may cut across events
- Silence is energy-based, not perceptual
- Dataset reflects the biases of recording conditions

## Reproducibility

- All features are derived from immutable lower layers
- Processing is deterministic given the same parameters
- Checkpoints and intermediate artifacts are preserved

## Ethics & Privacy

- No transcription is performed
- No semantic labeling of speech
- Dataset focuses on structure, not content
- Intended to minimize personal data exposure

## Citation

If you use this dataset, cite it as:

`Canonical Acoustic Regime Dataset v1.0 (2025)`

