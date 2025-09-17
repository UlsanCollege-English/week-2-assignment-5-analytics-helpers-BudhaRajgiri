# src/analytics.py

from typing import List, Optional


def chunk(lst: List[int], size: int) -> List[List[int]]:
    if size <= 0:
        raise ValueError("Chunk size must be greater than 0.")
    return [lst[i:i + size] for i in range(0, len(lst), size)]


def running_total(start: int, changes: List[int]) -> List[int]:
    result = []
    total = start
    for change in changes:
        total += change
        result.append(total)
    return result


def index_of_first_at_least(lst: List[int], threshold: int) -> Optional[int]:
    for i, value in enumerate(lst):
        if value >= threshold:
            return i
    return None
