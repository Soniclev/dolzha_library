from datetime import timedelta
from typing import Sequence


def compute_duration(*durations: Sequence[timedelta]) -> timedelta:
    """Computes total duration of sequence of timedelta"""
    total_seconds = sum(map(timedelta.total_seconds, durations))
    return timedelta(seconds=total_seconds)
