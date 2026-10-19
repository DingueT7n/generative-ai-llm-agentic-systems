"""Run using python -m ecotrack after pip install -e ."""
from __future__ import annotations
import argparse
from pathlib import Path
from .container_tool import container_status_by_zone
from .retrieval import build_default_retriever
from .evaluation import read_questions, source_hit_at_k
from .generation import grounded_answer

DATA = Path(__file__).resolve().parents[2] / "data"


def main() -> None:
    parser = argparse.ArgumentParser(description="EcoTrack coursework retrieval and evaluation")
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument("--question", help="Query the approved EcoTrack text corpus")
    actions.add_argument("--evaluate", action="store_true", help="Evaluate expected source Hit@3")
    actions.add_argument("--zone", help="Read the synthetic container states for a zone")
    parser.add_argument("--generate", action="store_true", help="Call Gemini to compose a grounded answer")
    parser.add_argument("--threshold", type=float, default=0.35)
    args = parser.parse_args()
    if args.generate and not args.question:
        parser.error("--generate requires --question")
    if args.zone:
        results = container_status_by_zone(DATA / "etat_conteneurs.csv", args.zone)
        if not results:
            print("No containers found for this zone")
        for row in results:
            print(" | ".join(f"{k}={v}" for k, v in row.items()))
        return
    retriever = build_default_retriever(DATA / "corpus_ecotrack")
    if args.evaluate:
        summary = source_hit_at_k(retriever, read_questions(DATA / "jeu_test_10_questions.csv"))
        print(f"Source Hit@3: {summary['score']:.1%} over {summary['questions']} test questions")
        for row in summary["details"]:
            print(f"{row['id']}: {'PASS' if row['found'] else 'MISS'} expected={row['expected']} retrieved={row['sources']}")
        return
    hits = retriever.search(args.question)
    print("\nRetrieved evidence:")
    for h in hits:
        print(f"- [{h.passage.chunk_id}] similarity={h.score:.3f}: {h.passage.text[:220]}...")
    if args.generate:
        print("\nGrounded response (verify citations):\n" + grounded_answer(args.question, hits, args.threshold))
    elif hits[0].score < args.threshold:
        print("\nLow-confidence retrieval: the assistant should abstain or request clarification.")


if __name__ == "__main__":
    main()
