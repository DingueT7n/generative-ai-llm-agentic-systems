# Multimodal Semantic Search

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can a single search workflow compare queries and assets across text and images?

## Approach implemented / explored

- Prepare a small multimodal demonstration dataset
- Generate embeddings for supported modalities
- Run semantic and cross-modal retrieval
- Inspect rankings and compare keyword search with semantic matching

## Technical stack

`Python`, `Gemini multimodal embeddings`, `NumPy`, `Pillow`, `Google Colab`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`multimodal-semantic-search.ipynb`](./multimodal-semantic-search.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key and access to the configured embedding model
- Internet for any external demonstration assets

## Limitations and honest scope

- Multimodal embedding support and model IDs can change
- Notebook contains embedded demonstration media and attribution from source material

**Evidence and results:** Search examples and exploratory retrieval; no independently verified real-world search precision.

## Provenance

Original learning material: `Jour_2_Recherche_sémantique_multimodale_(Colab,_FR).ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
