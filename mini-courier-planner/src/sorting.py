from typing import List, Tuple
from models import Parcel


def _priority_key(parcel: Parcel) -> Tuple[int, int, int]:
    """
    Primary sort by urgency (priority_tier ascending),
    secondary sort by tighter deadline (deadline_hours ascending),
    tertiary sort by higher value (-value).
    """
    return (parcel.priority_tier, parcel.deadline_hours, -parcel.value)


def merge_sort_parcels(parcels: List[Parcel]) -> List[Parcel]:
    """
    Stable O(n log n) Merge Sort to prioritize parcels before packing.
    """
    if len(parcels) <= 1:
        return list(parcels)

    mid = len(parcels) // 2
    left = merge_sort_parcels(parcels[:mid])
    right = merge_sort_parcels(parcels[mid:])
    return _merge(left, right)


def _merge(left: List[Parcel], right: List[Parcel]) -> List[Parcel]:
    merged: List[Parcel] = []
    i = j = 0

    while i < len(left) and j < len(right):
        if _priority_key(left[i]) <= _priority_key(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
