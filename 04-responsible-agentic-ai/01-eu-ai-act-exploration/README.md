# EU AI Act Compliance Exploration

> **INGETIS · Master-level studies · 2026–2027**  
> Portfolio maintainer: **Mohammed Alaa Eddine GUERBOUZ**  
> Type: classroom lab / adapted educational material

## Problem being explored

How can an AI agent retrieve formalized compliance rules and examine a hypothetical deployment scenario?

## Approach implemented / explored

- Call an external rule-service API and inspect available compliance modules
- Wrap tool calls in Python functions exposed to Gemini
- Explore rule retrieval for AI risk and transparency scenarios
- Inspect the function-call history and raw regulatory reference material

## Technical stack

`Python`, `Gemini API`, `HTTP/JSON-RPC`, `Agent Module`, `AI governance`.

## What this demonstrates

- Understanding of the concepts and implementation pattern explored in the notebook.
- Practical interaction with model APIs, data processing tools and/or agent workflows.
- Ability to discuss the trade-offs and operational constraints of this technique.

## Run the practical notebook

1. Open [`eu-ai-act-compliance-agent.ipynb`](./eu-ai-act-compliance-agent.ipynb) with Google Colab or Jupyter (Colab is preferred where configured by the original notebook).
2. Install the packages in its setup cells; run cells in order.
3. Configure model credentials through **Colab Secrets** or supported environment variables; never commit secrets.
4. Confirm model names, API quota and package versions supported by your own environment.

**Prerequisites**

- Gemini API key
- External Agent Module service availability and access policy

## Limitations and honest scope

- Educational pre-analysis is not legal advice or a legally sufficient compliance assessment
- External tool data and API availability can change

**Evidence and results:** Illustrative compliance analysis of a hypothetical insurance chatbot, not certification.

## Provenance

Original learning material: `Jour_4_Conformite_AI_Act_Gemini_Agent_Module_FR.ipynb`. The code cells and existing attribution were preserved in this portfolio cleanup. This is a study record, not a claim of independent authorship of third-party teaching material. See [repository attribution and sharing guidelines](../../ATTRIBUTION_AND_SHARING.md).
