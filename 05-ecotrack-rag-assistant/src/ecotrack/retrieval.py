"""Approved-corpus ingestion and multilingual semantic retrieval.

Portfolio enhancement added after the unfinished 2026 course starter.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from collections.abc import Mapping


@dataclass(frozen=True)
class Passage:
    source: str
    chunk_id: str
    text: str


@dataclass(frozen=True)
class SearchHit:
    passage: Passage
    score: float


def split_into_chunks(text: str, size: int = 600, overlap: int = 100) -> list[str]:
    """Split whitespace-normalized text into fixed-length, overlapping chunks."""
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("Expected size > 0 and 0 <= overlap < size")
    normalized = " ".join(text.split())
    if not normalized:
        return []
    stride = size - overlap
    return [normalized[start:start + size] for start in range(0, len(normalized), stride)
            if normalized[start:start + size]]


def load_documents(directory: Path) -> dict[str, str]:
    """Load only .txt documents directly inside the approved folder."""
    if not directory.is_dir():
        raise FileNotFoundError(f"Corpus directory does not exist: {directory}")
    documents = {}
    for file in sorted(directory.glob("*.txt")):
        if file.is_file() and not file.is_symlink():
            documents[file.name] = file.read_text(encoding="utf-8-sig")
    if not documents:
        raise ValueError(f"No .txt documents found in {directory}")
    return documents


def build_passages(documents: Mapping[str, str], size: int = 600, overlap: int = 100) -> list[Passage]:
    passages = []
    for filename, text in sorted(documents.items()):
        for index, chunk in enumerate(split_into_chunks(text, size, overlap), start=1):
            passages.append(Passage(source=filename, chunk_id=f"{filename}#P{index:02d}", text=chunk))
    return passages


class SemanticRetriever:
    """In-memory cosine similarity over unit-normalized embedding vectors."""

    def __init__(self, passages: list[Passage], encoder):
        import numpy as np
        if not passages:
            raise ValueError("At least one passage is required")
        self.passages = passages
        self.encoder = encoder
        self.vectors = np.asarray(encoder.encode([p.text for p in passages], normalize_embeddings=True), dtype=float)
        if self.vectors.ndim != 2 or self.vectors.shape[0] != len(passages):
            raise ValueError("Encoder returned an invalid passage embedding matrix")

    def search(self, question: str, k: int = 3) -> list[SearchHit]:
        import numpy as np
        if not question.strip():
            raise ValueError("Question cannot be empty")
        if k < 1:
            raise ValueError("k must be positive")
        query_vector = np.asarray(self.encoder.encode([question], normalize_embeddings=True)[0], dtype=float)
        scores = self.vectors @ query_vector
        indexes = np.argsort(-scores, kind="stable")[:k]
        return [SearchHit(self.passages[int(i)], float(scores[int(i)])) for i in indexes]


def build_default_retriever(directory: Path) -> SemanticRetriever:
    """Download/load the multilingual embedding model lazily."""
    from sentence_transformers import SentenceTransformer
    passages = build_passages(load_documents(directory))
    model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    return SemanticRetriever(passages, model)
