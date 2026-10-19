import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from ecotrack.retrieval import Passage, SemanticRetriever, load_documents, build_passages, split_into_chunks
from ecotrack.evaluation import source_hit_at_k
from ecotrack.container_tool import container_status_by_zone


class TinyEncoder:
    """Deterministic encoder to test ranking without downloading a model."""
    def encode(self, texts, normalize_embeddings=True):
        import numpy as np
        def embed(text):
            words = text.casefold()
            vec = np.array([int("verre" in words), int("nord" in words), int("critique" in words)], dtype=float)
            return vec / max(np.linalg.norm(vec), 1)
        return np.stack([embed(t) for t in texts])


class TestEcoTrack(unittest.TestCase):
    def test_chunking_preserves_overlap(self):
        chunks = split_into_chunks("abcdefghij", size=6, overlap=2)
        self.assertEqual(chunks, ["abcdef", "efghij", "ij"])

    def test_chunking_rejects_invalid_parameters(self):
        with self.assertRaises(ValueError): split_into_chunks("hello", size=2, overlap=2)

    def test_loads_documents_only_from_given_directory(self):
        with TemporaryDirectory() as td:
            path = Path(td)
            (path / "a.txt").write_text("verre et bac", encoding="utf-8")
            (path / "not-a-txt.csv").write_text("ignored", encoding="utf-8")
            docs = load_documents(path)
            self.assertEqual(list(docs), ["a.txt"])
            passages = build_passages(docs)
            self.assertEqual(passages[0].chunk_id, "a.txt#P01")

    def test_search_ranking_and_metric(self):
        samples = [Passage("a.txt", "a.txt#P01", "verre"), Passage("b.txt", "b.txt#P01", "nord")]
        retriever = SemanticRetriever(samples, TinyEncoder())
        self.assertEqual(retriever.search("verre", k=1)[0].passage.source, "a.txt")
        report = source_hit_at_k(retriever, [{"id":"Q1","question":"verre","document_attendu":"a.txt"}], k=1)
        self.assertEqual(report["score"], 1.0)
        self.assertEqual(report["metric"], "source_hit_at_1")

    def test_missing_question_is_rejected(self):
        retriever = SemanticRetriever([Passage("a.txt", "a.txt#P01", "verre")], TinyEncoder())
        with self.assertRaises(ValueError):retriever.search("")

    def test_read_only_container_lookup(self):
        data = Path(__file__).resolve().parents[1] / "data" / "etat_conteneurs.csv"
        matches = container_status_by_zone(data, " nord ")
        self.assertTrue(matches)
        self.assertTrue(all(row["zone"]=="Nord" for row in matches))

    def test_injected_document_not_in_default_corpus(self):
        corpus=Path(__file__).resolve().parents[1] / "data" / "corpus_ecotrack"
        documents=load_documents(corpus)
        self.assertNotIn("bonus_document_injection.txt", documents)


if __name__=="__main__": unittest.main()
