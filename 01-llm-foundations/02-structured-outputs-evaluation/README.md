# Structured Outputs and LLM Evaluation

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can an application reliably consume an LLM answer and check response quality?

## Approach implemented / explored

- Specify constrained response formats and inspect generated data
- Build simple examples of LLM output evaluation
- Explore evaluation challenges and failure modes
- Consider retries and error handling for model-backed applications

## Technical stack

`Python`, `Google Gen AI SDK`, `Structured generation`, `Evaluation`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`structured-outputs-and-evaluation.ipynb`](./structured-outputs-and-evaluation.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- Compatible SDK and selected model access

## Limitations and honest scope

- Structured output support varies across models
- Evaluation examples are instructional rather than a production quality gate

**Evidence and results:** Demonstrates evaluation concepts and structured outputs, not production-grade benchmark scores.

## Provenance

Original learning material: `jour_1_evaluation_sortie_structuree_colab_fr.ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
