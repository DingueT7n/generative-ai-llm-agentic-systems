# EcoTrack Assistant — Original Starter Notebook

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can a recycling-service assistant answer questions from an approved document corpus with traceable evidence?

## Approach implemented / explored

- Load supplied waste collection and policy documents
- Chunk text, embed passages and retrieve similar context
- Generate a document-grounded answer with citations and abstention
- Evaluate retrieval on 10 example questions and explore a prompt-injection document

## Technical stack

`Python`, `Sentence Transformers`, `Gemini API`, `Vector similarity`, `RAG`, `Pandas`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`ecotrack-assistant-starter.ipynb`](./ecotrack-assistant-starter.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Use the supplied data files in this repository
- Gemini API key for answer generation
- Local model download for embedding inference

## Limitations and honest scope

- The original notebook still contains TODO placeholders and is not a completed implementation
- A separate, explicitly labeled portfolio extension provides executable code and tests

**Evidence and results:** Original supplied coursework starter, clearly labeled unfinished.

## Provenance

Original learning material: `EcoTrack_Assistant_Depart.ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
