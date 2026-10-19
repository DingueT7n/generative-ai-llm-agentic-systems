# Text Embeddings and Semantic Similarity

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

Why does keyword matching miss semantically equivalent requests, and how can vectors compare meaning?

## Approach implemented / explored

- Generate embeddings for example texts
- Compute and inspect similarity scores
- Compare pairs and reason about semantic distance
- Visualize results and consider retrieval uses

## Technical stack

`Python`, `Gemini embeddings`, `Pandas`, `Seaborn`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`text-embedding-similarity.ipynb`](./text-embedding-similarity.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- Model access for embeddings

## Limitations and honest scope

- Similarity scores are model dependent
- High vector similarity is not proof of factual correctness

**Evidence and results:** Exploratory similarity demonstrations; no external information retrieval benchmark.

## Provenance

Original learning material: `jour_2_embeddings_similarite_colab_fr.ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
