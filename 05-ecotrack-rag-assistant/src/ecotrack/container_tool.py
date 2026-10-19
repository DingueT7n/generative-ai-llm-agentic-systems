"""Read-only synthetic container status lookup (tool-use bonus)."""
from __future__ import annotations
import csv
from pathlib import Path


def container_status_by_zone(path: Path, zone: str) -> list[dict[str, str]]:
    if not zone.strip():
        raise ValueError("Zone is required")
    with path.open(encoding="utf-8-sig", newline="") as file:
        rows = list(csv.DictReader(file, delimiter=";"))
    return [dict(row) for row in rows if row["zone"].casefold() == zone.strip().casefold()]
