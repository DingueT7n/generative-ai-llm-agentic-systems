# EcoTrack AI Assistant — Document-grounded RAG

> **INGETIS · 2026–2027**  
> **Student / portfolio maintainer:** Mohammed Alaa Eddine GUERBOUZ  
> **Original status:** unfinished educational starter notebook  
> **Portfolio enhancement:** a separate, runnable retrieval/evaluation implementation with tests

## 1. Problem and realistic use case

Municipal recycling users ask practical questions: *When is the bin critical?*, *Which waste stream accepts glass?*, *When does collection take place?*, or *How do citizens report an overflowing container?* A generic LLM could invent schedules or safety rules. The goal is to retrieve information from a **small approved local document corpus** before responding and to cite the evidence used.

## 2. Supplied academic material

- [`notebooks/ecotrack-assistant-starter.ipynb`](notebooks/ecotrack-assistant-starter.ipynb) — original assignment notebook with **14 TODO markers** across incomplete exercises; retained as supplied except for a portfolio annotation.
- [`data/corpus_ecotrack/`](data/corpus_ecotrack/) — seven short policy and operating documents (recycling, collection, zones, privacy, platform).
- [`data/jeu_test_10_questions.csv`](data/jeu_test_10_questions.csv) — ten sample questions and expected source files.
- [`data/etat_conteneurs.csv`](data/etat_conteneurs.csv) — synthetic bin states for a zone lookup extension.
- [`data/bonus_document_injection.txt`](data/bonus_document_injection.txt) — **deliberate hostile instruction embedded in a document**; only add to retrieval experiments intentionally.

## 3. Original exercise pipeline

```text
Approved .txt documents
    ↓ load and clean
Overlapping text chunks
    ↓ multilingual sentence embeddings
Cosine similarity / Top-K
    ↓ grounding context and source IDs
Gemini answer generation + citations
    ↓
Refusal if evidence is insufficient; retrieval evaluation
```

### Concepts explored

1. **Document ingestion:** preserve document names as citation IDs.
2. **Chunking:** passage size and overlap balance retrieval precision against context coverage.
3. **Embeddings:** map passages and user questions to a shared semantic vector space.
4. **Top-K retrieval:** return candidate evidence passages with source names and scores.
5. **Grounded generation:** instruct the LLM to use the retrieved snippets and cite their identifiers.
6. **Evaluation:** compare the expected source against retrieved top-3 passages on ten questions.
7. **Safety:** keep a malicious document as untrusted data; never treat it as an agent instruction.

## 4. New portfolio enhancement: runnable Python application

`src/ecotrack/` is a **post-course enhancement**, separate from the teacher's unfinished starter. It offers:

- Deterministic document chunking and stable source identifiers.
- A multilingual Sentence Transformer retriever with cosine similarity.
- Offline evidence-only query mode (no Gemini key needed after the embedding model is available).
- Optional Gemini-based grounded answers when the `GEMINI_API_KEY` environment variable is available.
- Dataset-driven **source Hit@3** evaluation; note that the assignment calls this *précision@3*, but its stated formula is actually **Hit@3 / Recall@3 of the expected source**, not standard information-retrieval precision@3.
- A read-only tool for inspecting synthetic container states by zone.
- Unit tests for chunk overlap, ranking, evaluation, corpus loading and tool input filtering.

### Setup

```bash
cd 05-ecotrack-rag-assistant
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

> The sentence-transformers model downloads weights on the first run; internet access is needed initially. No paid API call is required for retrieval/evaluation.

### Search the knowledge base

```bash
python -m ecotrack --question "Quand les recyclables sont-ils collectés en zone Nord ?"
python -m ecotrack --evaluate
python -m ecotrack --zone Nord
```

### Optional generative response

```bash
# PowerShell: $env:GEMINI_API_KEY="..."
# Linux/macOS: export GEMINI_API_KEY="..."
python -m ecotrack --question "Où déposer les bouteilles en verre ?" --generate
```

### Execute tests (no Gemini call or model download)

```bash
python -m unittest discover -s tests -v
```

## 5. Architecture and safety limitations

- Generation requests include only retrieved context and a system instruction to cite source IDs. **This is a demo, not a proof of perfect grounding.** Validate model output and citations before production use.
- The default corpus is restricted to the seven approved documents; the separate injection example is deliberately excluded unless explicitly added for adversarial testing.
- A similarity threshold is heuristic; it must be tuned on labeled, representative questions before relying on abstention.
- The synthetic datasets are assignment examples, **not live municipal data**.
- There is no authenticated API, persistent database, production telemetry or GDPR compliance assessment.

## 6. Learning outcomes

- Understand the RAG workflow end to end and its failure modes.
- Contrast code-based retrieval evaluation with generated-answer correctness.
- Recognize that retrieved documents are data, not privileged instructions.
- Express a classroom notebook as a more maintainable Python package without erasing the original assignment state.

See [repository attribution guidelines](../ATTRIBUTION_AND_SHARING.md) before publication.
