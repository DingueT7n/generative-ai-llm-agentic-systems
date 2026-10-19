# Document Q&A using RAG and ChromaDB

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can a language model answer from retrieved documents instead of relying only on parametric memory?

## Approach implemented / explored

- Build a document embedding store with ChromaDB
- Retrieve relevant evidence for a user question
- Pass retrieved context to a generative model
- Discuss limitations and failure modes of grounded Q&A

## Technical stack

`Python`, `ChromaDB`, `Gemini API`, `Vector retrieval`, `RAG`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`chroma-document-rag.ipynb`](./chroma-document-rag.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- ChromaDB dependencies

## Limitations and honest scope

- Retrieval does not guarantee correctness
- Document boundaries, prompt injection and citation checking need more rigor in production

**Evidence and results:** Instructional RAG pipeline; no verified production grounding guarantees.

## Provenance

Original learning material: `jour_2_qa_documents_rag_colab_fr(1).ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
