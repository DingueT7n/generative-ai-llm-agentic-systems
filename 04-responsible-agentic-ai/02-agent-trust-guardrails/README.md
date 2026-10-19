# Deterministic Trust Layer for Gemini Agents

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can application code constrain an agent before it executes a side-effecting tool?

## Approach implemented / explored

- Configure a normal Gemini call as a baseline
- Define an explicit policy for a demonstration tool
- Validate permitted arguments and access constraints outside the model
- Inspect traces and discuss auditability

## Technical stack

`Python`, `Gemini API`, `Pramagent`, `Deterministic tool policies`, `Audit traces`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`gemini-agent-guardrails.ipynb`](./gemini-agent-guardrails.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- Compatible Pramagent library and model access

## Limitations and honest scope

- Policy examples are educational and not a complete security boundary
- Always validate permissions within server-side applications

**Evidence and results:** Demonstrates guardrail concepts; not security certification.

## Provenance

Original learning material: `jour_4_Couche_de_confiance_Pramagent_Gemini_FR(1).ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
