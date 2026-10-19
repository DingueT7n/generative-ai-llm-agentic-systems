# Gemini Function Calling with SQLite

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can an LLM use well-defined tools to answer questions from application data?

## Approach implemented / explored

- Create a local SQLite database with synthetic tables
- Define tools for listing tables, inspecting schemas and running queries
- Route model-selected calls to Python functions
- Explore a live streaming API demonstration

## Technical stack

`Python`, `Gemini API`, `SQLite`, `Function calling`, `JupySQL`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`gemini-function-calling-sqlite.ipynb`](./gemini-function-calling-sqlite.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- SQLite and notebook SQL extension
- Model support for the chosen function-calling mode

## Limitations and honest scope

- Database tool access requires strict query authorization and read-only policies in real applications
- Live API availability varies by account/model

**Evidence and results:** Demonstration using local synthetic database data; not a secured database agent.

## Provenance

Original learning material: `jour-3-appel-de-fonctions-colab-fr.ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
