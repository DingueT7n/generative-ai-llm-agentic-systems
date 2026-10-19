"""Retrieval evaluation against the provided source-based coursework dataset."""
from __future__ import annotations

import csv
from pathlib import Path


def read_questions(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file, delimiter=";"))


def source_hit_at_k(retriever, tests: list[dict[str, str]], k: int = 3) -> dict:
    """Fraction of questions with their expected source in the top-k passages.

    This is Hit@K (or source Recall@K with a single expected source), not
    traditional Precision@K even though the original assignment uses that name.
    """
    if not tests:
        raise ValueError("Evaluation set must contain at least one question")
    details = []
    for row in tests:
        hits = retriever.search(row["question"], k=k)
        sources = list(dict.fromkeys(hit.passage.source for hit in hits))
        expected = row["document_attendu"]
        details.append({"id": row.get("id", ""), "expected": expected, "found": expected in sources, "sources": sources})
    return {"metric": f"source_hit_at_{k}", "score": sum(x["found"] for x in details) / len(details),
            "questions": len(details), "details": details}
