# Text Classification with Embeddings and Keras

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

Can pretrained text embeddings support a lightweight supervised classifier without training an LLM?

## Approach implemented / explored

- Fetch a text classification dataset (20 Newsgroups)
- Create embeddings to represent text numerically
- Train a Keras neural-network classifier
- Evaluate model predictions and try a custom example

## Technical stack

`Python`, `Google Gen AI SDK`, `scikit-learn`, `Keras`, `NumPy`, `Pandas`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`keras-embedding-classifier.ipynb`](./keras-embedding-classifier.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- External dataset access for 20 Newsgroups
- Keras backend and relevant dependencies

## Limitations and honest scope

- Training and evaluation should be split to avoid leakage
- Costs depend on embedding API calls and dataset size

**Evidence and results:** Includes training/evaluation code; no performance metrics were reproduced in this packaging process.

## Provenance

Original learning material: `jour_2_classification_embeddings_keras_colab_fr.ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
