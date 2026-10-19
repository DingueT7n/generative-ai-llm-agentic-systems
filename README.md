# Generative AI, LLMs & Agentic Systems 

> **Master-level Generative AI coursework**  
> **Institution:** INGETIS (Paris, France)  
> **Academic year:** 2026–2027  
> **Student / portfolio maintainer:** **Mohammed Alaa Eddine GUERBOUZ**  
> **Content:** hands-on notebooks, course exercises and one clearly identified post-course code enhancement

## Overview

This repository brings together my practical learning work in **Large Language Models (LLMs), prompt engineering, embeddings, retrieval-augmented generation (RAG), multimodal search, AI agents and responsible AI** during my studies at **INGETIS**.

Rather than presenting every notebook as a separate GitHub repository, the material is organized by concept and difficulty: from calling an LLM, to semantic search, tool calling, agent workflows and governance. The folders contain the **original instructional source cells**, readable filenames and detailed descriptions of the problems and concepts explored.

**Scope note:** several notebooks are teaching materials/adapted exercises and retain original credits. The portfolio reflects hands-on study and is **not** a claim that all example notebooks were created independently. The EcoTrack starter was not completed in the upload; a **separate later enhancement** is supplied as runnable code.

## What problems these exercises explore

- **Unreliable LLM outputs:** use prompt controls, structured responses and evaluation.
- **Insufficient context:** represent texts as embeddings and retrieve relevant sources with RAG.
- **Connecting models to applications:** give agents explicit tools for database querying or workflow actions.
- **Stateful coordination:** use LangGraph to represent transitions and action state.
- **Governance and tool safety:** keep authorization, constraints and external facts outside model-controlled instructions.
- **Grounded domain assistance:** use an approved local document corpus for EcoTrack questions.

## Learning modules and projects

| Module | Exercise / project | Key concepts |
|---|---|---|
| [01 · LLM Foundations](01-llm-foundations/README.md) | [Prompt Engineering with Gemini](01-llm-foundations/01-prompt-engineering/README.md) | Prompt design, generation settings |
| | [Structured Outputs & Evaluation](01-llm-foundations/02-structured-outputs-evaluation/README.md) | Output contracts, evaluation |
| [02 · Embeddings & RAG](02-embeddings-and-rag/README.md) | [Semantic Similarity](02-embeddings-and-rag/01-semantic-similarity/README.md) | Vector representations, similarity |
| | [Keras Embedding Classification](02-embeddings-and-rag/02-embedding-classification/README.md) | Classification of text embeddings |
| | [Document RAG with ChromaDB](02-embeddings-and-rag/03-document-question-answering/README.md) | Retrieval, grounded QA |
| | [Multimodal Semantic Search](02-embeddings-and-rag/04-multimodal-search/README.md) | Text/image retrieval |
| [03 · Agentic AI](03-agentic-ai/README.md) | [Gemini Function Calling + SQLite](03-agentic-ai/01-function-calling-with-sqlite/README.md) | Tool use, SQL-backed Q&A |
| | [BaristaBot with LangGraph](03-agentic-ai/02-langgraph-stateful-agent/README.md) | Graph states, tools, ordering |
| [04 · Responsible Agentic AI](04-responsible-agentic-ai/README.md) | [EU AI Act Compliance Exploration](04-responsible-agentic-ai/01-eu-ai-act-exploration/README.md) | Rule retrieval, governance |
| | [Deterministic Agent Guardrails](04-responsible-agentic-ai/02-agent-trust-guardrails/README.md) | Tool policies, traces |
| | [Browser-enabled Gemini Agent](04-responsible-agentic-ai/03-browser-enabled-agent/README.md) | Browser tools, network safety |
| [05 · Applied Project](05-ecotrack-rag-assistant/README.md) | [EcoTrack RAG Assistant](05-ecotrack-rag-assistant/README.md) | Retrieval, citations, evaluation, security |

**Total:** 12 unique source notebooks. The duplicate files present in the upload have been consolidated. 11 notebook topics are classroom exercises; EcoTrack is an unfinished course project starter accompanied by newly added enhancement code.

## EcoTrack — highlighted applied case study

**Use case:** citizens and waste-management teams need answers grounded in an approved set of collection rules and operating documents. The original student starter introduces ingestion, chunking, embedding, top-k retrieval, Gemini grounded generation, source IDs, abstention, evaluation and prompt-injection testing.

A **later portfolio enhancement**, under [`05-ecotrack-rag-assistant/src`](05-ecotrack-rag-assistant/src/), demonstrates modular retrieval/evaluation code and unit tests without rewriting the teaching notebook or claiming the coursework TODOs were submitted as completed.

[Read the full EcoTrack architecture, setup and limitations](05-ecotrack-rag-assistant/README.md).

## Technologies practiced

`Python` · `Jupyter / Google Colab` · `Google Gen AI SDK / Gemini API` · `LangGraph` · `LangChain` · `Sentence Transformers` · `ChromaDB` · `Keras` · `scikit-learn` · `SQLite` · `NumPy` · `Pandas` · `Selenium` · `Vector Similarity` · `RAG` · `LLM Tool Calling`.

## Getting started

### 1. Notebook labs

Open the notebook in its project folder using **Google Colab**, and follow the setup cells. Many labs require a **Gemini API key** stored via Colab's Secrets panel under `GEMINI_API_KEY` or `GOOGLE_API_KEY` (as indicated by each source notebook). Some examples have model names or package versions that need updating to match your account and current SDK. **No external API calls have been run as part of this repository cleanup.**

### 2. EcoTrack extension

```bash
cd 05-ecotrack-rag-assistant
python -m venv .venv
# activate the environment
pip install -r requirements.txt
pip install -e .
python -m unittest discover -s tests -v
python -m ecotrack --question "Quand les recyclables sont-ils collectés en zone Nord ?"
python -m ecotrack --evaluate
```

Running retrieval downloads the sentence embedding model on first use. To call Gemini for answer generation, set `GEMINI_API_KEY` in your environment and add `--generate`.

## Academic provenance and transparency

| Item | Handling |
|---|---|
| University and date | Documented as **INGETIS / 2026–2027**, in each notebook's portfolio header |
| Notebook code | Source cell contents retained unchanged; new portfolio markdown cover added |
| Notebook duplicates | Two exact duplicates consolidated, originals listed in changelog |
| Unfinished code | Explicitly marked (especially EcoTrack); not hidden or represented as completed |
| Course slides/assignment PDFs | Stored in local `_private-course-reference/` but excluded from Git commits |
| Copyrighted educational examples | Credits preserved; publication requires permission when applicable |
| Secrets | Keep model credentials in private secrets/environment, never committed |
| Benchmarks | No claims of reproduced model performance without execution evidence |

Read [Attribution and Sharing](ATTRIBUTION_AND_SHARING.md), [Portfolio Changelog](PORTFOLIO_CHANGELOG.md) and [Source Inventory](SOURCE_INVENTORY.csv) before pushing to a public repository.

---

*Academic portfolio maintained by Mohammed Alaa Eddine GUERBOUZ · INGETIS (Paris, France) · 2026–2027. These examples demonstrate learning and experimentation; they are not represented as production deployments.*
