"""
src/utils.py - Shared utility functions for the NFL Super Bowl Prediction Project
"""

import pandas as pd
from pathlib import Path


def ensure_dir(path: str) -> Path:
    """
    Create directory if it doesn't exist. Returns the Path object.
    Used across notebooks to guarantee outputs/ and data/processed/ exist.
    """
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def evaluate_top_k(df: pd.DataFrame, k: int) -> tuple:
    """
    Evaluate whether the actual Super Bowl winner appears in top-K ranked teams
    by predicted probability.
    
    Shared across cleaning/modeling workflows to ensure consistent evaluation.
    
    Parameters
    ----------
    df : pd.DataFrame
        Must contain 'year', 'super_bowl_winner', and 'predicted_probability'
    k : int
        Number of top-ranked teams to check per year
        
    Returns
    -------
    tuple: (correct, total, accuracy)
    """
    correct = 0
    total = 0

    for year in df["year"].unique():
        year_df = df[df["year"] == year].sort_values(
            by="predicted_probability", ascending=False
        )
        top_k = year_df.head(k)
        
        if top_k["super_bowl_winner"].sum() > 0:
            correct += 1
        total += 1

    return correct, total, correct / total